from flask import Blueprint, request, jsonify
from sqlalchemy import func
from extensions import db
from models.lesson import Lesson
from models.book import Book
from models.user import User
import json
import logging

bp = Blueprint("admin", __name__)
logger = logging.getLogger(__name__)


def _normalize_difficulty(value):
    if not value:
        return "unknown"
    return str(value).strip().lower()


def _parse_json_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return []
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, list) else []
        except json.JSONDecodeError:
            return []
    return []


@bp.route("/admin/overview", methods=["GET"])
def admin_overview():
    """Return summary stats and recent content for admin dashboards."""
    try:
        lessons = Lesson.query.all()

        subject_counts = {}
        difficulty_counts = {}

        for lesson in lessons:
            subject = lesson.subject or "General"
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

            difficulty = _normalize_difficulty(lesson.difficulty)
            difficulty_counts[difficulty] = difficulty_counts.get(difficulty, 0) + 1

        avg_duration = db.session.query(func.avg(Lesson.duration_minutes)).scalar() or 0

        latest_lessons = Lesson.query.order_by(Lesson.created_at.desc()).limit(6).all()

        return jsonify({
            "success": True,
            "counts": {
                "lessons": Lesson.query.count(),
                "books": Book.query.count(),
                "users": User.query.count()
            },
            "avg_duration": round(avg_duration, 1),
            "subject_counts": subject_counts,
            "difficulty_counts": difficulty_counts,
            "latest_lessons": [
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "subject": lesson.subject,
                    "difficulty": lesson.difficulty,
                    "duration_minutes": lesson.duration_minutes,
                    "created_at": lesson.created_at.isoformat() if lesson.created_at else None
                }
                for lesson in latest_lessons
            ]
        }), 200
    except Exception as e:
        logger.error(f"Admin overview error: {str(e)}")
        return jsonify({"error": "Failed to load overview", "details": str(e)}), 500


@bp.route("/admin/lessons", methods=["GET"])
def list_lessons():
    """List lessons for admin tooling."""
    try:
        limit = request.args.get("limit", default=100, type=int)
        lessons = Lesson.query.order_by(Lesson.created_at.desc()).limit(limit).all()
        return jsonify({
            "success": True,
            "data": [
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "subject": lesson.subject,
                    "difficulty": lesson.difficulty,
                    "duration_minutes": lesson.duration_minutes
                } for lesson in lessons
            ]
        }), 200
    except Exception as e:
        logger.error(f"List lessons error: {str(e)}")
        return jsonify({"error": "Failed to list lessons", "details": str(e)}), 500


@bp.route("/admin/lessons", methods=["POST"])
def create_lesson():
    """Create a new lesson."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        title = (data.get("title") or "").strip()
        description = (data.get("description") or "").strip()
        subject = (data.get("subject") or "").strip()
        difficulty = (data.get("difficulty") or "").strip().lower()

        if not title or not description or not subject or not difficulty:
            return jsonify({"error": "title, description, subject, and difficulty are required"}), 400

        lesson = Lesson(
            title=title,
            description=description,
            subject=subject,
            difficulty=difficulty,
            content=data.get("content"),
            information=data.get("information"),
            video_url=data.get("video_url"),
            steps=_parse_json_list(data.get("steps")),
            quiz=_parse_json_list(data.get("quiz")),
            min_age=data.get("min_age", 5),
            max_age=data.get("max_age", 18),
            duration_minutes=data.get("duration_minutes", 30)
        )

        db.session.add(lesson)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Lesson created",
            "lesson": lesson.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Create lesson error: {str(e)}")
        return jsonify({"error": "Failed to create lesson", "details": str(e)}), 500


@bp.route("/admin/lessons/<int:lesson_id>", methods=["PUT"])
def update_lesson(lesson_id):
    """Update an existing lesson."""
    try:
        lesson = Lesson.query.get(lesson_id)
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        if "title" in data:
            lesson.title = (data.get("title") or "").strip()
        if "description" in data:
            lesson.description = (data.get("description") or "").strip()
        if "subject" in data:
            lesson.subject = (data.get("subject") or "").strip()
        if "difficulty" in data:
            lesson.difficulty = (data.get("difficulty") or "").strip().lower()
        if "content" in data:
            lesson.content = data.get("content")
        if "information" in data:
            lesson.information = data.get("information")
        if "video_url" in data:
            lesson.video_url = data.get("video_url")
        if "steps" in data:
            lesson.steps = _parse_json_list(data.get("steps"))
        if "quiz" in data:
            lesson.quiz = _parse_json_list(data.get("quiz"))
        if "min_age" in data:
            lesson.min_age = data.get("min_age", lesson.min_age)
        if "max_age" in data:
            lesson.max_age = data.get("max_age", lesson.max_age)
        if "duration_minutes" in data:
            lesson.duration_minutes = data.get("duration_minutes", lesson.duration_minutes)

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Lesson updated",
            "lesson": lesson.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        logger.error(f"Update lesson error: {str(e)}")
        return jsonify({"error": "Failed to update lesson", "details": str(e)}), 500


@bp.route("/admin/quality-check", methods=["GET"])
def quality_check():
    """Return lessons with missing fields for moderation review."""
    try:
        lessons = Lesson.query.all()
        flagged = []

        for lesson in lessons:
            issues = []
            if not lesson.description or len(lesson.description) < 60:
                issues.append("Short or missing description")
            if not lesson.content:
                issues.append("Missing lesson content")
            if not lesson.steps:
                issues.append("Missing steps")
            if not lesson.quiz:
                issues.append("Missing quiz")
            if not lesson.information:
                issues.append("Missing key information")
            if not lesson.video_url:
                issues.append("Missing video URL")

            if issues:
                flagged.append({
                    "id": lesson.id,
                    "title": lesson.title,
                    "subject": lesson.subject,
                    "difficulty": lesson.difficulty,
                    "issues": issues
                })

        return jsonify({
            "success": True,
            "count": len(flagged),
            "data": flagged
        }), 200
    except Exception as e:
        logger.error(f"Quality check error: {str(e)}")
        return jsonify({"error": "Failed to run quality check", "details": str(e)}), 500
