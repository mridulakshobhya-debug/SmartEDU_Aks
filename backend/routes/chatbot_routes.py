from flask import Blueprint, request, jsonify
from services.ai_service import ai_recommend, ai_chat
import logging

bp = Blueprint("chatbot", __name__)
logger = logging.getLogger(__name__)


@bp.route("/chatbot", methods=["POST"])
def chatbot():
    """Book recommendation and AI chat endpoint"""
    try:
        data = request.get_json()
        
        # Validation
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Check if this is a book recommendation request (has age and interest)
        age = data.get("age")
        interest = data.get("interest")
        
        if age is not None and interest is not None:
            # Book recommendation request
            if not interest or not isinstance(interest, str) or len(interest) < 1:
                return jsonify({"error": "interest must be a non-empty string"}), 400
            
            try:
                age = int(age)
            except (TypeError, ValueError):
                return jsonify({"error": "age must be a valid integer"}), 400
            
            # Get book recommendations
            reply = ai_recommend(age, interest)
            
            return jsonify({
                "success": True,
                "age": age,
                "interest": interest,
                "reply": reply
            }), 200
        else:
            # Chat message request
            user_message = data.get("user_message")
            conversation_history = data.get("conversation_history", [])
            
            if not user_message:
                return jsonify({"error": "user_message field is required"}), 400
            
            if not isinstance(user_message, str) or len(user_message) < 2:
                return jsonify({"error": "user_message must be a string with at least 2 characters"}), 400
            
            # Get chat response with conversation history
            # Using age 14 as default for content-appropriate recommendations
            reply = ai_chat(14, user_message, conversation_history)
            
            return jsonify({
                "success": True,
                "user_message": user_message,
                "reply": reply
            }), 200
        
    except Exception as e:
        logger.error(f"Chatbot error: {str(e)}")
        return jsonify({"error": "Failed to process request", "details": str(e)}), 500
