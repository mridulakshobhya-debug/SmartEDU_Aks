from extensions import db
from datetime import datetime


class Lesson(db.Model):
    """Lesson model for eLearning content"""
    __tablename__ = "lessons"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    information = db.Column(db.Text)  # Key learning points
    video_url = db.Column(db.String(500))  # Video placeholder URL
    steps = db.Column(db.JSON)  # List of learning steps
    quiz = db.Column(db.JSON)  # Quiz questions with answers
    difficulty = db.Column(db.String(50), default="intermediate")  # beginner, intermediate, advanced
    subject = db.Column(db.String(100), default="General")
    min_age = db.Column(db.Integer, default=5)
    max_age = db.Column(db.Integer, default=18)
    duration_minutes = db.Column(db.Integer, default=30)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Lesson title='{self.title}' difficulty='{self.difficulty}' age_range={self.min_age}-{self.max_age}>"
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "content": self.content,
            "information": self.information,
            "video_url": self.video_url,
            "steps": self.steps or [],
            "quiz": self.quiz or [],
            "difficulty": self.difficulty,
            "subject": self.subject,
            "min_age": self.min_age,
            "max_age": self.max_age,
            "duration_minutes": self.duration_minutes
        }
