from flask import Blueprint, request, jsonify
from services.ai_service import ai_recommend, ai_chat
import logging

bp = Blueprint("chatbot", __name__)
logger = logging.getLogger(__name__)


@bp.route("/chatbot", methods=["POST"])
def chatbot():
    """AI-powered chatbot endpoint with conversation support"""
    try:
        data = request.get_json()
        
        # Validation
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        user_message = data.get("user_message")
        conversation_history = data.get("conversation_history", [])
        
        if not user_message:
            return jsonify({"error": "user_message field is required"}), 400
        
        if not isinstance(user_message, str) or len(user_message) < 2:
            return jsonify({"error": "user_message must be a string with at least 2 characters"}), 400
        
        # Get recommendations/chat response with conversation history
        # Using age 14 as default for content-appropriate recommendations
        reply = ai_chat(14, user_message, conversation_history)
        
        return jsonify({
            "success": True,
            "user_message": user_message,
            "reply": reply
        }), 200
        
    except Exception as e:
        logger.error(f"Chatbot error: {str(e)}")
        return jsonify({"error": "Failed to process recommendation", "details": str(e)}), 500
