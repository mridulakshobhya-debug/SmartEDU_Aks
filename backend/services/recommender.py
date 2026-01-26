import os
import sys
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book

logger = logging.getLogger(__name__)


def recommend(age, interest):
    """
    Get book recommendations from database based on age and interest
    Fallback when API is not available
    """
    try:
        books = Book.query.all()
        
        # Filter by age
        age_filtered = [b for b in books if b.min_age <= age <= b.max_age]
        
        # Filter by interest (simple keyword matching)
        interest_lower = interest.lower()
        interest_filtered = [
            b for b in age_filtered
            if interest_lower in (b.category or "").lower() or
               interest_lower in (b.title or "").lower() or
               interest_lower in (b.description or "").lower()
        ]
        
        # If no exact match, return all age-appropriate books
        recommendations = interest_filtered if interest_filtered else age_filtered
        
        # Format response
        if not recommendations:
            return f"No books found for {age}-year-olds interested in {interest}. Try searching for a different interest!"
        
        result = f"📚 Recommended books for {age}-year-olds interested in {interest}:\n\n"
        
        for i, book in enumerate(recommendations[:5], 1):
            result += f"{i}. **{book.title}** by {book.author}\n"
            if book.description:
                result += f"   {book.description}\n"
            result += f"   Age range: {book.min_age}-{book.max_age}\n\n"
        
        return result
        
    except Exception as e:
        logger.error(f"Error in recommend: {str(e)}")
        return f"Unable to fetch recommendations. Please try again later."
