from flask import Blueprint, request, jsonify
from models.book import Book
from services.age_guard import allowed

bp = Blueprint("books", __name__)


@bp.route("/books", methods=["GET"])
def get_books():
    """Get books filtered by user age"""
    try:
        age = request.args.get("age", type=int)
        
        if age is None:
            return jsonify({"error": "Age parameter is required"}), 400
        
        if age < 5 or age > 100:
            return jsonify({"error": "Age must be between 5 and 100"}), 400
        
        books = Book.query.all()
        filtered_books = [b.to_dict() for b in books if allowed(age, b)]
        
        return jsonify({
            "success": True,
            "count": len(filtered_books),
            "data": filtered_books
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    """Get a specific book by ID"""
    try:
        book = Book.query.get(book_id)
        
        if not book:
            return jsonify({"error": "Book not found"}), 404
        
        return jsonify({
            "success": True,
            "data": book.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
