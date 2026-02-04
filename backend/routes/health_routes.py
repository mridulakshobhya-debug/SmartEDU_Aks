from flask import Blueprint, jsonify
from sqlalchemy import text
from extensions import db
from models.lesson import Lesson
from models.book import Book
from models.user import User

bp = Blueprint("health", __name__)


@bp.route("/health", methods=["GET"])
def health_check():
    """Simple health check for Vercel."""
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"ok": True, "db": "up"}), 200
    except Exception as e:
        return jsonify({"ok": False, "db": "down", "error": str(e)}), 500


@bp.route("/diagnostics", methods=["GET"])
def diagnostics():
    """Return lightweight diagnostics (no secrets)."""
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({
            "ok": True,
            "counts": {
                "lessons": Lesson.query.count(),
                "books": Book.query.count(),
                "users": User.query.count()
            }
        }), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
