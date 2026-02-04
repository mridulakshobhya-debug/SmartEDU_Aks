from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import sys
import tempfile

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import config_by_name
from extensions import db
from routes.book_routes import bp as book_bp
from routes.lesson_routes import bp as lesson_bp
from routes.chatbot_routes import bp as chatbot_bp
from routes.auth import bp as auth_bp
from routes.ai_tools_routes import bp as ai_tools_bp
from routes.admin_routes import bp as admin_bp


def create_app(config_name=None):
    """Create and configure Flask application"""
    if config_name is None:
        config_name = os.getenv("FLASK_ENV") or ("production" if os.getenv("VERCEL") else "development")
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create instance folder if it doesn't exist (Vercel filesystem is read-only except /tmp)
    instance_path = (
        os.path.join(tempfile.gettempdir(), "smartedu_instance")
        if os.getenv("VERCEL")
        else os.path.join(project_root, "instance")
    )
    os.makedirs(instance_path, exist_ok=True)
    
    static_folder = os.path.join(project_root, "public")
    app = Flask(__name__, static_folder=static_folder, static_url_path="/", instance_path=instance_path)
    app.config.from_object(config_by_name.get(config_name, config_by_name["development"]))
    
    # Initialize CORS
    cors_origins = app.config.get("CORS_ORIGINS", "*")
    if isinstance(cors_origins, str):
        cors_origins = [o.strip() for o in cors_origins.split(",") if o.strip()] or "*"
    supports_credentials = False if cors_origins == "*" else True
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": cors_origins,
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
        supports_credentials=supports_credentials,
    )
    
    # Initialize database BEFORE importing routes
    db.init_app(app)
    
    # Import routes AFTER db initialization
    from routes.book_routes import bp as book_bp
    from routes.lesson_routes import bp as lesson_bp
    from routes.chatbot_routes import bp as chatbot_bp
    from routes.auth import bp as auth_bp
    from routes.ai_tools_routes import bp as ai_tools_bp
    
    # Register blueprints
    app.register_blueprint(book_bp, url_prefix="/api")
    app.register_blueprint(lesson_bp, url_prefix="/api")
    app.register_blueprint(chatbot_bp, url_prefix="/api")
    app.register_blueprint(ai_tools_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api")
    
    # Routes
    @app.route("/")
    def home():
        return send_from_directory(app.static_folder, "index.html")
    
    @app.route("/elearning.html")
    def elearning():
        return send_from_directory(app.static_folder, "elearning.html")
    
    @app.route("/ai-tools.html")
    def ai_tools():
        return send_from_directory(app.static_folder, "ai-tools.html")

    @app.route("/admin.html")
    def admin():
        return send_from_directory(app.static_folder, "admin.html")

    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Route not found"}, 404
    
    @app.errorhandler(500)
    def server_error(error):
        return {"error": "Internal server error"}, 500
    
    # Create database tables
    with app.app_context():
        db.create_all()
        # Auto-seed on start when database is empty
        auto_seed = os.getenv("AUTO_SEED", "true").strip().lower() in {"1", "true", "yes", "on"}
        if auto_seed and not app.config.get("TESTING", False):
            try:
                from models.lesson import Lesson
                from models.book import Book
                from models.user import User
                from seed import seed_all

                has_lessons = Lesson.query.first() is not None
                has_books = Book.query.first() is not None
                has_users = User.query.first() is not None

                if not (has_lessons or has_books or has_users):
                    seed_all(reset_db=False, clear_users=False)
            except Exception as e:
                app.logger.error(f"Auto-seed failed: {e}")
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host="0.0.0.0", port=5000, use_reloader=False)
