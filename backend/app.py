from flask import Flask, send_file
from flask_cors import CORS
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import config_by_name
from extensions import db
from routes.book_routes import bp as book_bp
from routes.lesson_routes import bp as lesson_bp
from routes.chatbot_routes import bp as chatbot_bp
from routes.auth import bp as auth_bp


def create_app(config_name=None):
    """Create and configure Flask application"""
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")
    
    app = Flask(__name__, static_folder="../frontend", static_url_path="/")
    app.config.from_object(config_by_name.get(config_name, config_by_name["development"]))
    
    # Initialize CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(book_bp, url_prefix="/api")
    app.register_blueprint(lesson_bp, url_prefix="/api")
    app.register_blueprint(chatbot_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    # Routes
    @app.route("/")
    def home():
        return send_file("../frontend/index.html")
    
    @app.route("/elearning.html")
    def elearning():
        return send_file("../frontend/elearning.html")
    
    @app.route("/chatbot.html")
    def chatbot():
        return send_file("../frontend/chatbot.html")
    
    @app.route("/login.html")
    def login():
        return send_file("../frontend/login.html")
    
    @app.route("/signup.html")
    def signup():
        return send_file("../frontend/signup.html")
    
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Route not found"}, 404
    
    @app.errorhandler(500)
    def server_error(error):
        return {"error": "Internal server error"}, 500
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
