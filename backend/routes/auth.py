from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from sqlalchemy import func
import logging

bp = Blueprint("auth", __name__)
logger = logging.getLogger(__name__)


@bp.route("/signup", methods=["POST"])
def signup():
    """Register a new user"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        username = data.get("username", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "")
        full_name = data.get("full_name", "").strip()
        age = data.get("age")
        
        # Validation
        if not username or len(username) < 3:
            return jsonify({"error": "Username must be at least 3 characters"}), 400
        
        if not email or "@" not in email:
            return jsonify({"error": "Valid email is required"}), 400
        
        if not password or len(password) < 6:
            return jsonify({"error": "Password must be at least 6 characters"}), 400
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 409
        
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 409
        
        # Create new user
        user = User(
            username=username,
            email=email,
            full_name=full_name or username,
            age=age
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        logger.info(f"New user registered: {username}")
        
        return jsonify({
            "success": True,
            "message": "Account created successfully!",
            "user": user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Signup error: {str(e)}")
        return jsonify({"error": "Failed to create account", "details": str(e)}), 500


@bp.route("/login", methods=["POST"])
def login():
    """Login user"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        username_or_email = data.get("username", "").strip()
        password = data.get("password", "")
        
        if not username_or_email or not password:
            return jsonify({"error": "Username/email and password are required"}), 400
        
        # Find user by username or email
        identifier = username_or_email.strip()
        identifier_lower = identifier.lower()
        user = User.query.filter(
            (func.lower(User.username) == identifier_lower)
            | (func.lower(User.email) == identifier_lower)
        ).first()
        
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid username/email or password"}), 401
        
        logger.info(f"User logged in: {user.username}")
        
        return jsonify({
            "success": True,
            "message": "Login successful!",
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({"error": "Login failed", "details": str(e)}), 500


@bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get user details"""
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({
            "success": True,
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        logger.error(f"Get user error: {str(e)}")
        return jsonify({"error": "Failed to fetch user"}), 500


@bp.route("/user/<int:user_id>/update", methods=["PUT"])
def update_user(user_id):
    """Update user profile"""
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        data = request.get_json()
        
        if "full_name" in data:
            user.full_name = data["full_name"].strip()
        
        if "age" in data:
            user.age = data["age"]
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Profile updated successfully",
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Update user error: {str(e)}")
        return jsonify({"error": "Failed to update profile"}), 500
