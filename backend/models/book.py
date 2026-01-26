from extensions import db
from datetime import datetime


class Book(db.Model):
    """Book model with age-appropriate content filtering"""
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    author = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    min_age = db.Column(db.Integer, default=5)
    max_age = db.Column(db.Integer, default=18)
    category = db.Column(db.String(100), default="General")
    cover_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Book title='{self.title}' author='{self.author}' age_range={self.min_age}-{self.max_age}>"
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "category": self.category,
            "min_age": self.min_age,
            "max_age": self.max_age,
            "cover_url": self.cover_url
        }
