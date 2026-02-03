import os
import sys
import requests
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book

# File handling imports
try:
    from docx import Document
except ImportError:
    Document = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

logger = logging.getLogger(__name__)


def create_table_html(headers, rows, title="Results"):
    """Generate a beautiful HTML table"""
    html = f'<h3 style="margin-bottom: 1rem; color: var(--primary);">{title}</h3>\n'
    html += '<table>\n'
    html += '<thead>\n<tr>\n'
    
    for header in headers:
        html += f'  <th>{header}</th>\n'
    
    html += '</tr>\n</thead>\n'
    html += '<tbody>\n'
    
    for row in rows:
        html += '<tr>\n'
        for cell in row:
            html += f'  <td>{cell}</td>\n'
        html += '</tr>\n'
    
    html += '</tbody>\n</table>\n'
    return html


def recommend(age, interest):
    """Fallback recommendation function with varied responses"""
    try:
        books = Book.query.all()
        age_filtered = [b for b in books if b.min_age <= age <= b.max_age]
        interest_lower = interest.lower()
        interest_filtered = [
            b for b in age_filtered
            if interest_lower in (b.category or "").lower() or
               interest_lower in (b.title or "").lower() or
               interest_lower in (b.description or "").lower()
        ]
        recommendations = interest_filtered if interest_filtered else age_filtered
        
        if not recommendations:
            msg = f"I couldn't find specific books about '{interest}' for {age}-year-olds."
            if age_filtered:
                msg += " However, here are some great age-appropriate books you might enjoy:"
                return msg + "\n\n" + format_books_table(age_filtered[:3])
            else:
                return f"No books found for {age}-year-olds. Please try again later!"
        
        # Format response with varied introductions
        intros = [
            f"Great question about {interest}! Here are some fantastic books for {age}-year-olds:",
            f"Oh, I love that topic! Based on your interest in {interest}, I'd recommend these books for {age}-year-olds:",
            f"Perfect! {interest} is such an interesting topic. For a {age}-year-old, I'd suggest these books:",
            f"Wonderful choice! I found some excellent books about {interest} for {age}-year-olds:",
        ]
        
        intro = intros[len(recommendations) % len(intros)]
        result = f"{intro}\n\n"
        result += format_books_table(recommendations[:5])
        
        return result
        
    except Exception as e:
        logger.error(f"Error in recommend: {str(e)}")
        return f"Unable to fetch recommendations. Please try again later."


def format_books_table(books):
    """Format books as HTML table"""
    if not books:
        return "No books found."
    
    headers = ["Title", "Author", "Category", "Age Range", "Description"]
    rows = []
    
    for book in books:
        rows.append([
            book.title or "Unknown",
            book.author or "Unknown",
            book.category or "General",
            f"{book.min_age}-{book.max_age}",
            (book.description or "No description")[:100] + ("..." if len(book.description or "") > 100 else "")
        ])
    
    return create_table_html(headers, rows, "📚 Book Recommendations")


def format_books(books):
    """Format books for display (legacy text format)"""
    result = ""
    for i, book in enumerate(books, 1):
        result += f"{i}. **{book.title}** by {book.author}\n"
        if book.description:
            result += f"   {book.description}\n"
        result += f"   Age range: {book.min_age}-{book.max_age}\n\n"
    return result


def ai_recommend(age, interest):
    """
    Get AI-powered book recommendations using Groq API
    Falls back to database recommendations if API fails
    """
    from config import Config
    
    api_key = Config.GROQ_API_KEY
    
    # If no API key, use fallback
    if not api_key or api_key == "your_groq_api_key_here" or api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
        logger.info("No Groq API key provided, using fallback recommendations")
        return recommend(age, interest)
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"""You are a helpful librarian recommending books for a {age}-year-old interested in {interest}.
Provide 3-5 age-appropriate book recommendations with brief descriptions.
Format: List each book with title, author, and why it's good for them."""
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system", "content": "You are a helpful librarian and reading coach for children and teens."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 1024
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            reply = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if reply:
                return reply
        else:
            logger.warning(f"Groq API error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in ai_recommend: {str(e)}")
    
    # Fallback to database recommendations
    return recommend(age, interest)


