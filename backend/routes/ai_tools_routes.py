from flask import Blueprint, request, jsonify
from services.ai_service import generate_worksheet, analyze_content, extract_text_from_file
import logging

bp = Blueprint("ai_tools", __name__)
logger = logging.getLogger(__name__)


@bp.route("/generate-worksheet", methods=["POST"])
def generate_worksheet_endpoint():
    """Generate a worksheet using AI"""
    try:
        data = request.get_json()
        
        # Validation
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        subject = data.get("subject")
        difficulty = data.get("difficulty")
        num_questions = data.get("numQuestions", 10)
        question_type = data.get("questionType", "Mixed")
        topic = data.get("topic", "")
        
        # Validate required fields
        if not subject or not difficulty:
            return jsonify({"error": "subject and difficulty are required"}), 400
        
        if not isinstance(num_questions, int) or num_questions < 1 or num_questions > 50:
            return jsonify({"error": "numQuestions must be between 1 and 50"}), 400
        
        # Generate worksheet
        worksheet_html = generate_worksheet(
            subject=subject,
            difficulty=difficulty,
            num_questions=num_questions,
            question_type=question_type,
            topic=topic
        )
        
        return jsonify({
            "success": True,
            "subject": subject,
            "difficulty": difficulty,
            "worksheet": worksheet_html
        }), 200
        
    except Exception as e:
        logger.error(f"Worksheet generation error: {str(e)}")
        return jsonify({"error": "Failed to generate worksheet", "details": str(e)}), 500


@bp.route("/analyze-content", methods=["POST"])
def analyze_content_endpoint():
    """Analyze educational content using AI (supports file upload or text)"""
    try:
        # Check if it's a file upload
        if 'file' in request.files:
            file = request.files['file']
            analysis_type = request.form.get("analysisType", "summary")
            detail_level = request.form.get("detailLevel", "Detailed")
            questions_answered = request.form.get("questionsAnswered", type=int)
            total_questions = request.form.get("totalQuestions", type=int)
            
            # Validate file
            if file.filename == '':
                return jsonify({"error": "No file selected"}), 400
            
            # Extract text from file
            content = extract_text_from_file(file)
            
            # Check if extraction failed
            if content.startswith("Error") or content.startswith("Unsupported") or content.startswith("PDF support"):
                return jsonify({"error": content}), 400
            
            if not content or len(content) < 10:
                return jsonify({"error": "File appears to be empty or too short. Minimum 10 characters required"}), 400
        else:
            # Text-based analysis
            data = request.get_json()
            
            # Validation
            if not data:
                return jsonify({"error": "Request body is required"}), 400
            
            content = data.get("content")
            analysis_type = data.get("analysisType", "summary")
            detail_level = data.get("detailLevel", "Detailed")
            questions_answered = data.get("questionsAnswered")
            total_questions = data.get("totalQuestions")
            
            # Validate required fields
            if not content:
                return jsonify({"error": "content is required"}), 400
            
            if len(content) < 10:
                return jsonify({"error": "content must be at least 10 characters long"}), 400
        
        # Analyze content
        analysis_result = analyze_content(
            content=content,
            analysis_type=analysis_type,
            detail_level=detail_level,
            questions_answered=questions_answered,
            total_questions=total_questions
        )
        
        return jsonify({
            "success": True,
            "analysisType": analysis_type,
            "analysis": analysis_result
        }), 200
        
    except Exception as e:
        logger.error(f"Content analysis error: {str(e)}")
        return jsonify({"error": "Failed to analyze content", "details": str(e)}), 500
