import os
import sys
import requests
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book

logger = logging.getLogger(__name__)


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
            return f"I couldn't find specific books about '{interest}' for {age}-year-olds. However, here are some great age-appropriate books you might enjoy:\n\n" + format_books(age_filtered[:3]) if age_filtered else f"No books found for {age}-year-olds. Please try again later!"
        
        # Format response with varied introductions
        intros = [
            f"Great question about {interest}! Here are some fantastic books for {age}-year-olds:",
            f"Oh, I love that topic! Based on your interest in {interest}, I'd recommend these books for {age}-year-olds:",
            f"Perfect! {interest} is such an interesting topic. For a {age}-year-old, I'd suggest these books:",
            f"Wonderful choice! I found some excellent books about {interest} for {age}-year-olds:",
        ]
        
        intro = intros[len(recommendations) % len(intros)]
        result = f"{intro}\n\n"
        result += format_books(recommendations[:5])
        
        return result
        
    except Exception as e:
        logger.error(f"Error in recommend: {str(e)}")
        return f"Unable to fetch recommendations. Please try again later."


def format_books(books):
    """Format books for display"""
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
    Conversational AI chat with context awareness
    Uses conversation history for more intelligent responses
    Falls back to recommendations if API unavailable
    """
    from config import Config
    
    if conversation_history is None:
        conversation_history = []
    
    api_key = Config.GROQ_API_KEY
    
    # Build conversation messages
    messages = [
        {
            "role": "system",
            "content": f"You are a helpful librarian and learning assistant for a {age}-year-old. Help them find books and provide reading recommendations. Be friendly, encouraging, and age-appropriate."
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
        logger.info("No valid Groq API key, using fallback recommendations")
        return recommend(age, user_message)
    
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
    
    # Fallback to database recommendations
    return recommend(age, user_message)

