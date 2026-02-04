from flask import Blueprint, request, jsonify
from models.lesson import Lesson
from services.seed_runner import ensure_seeded

bp = Blueprint("lessons", __name__)


@bp.route("/lessons", methods=["GET"])
def get_lessons():
    """Get lessons - no age requirement for inclusive access"""
    try:
        ensure_seeded()

        subject = request.args.get("subject", type=str)
        difficulty = request.args.get("difficulty", type=str)
        
        # Build query - load all lessons without age filtering
        query = Lesson.query
        
        if subject:
            query = query.filter_by(subject=subject)
        
        if difficulty:
            query = query.filter_by(difficulty=difficulty)
        
        lessons = query.all()
        
        return jsonify({
            "success": True,
            "count": len(lessons),
            "data": [l.to_dict() for l in lessons]
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/lessons/<int:lesson_id>", methods=["GET"])
def get_lesson(lesson_id):
    """Get a specific lesson by ID"""
    try:
        lesson = Lesson.query.get(lesson_id)
        
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404
        
        return jsonify({
            "success": True,
            "data": lesson.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