def ai_chat(age, user_message, conversation_history=None):
    """
    Conversational AI chat with context awareness.
    Uses Groq for general Q&A and SmartEDU LMS support.
    """
    from config import Config
    
    if conversation_history is None:
        conversation_history = []
    
    api_key = Config.GROQ_API_KEY
    
    # Build conversation messages
    messages = [
        {
            "role": "system",
            "content": (
                "You are SmartEDU LMS's AI assistant. Answer any question clearly and helpfully. "
                "If the user asks about learning, provide actionable steps and resources. "
                "If a question is ambiguous, ask a brief clarifying question. "
                "Keep responses concise but complete."
            )
        }
    ]
    
    # Add conversation history
    for msg in conversation_history:
        messages.append({
            "role": msg.get("role", "user"),
            "content": msg.get("content", "")
        })
    
    # Add current user message
    messages.append({
        "role": "user",
        "content": user_message
    })
    
    # If no API key or invalid, use fallback
    if not api_key or api_key == "gsk_YOUR_GROQ_API_KEY_HERE" or api_key == "your_groq_api_key_here":
        logger.info("No valid Groq API key, chatbot is not configured")
        return "The AI assistant is not configured yet. Please set GROQ_API_KEY in your .env file and try again."
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1024
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            reply = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if reply:
                return reply
        else:
            logger.warning(f"Groq API error: {response.status_code}")
            logger.warning(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in ai_chat: {str(e)}")
    
    # Fallback if API call fails
    return "The AI assistant is temporarily unavailable. Please check your GROQ_API_KEY and try again."


def generate_worksheet(subject, difficulty, num_questions=10, question_type="Mixed", topic=""):
    """
    Generate an educational worksheet using Groq API
    Returns formatted HTML for the worksheet
    """
    from config import Config
    
    api_key = Config.GROQ_API_KEY
    
    # If no API key, return error message
    if not api_key or api_key == "your_groq_api_key_here" or api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
        logger.warning("No Groq API key provided for worksheet generation")
        return generate_fallback_worksheet(subject, difficulty, num_questions, question_type, topic)
    
    try:
        # Build the prompt for worksheet generation
        topic_str = f" about {topic}" if topic else ""
        prompt = f"""Generate a comprehensive {difficulty} level {subject} worksheet{topic_str} with {num_questions} {question_type} questions.

Format the output as HTML with the following structure:
- Use <div class="question"> for each question
- Use <h3> for section headers
- Include answer space/lines for students
- Make it visually organized and printable

Requirements:
- Difficulty: {difficulty} (Beginner=basic concepts, Intermediate=applied knowledge, Advanced=critical thinking)
- Number of questions: {num_questions}
- Question type: {question_type}
- Subject: {subject}
{f'- Topic: {topic}' if topic else ''}

Generate the worksheet now:"""
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert educational content creator who generates clear, well-structured worksheets and study materials. Always format output as clean HTML that can be printed."
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 2048
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            worksheet_html = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            if worksheet_html:
                # Wrap in a div with styling
                return f"""<div class="worksheet">
                {worksheet_html}
                </div>"""
        else:
            logger.warning(f"Groq API error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in generate_worksheet: {str(e)}")
    
    # Fallback to basic worksheet
    return generate_fallback_worksheet(subject, difficulty, num_questions, question_type, topic)


def generate_fallback_worksheet(subject, difficulty, num_questions, question_type, topic):
    """Generate a basic fallback worksheet when API is not available"""
    html = f"""<div class="worksheet">
    <h2>📝 {subject} Worksheet</h2>
    <p><strong>Difficulty:</strong> {difficulty} | <strong>Questions:</strong> {num_questions}</p>
    <p><strong>Type:</strong> {question_type}</p>
    {f'<p><strong>Topic:</strong> {topic}</p>' if topic else ''}
    
    <hr style="margin: 2rem 0;">
"""
    
    # Generate basic questions
    question_templates = {
        "Beginner": [
            "What is the basic definition of {topic_or_subject}?",
            "Explain one key concept of {topic_or_subject}.",
            "Describe the importance of {topic_or_subject} in real life.",
        ],
        "Intermediate": [
            "Analyze the relationship between two concepts in {topic_or_subject}.",
            "Apply your knowledge of {topic_or_subject} to solve a real-world problem.",
            "Compare and contrast two aspects of {topic_or_subject}.",
        ],
        "Advanced": [
            "Critically evaluate the implications of {topic_or_subject}.",
            "Synthesize information from multiple sources about {topic_or_subject}.",
            "Propose a solution to a complex problem involving {topic_or_subject}.",
        ]
    }
    
    templates = question_templates.get(difficulty, question_templates["Intermediate"])
    topic_text = topic or subject
    
    # Cap to a reasonable maximum to avoid overly large responses
    max_questions = 50
    total_questions = min(num_questions, max_questions)

    for i in range(1, total_questions + 1):
        template = templates[(i - 1) % len(templates)]
        question = template.format(topic_or_subject=topic_text)
        html += f"""
    <div class="question" style="margin-bottom: 2rem;">
        <p><strong>Question {i}:</strong> {question}</p>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Answer: ________________________________________________________________</p>
    </div>
"""
    
    html += """
    <hr style="margin: 2rem 0;">
    <p style="text-align: center; color: var(--text-muted); font-size: 0.85rem;">
        Note: For a personalized worksheet with Groq API integration, ensure GROQ_API_KEY is configured.
    </p>
</div>"""
    
    return html


def extract_text_from_file(file_obj):
    """
    Extract text content from various file formats
    Supports: PDF, DOCX, DOC, TXT
    
    Args:
        file_obj: File object from Flask request
    
    Returns:
        str: Extracted text content
    """
    try:
        filename = file_obj.filename.lower()
        
        # Handle PDF files
        if filename.endswith('.pdf'):
            if PdfReader is None:
                return "PDF support not available. Please install PyPDF2."
            
            try:
                pdf_reader = PdfReader(file_obj)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text.strip()
            except Exception as e:
                logger.error(f"Error reading PDF: {str(e)}")
                return f"Error reading PDF file: {str(e)}"
        
        # Handle DOCX files
        elif filename.endswith('.docx') or filename.endswith('.doc'):
            if Document is None:
                return "DOCX support not available. Please install python-docx."
            
            try:
                doc = Document(file_obj)
                text = ""
                for paragraph in doc.paragraphs:
                    text += paragraph.text + "\n"
                return text.strip()
            except Exception as e:
                logger.error(f"Error reading DOCX: {str(e)}")
                return f"Error reading DOCX file: {str(e)}"
        
        # Handle TXT files
        elif filename.endswith('.txt'):
            try:
                file_obj.seek(0)
                text = file_obj.read().decode('utf-8')
                return text.strip()
            except Exception as e:
                logger.error(f"Error reading TXT: {str(e)}")
                return f"Error reading TXT file: {str(e)}"
        
        else:
            return f"Unsupported file format: {filename}. Supported formats: PDF, DOCX, DOC, TXT"
    
    except Exception as e:
        logger.error(f"Unexpected error in extract_text_from_file: {str(e)}")
        return f"Error processing file: {str(e)}"


def analyze_content(content, analysis_type="summary", detail_level="Detailed", questions_answered=None, total_questions=None):
    """
    Analyze educational content using Groq API
    Returns analysis as text
    
    Args:
        content: The text content to analyze
        analysis_type: Type of analysis (summary, explain, keypoints, questions, assessment)
        detail_level: Level of detail (Brief, Detailed, Comprehensive)
        questions_answered: Number of questions answered (for assessment)
        total_questions: Total number of questions (for assessment)
    """
    from config import Config
    
    api_key = Config.GROQ_API_KEY
    
    # If no API key, return fallback analysis
    if not api_key or api_key == "your_groq_api_key_here" or api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
        logger.warning("No Groq API key provided for content analysis")
        return generate_fallback_analysis(content, analysis_type, detail_level)
    
    try:
        # Build prompt based on analysis type
        analysis_prompts = {
            "summary": f"Provide a clear and concise summary of the following content in {detail_level.lower()} detail:",
            "explain": f"Explain the main concepts in the following content in {detail_level.lower()} detail. Make it easy to understand:",
            "keypoints": f"Extract and list the key points from the following content. Detail level: {detail_level}:",
            "questions": f"Generate {3 if detail_level == 'Brief' else 5 if detail_level == 'Detailed' else 8} study questions based on the following content:",
            "assessment": "Analyze the student's test/quiz performance"
        }
        
        # Build the prompt
        if analysis_type == "assessment" and questions_answered is not None and total_questions is not None:
            score_percentage = round((questions_answered / total_questions) * 100)
            prompt = f"""The student has completed a test/quiz and answered {questions_answered} out of {total_questions} questions correctly (Score: {score_percentage}%).

Here is the test content/material:
{content}

Please provide:
1. A summary of their performance
2. Key areas they did well in
3. Areas that need improvement based on the content
4. Specific recommendations for studying the weak areas
5. Encouragement and next steps

Be constructive and supportive in your feedback."""
        else:
            prompt = f"""{analysis_prompts.get(analysis_type, analysis_prompts['summary'])}

{content}

Provide a {detail_level.lower()} analysis."""
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert educational tutor who provides clear, accurate, and helpful analysis of educational content. Format your response for readability."
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 1024
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            analysis = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            if analysis:
                return analysis
        else:
            logger.warning(f"Groq API error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in analyze_content: {str(e)}")
    
    # Fallback analysis
    return generate_fallback_analysis(content, analysis_type, detail_level, questions_answered, total_questions)


def generate_fallback_analysis(content, analysis_type, detail_level, questions_answered=None, total_questions=None):
    """Generate basic fallback analysis when API is not available"""
    analysis_type_titles = {
        "summary": "Summary",
        "explain": "Explanation",
        "keypoints": "Key Points",
        "questions": "Study Questions",
        "assessment": "Test Performance Assessment"
    }
    
    title = analysis_type_titles.get(analysis_type, "Analysis")
    word_count = len(content.split())
    
    # Special handling for assessment type
    if analysis_type == "assessment" and questions_answered is not None and total_questions is not None:
        score_percentage = round((questions_answered / total_questions) * 100)
        fallback_text = f"""## Test Performance Assessment

### Your Score
- **Questions Answered:** {questions_answered} out of {total_questions}
- **Percentage:** {score_percentage}%
- **Performance:** """
        
        if score_percentage >= 90:
            fallback_text += "Excellent! Outstanding performance!"
        elif score_percentage >= 80:
            fallback_text += "Very Good! Strong understanding demonstrated."
        elif score_percentage >= 70:
            fallback_text += "Good! Solid grasp of the material."
        elif score_percentage >= 60:
            fallback_text += "Satisfactory. Some areas need improvement."
        else:
            fallback_text += "Needs Improvement. Consider reviewing the material."
        
        fallback_text += f"""

### Analysis
Based on your performance of {score_percentage}% on this test, here's some guidance:

**What You Did Well:**
- You demonstrated understanding of {score_percentage}% of the tested material
- Continue practicing the concepts you've mastered

**Areas for Improvement:**
- Focus on the {100 - score_percentage}% of material where you had difficulty
- Review the key concepts multiple times
- Try practice problems for challenging topics

**Recommendations:**
1. Go back and review the material you found difficult
2. Study the content in smaller chunks
3. Try teaching the material to someone else
4. Practice similar problems multiple times
5. Consider studying with a peer or getting tutoring help

**Next Steps:**
- Create a study plan focusing on weak areas
- Set achievable goals for improvement
- Take another practice test after studying
- Track your progress over time

**Encouragement:**
Learning is a journey! Every attempt helps you improve. Keep practicing and you'll see your scores increase!

---

*Note: For AI-powered detailed analysis with personalized feedback, please ensure your GROQ_API_KEY is properly configured.*
"""
    else:
        fallback_text = f"""## {title}

This is a basic analysis. For comprehensive AI-powered analysis with Groq API integration, please ensure your GROQ_API_KEY is properly configured.

### Content Overview
- Original content length: {word_count} words
- Analysis type: {analysis_type.replace('_', ' ').title()}
- Detail level: {detail_level}

### Quick Insights
The provided content appears to be educational material related to {' '.join(content.split()[:3])} topics.

**Note:** To enable full AI-powered analysis:
1. Set up your Groq API key in the environment variables
2. Configure GROQ_API_KEY in your .env file
3. The system will then provide detailed, intelligent analysis of your content

### Next Steps
- Review the original content carefully
- Identify key concepts and main ideas
- Consider how this content relates to your learning goals
- Use this information to create study notes and summaries
"""
    
    return fallback_text


def generate_project_feedback(project_title, submission, difficulty="intermediate", repo=""):
    """
    Generate feedback for a guided project submission.
    Returns actionable feedback with strengths, improvements, and next steps.
    """
    from config import Config

    api_key = Config.GROQ_API_KEY

    if not api_key or api_key == "your_groq_api_key_here" or api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
        logger.warning("No Groq API key provided for project feedback")
        return generate_fallback_project_feedback(project_title, submission, difficulty, repo)

    try:
        prompt = f"""You are a senior instructor providing feedback on a learner project.
Project: {project_title}
Difficulty: {difficulty}
Repo link (optional): {repo or 'N/A'}

Submission:
{submission}

Provide structured feedback with the following sections:
1. Summary (2-3 sentences)
2. Strengths (3 bullets)
3. Improvements (3 bullets)
4. Next Steps (3 bullets)
5. Score (1-5) with a short reason

Be supportive, specific, and actionable."""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert software instructor and coach. Give clear, actionable feedback."
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.6,
                "max_tokens": 900
            },
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            reply = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if reply:
                return reply
        else:
            logger.warning(f"Groq API error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in generate_project_feedback: {str(e)}")

    return generate_fallback_project_feedback(project_title, submission, difficulty, repo)


def generate_fallback_project_feedback(project_title, submission, difficulty="intermediate", repo=""):
    """Fallback feedback when AI service is unavailable."""
    snippet = submission[:300].strip().replace("\n", " ")
    return f"""Project Feedback: {project_title}

Summary:
You submitted a project at the {difficulty} level. Your response includes: {snippet if snippet else 'a project description'}.

Strengths:
- You provided a clear submission outline.
- You documented key parts of your approach.
- You shared enough detail to review your work.

Improvements:
- Add more concrete examples or code snippets.
- Explain why you made specific decisions.
- Include screenshots or outputs where possible.

Next Steps:
- Refine the project based on the improvement list.
- Test your solution with edge cases.
- Add a short README explaining setup and usage.

Score: 3/5 (Good progress; add more evidence and detail for a stronger submission.)"""

