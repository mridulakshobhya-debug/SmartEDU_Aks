import os
from flask import current_app

from models.book import Book
from models.lesson import Lesson
from models.user import User
from seed import seed_all

_seed_attempted = False


def ensure_seeded():
    """Seed once when database is empty and AUTO_SEED is enabled."""
    global _seed_attempted

    if _seed_attempted:
        return False

    if current_app and current_app.config.get("TESTING", False):
        return False

    auto_seed = os.getenv("AUTO_SEED", "true").strip().lower() in {"1", "true", "yes", "on"}
    if not auto_seed:
        return False

    has_lessons = Lesson.query.first() is not None
    has_books = Book.query.first() is not None
    has_users = User.query.first() is not None

    if has_lessons or has_books or has_users:
        return False

    _seed_attempted = True
    seed_all(reset_db=False, clear_users=False)
    return True
