"""
Seed Artificial Intelligence course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_artificial_intelligence():
    """Seed Artificial Intelligence lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "What is Artificial Intelligence?",
            "description": "Understand the fundamentals of Artificial Intelligence and its real-world applications.",
            "subject": "Artificial Intelligence",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=ad79nYk2keg",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "Learn what AI is, how it differs from ML and DL, and explore real-world AI examples.",
            "steps": ["Understand what AI is", "Learn difference between AI, ML, and DL", "Identify real-world AI examples", "Learn how AI works at high level", "Understand why AI is important"],
            "quiz": [
                {"question": "AI stands for?", "answer": "Artificial Intelligence"},
                {"question": "AI vs human intelligence?", "answer": "Machines mimicking intelligence"},
                {"question": "Example of AI?", "answer": "Voice assistants"},
                {"question": "AI mainly works on?", "answer": "Data"}
            ]
        },
        {
            "title": "History & Types of AI",
            "description": "Explore the evolution of AI and understand narrow, general, and super AI concepts.",
            "subject": "Artificial Intelligence",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=JMUxmLyrhSk",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Learn the history of AI, understand different types, and explore current AI categories.",
            "steps": ["Learn evolution of AI", "Understand narrow AI", "Learn general AI", "Learn super AI (concept)", "Identify AI categories"],
            "quiz": [
                {"question": "Narrow AI means?", "answer": "Task-specific AI"},
                {"question": "Example of narrow AI?", "answer": "Chatbots"},
                {"question": "Does general AI exist?", "answer": "No"},
                {"question": "Super AI is?", "answer": "Hypothetical future AI"}
            ]
        },
        {
            "title": "How AI Systems Work (Basic Flow)",
            "description": "Understand the basic workflow of AI systems from input to output.",
            "subject": "Artificial Intelligence",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=8IlDmi4QZbA",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 18,
            "information": "Learn the input-process-output flow, data role, training vs prediction, and feedback loops.",
            "steps": ["Learn input → process → output", "Understand role of data", "Learn training vs prediction", "Understand feedback loop", "Simple AI workflow"],
            "quiz": [
                {"question": "AI input is?", "answer": "Data"},
                {"question": "Training means?", "answer": "Teaching model"},
                {"question": "Output is?", "answer": "Prediction/result"},
                {"question": "Feedback improves?", "answer": "Accuracy"}
            ]
        },
        {
            "title": "Data Basics for AI",
            "description": "Learn the importance of data and data quality in AI systems.",
            "subject": "Artificial Intelligence",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=ua-CiDNNj30",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 19,
            "information": "Understand data types, structured vs unstructured data, and data quality importance.",
            "steps": ["Learn what data is", "Types of data", "Structured vs unstructured data", "Data quality importance", "Data collection basics"],
            "quiz": [
                {"question": "Data is?", "answer": "Information"},
                {"question": "Example of unstructured data?", "answer": "Images/videos"},
                {"question": "Structured data stored in?", "answer": "Tables"},
                {"question": "Bad data causes?", "answer": "Poor AI results"}
            ]
        },
        {
            "title": "Introduction to Machine Learning",
            "description": "Learn the fundamentals of Machine Learning and how it relates to AI.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=ukzFI9rgwfU",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Understand ML concept, ML vs AI, types of ML, and the model idea.",
            "steps": ["Understand ML concept", "ML vs AI", "Types of ML", "Learn examples", "Understand model idea"],
            "quiz": [
                {"question": "ML stands for?", "answer": "Machine Learning"},
                {"question": "ML learns from?", "answer": "Data"},
                {"question": "ML is subset of?", "answer": "AI"},
                {"question": "Example of ML?", "answer": "Recommendation system"}
            ]
        },
        {
            "title": "Types of Machine Learning",
            "description": "Explore supervised, unsupervised, and reinforcement learning approaches.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Learn supervised learning, unsupervised learning, reinforcement learning, and real-life examples.",
            "steps": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Compare learning types", "Real-life examples"],
            "quiz": [
                {"question": "Supervised uses?", "answer": "Labeled data"},
                {"question": "Unsupervised finds?", "answer": "Patterns"},
                {"question": "Reinforcement uses?", "answer": "Rewards"},
                {"question": "Example of supervised ML?", "answer": "Spam detection"}
            ]
        },
        {
            "title": "AI Tools & Platforms (Beginner Friendly)",
            "description": "Explore beginner-friendly AI tools and no-code platforms.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=Zp8kH8P9n2U",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 21,
            "information": "Learn about no-code AI tools, low-code platforms, and cloud AI services.",
            "steps": ["Learn AI tools overview", "No-code AI tools", "Low-code platforms", "Cloud AI services", "When to use tools"],
            "quiz": [
                {"question": "No-code means?", "answer": "No programming"},
                {"question": "Example AI tool?", "answer": "Teachable Machine"},
                {"question": "Cloud AI example?", "answer": "Google AI"},
                {"question": "Tools help to?", "answer": "Build faster"}
            ]
        },
        {
            "title": "Neural Networks (Very Basic)",
            "description": "Introduction to neural networks and how they mimic the brain.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=aircAruvnKk",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 25,
            "information": "Learn neurons, layers, weights, and basic neural network training concepts.",
            "steps": ["Understand neurons", "Input, hidden, output layers", "Learn weights concept", "Understand training idea", "Real-life analogy"],
            "quiz": [
                {"question": "Neural network inspired by?", "answer": "Human brain"},
                {"question": "Layer types?", "answer": "Input, hidden, output"},
                {"question": "Weights mean?", "answer": "Importance values"},
                {"question": "NN output is?", "answer": "Prediction"}
            ]
        },
        {
            "title": "Natural Language Processing (Intro)",
            "description": "Introduction to Natural Language Processing and text understanding.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=CMrHM8a3hqw",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 23,
            "information": "Learn NLP basics, text processing, tokenization, and real-world NLP applications.",
            "steps": ["Learn NLP basics", "Text processing idea", "Tokenization", "Real-life NLP apps", "Challenges in NLP"],
            "quiz": [
                {"question": "NLP stands for?", "answer": "Natural Language Processing"},
                {"question": "NLP deals with?", "answer": "Text & language"},
                {"question": "Tokenization means?", "answer": "Splitting text"},
                {"question": "NLP example?", "answer": "Chatbots"}
            ]
        },
        {
            "title": "Computer Vision (Intro)",
            "description": "Introduction to Computer Vision and image analysis with AI.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=OcycT1Jwsns",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Learn Computer Vision basics, image data, object detection, and real-world use cases.",
            "steps": ["Learn what CV is", "Image data basics", "Object detection idea", "Face recognition", "Real-life use cases"],
            "quiz": [
                {"question": "CV stands for?", "answer": "Computer Vision"},
                {"question": "CV deals with?", "answer": "Images & videos"},
                {"question": "Face recognition uses?", "answer": "AI models"},
                {"question": "CV example?", "answer": "Self-driving cars"}
            ]
        },
        {
            "title": "AI Ethics & Responsible AI",
            "description": "Understand ethics, bias, privacy, and responsible AI development.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=V6G5f3XzJkA",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Learn AI ethics, bias in AI, privacy concerns, and responsible AI practices.",
            "steps": ["Learn AI ethics", "Bias in AI", "Privacy concerns", "Responsible AI usage", "Future challenges"],
            "quiz": [
                {"question": "AI bias means?", "answer": "Unfair outcomes"},
                {"question": "Data privacy is?", "answer": "Protecting personal data"},
                {"question": "Responsible AI means?", "answer": "Safe and fair AI"},
                {"question": "Ethics important because?", "answer": "Human impact"}
            ]
        },
        {
            "title": "Building Your First AI Project (Beginner Level)",
            "description": "Learn how to build a simple AI project from start to finish.",
            "subject": "Artificial Intelligence",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=Zp8kH8P9n2U",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 27,
            "information": "Build your first AI project using no-code tools, train models, and test results.",
            "steps": ["Choose simple AI problem", "Collect small dataset", "Use no-code tool", "Train model", "Test and improve"],
            "quiz": [
                {"question": "First step in AI project?", "answer": "Define problem"},
                {"question": "Tool for beginners?", "answer": "Teachable Machine"},
                {"question": "Training means?", "answer": "Learning patterns"},
                {"question": "Testing checks?", "answer": "Accuracy"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if AI lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "Artificial Intelligence"
            ).first()
            
            if existing:
                print("Artificial Intelligence lessons already exist in database. Skipping seeding.")
                return
            
            # Add all lessons
            for lesson_data in lessons_data:
                lesson = Lesson(
                    title=lesson_data["title"],
                    description=lesson_data["description"],
                    subject=lesson_data["subject"],
                    difficulty=lesson_data["difficulty"],
                    video_url=lesson_data["video_url"],
                    min_age=lesson_data["min_age"],
                    max_age=lesson_data["max_age"],
                    duration_minutes=lesson_data["duration_minutes"],
                    information=lesson_data["information"],
                    steps=lesson_data["steps"],
                    quiz=lesson_data["quiz"]
                )
                db.session.add(lesson)
            
            db.session.commit()
            print(f"✅ Successfully added {len(lessons_data)} Artificial Intelligence lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_artificial_intelligence()
