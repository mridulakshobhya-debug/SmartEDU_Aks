"""
Seed Advanced Computer Science course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_advanced_computer_science():
    """Seed Advanced Computer Science lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "Advanced Problem Solving & Computational Thinking",
            "description": "Master advanced problem-solving strategies and computational thinking techniques.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=Oqj5Z3Fj0G8",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Learn decomposition, abstraction, pattern recognition, and optimization in complex problems.",
            "steps": ["Revisit problem-solving strategies", "Learn decomposition deeply", "Apply abstraction in complex problems", "Use pattern recognition", "Optimize solutions"],
            "quiz": [
                {"question": "What is abstraction?", "answer": "Removing unnecessary details"},
                {"question": "Decomposition means?", "answer": "Breaking problems into parts"},
                {"question": "Pattern recognition helps in?", "answer": "Finding similarities"},
                {"question": "Optimization means?", "answer": "Making solution efficient"}
            ]
        },
        {
            "title": "Data Structures (Core Concepts)",
            "description": "Understand fundamental data structures and their applications.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=RBSGKlAvoiM",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Learn arrays, lists, stacks, queues, and linked lists with their trade-offs.",
            "steps": ["Understand why data structures matter", "Learn arrays and lists", "Understand stacks and queues", "Learn linked lists", "Compare data structures"],
            "quiz": [
                {"question": "Stack follows?", "answer": "LIFO"},
                {"question": "Queue follows?", "answer": "FIFO"},
                {"question": "Linked list advantage?", "answer": "Dynamic size"},
                {"question": "Example of linear DS?", "answer": "Array"}
            ]
        },
        {
            "title": "Algorithms (Sorting & Searching)",
            "description": "Master sorting and searching algorithms with efficiency analysis.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=kPRA0W1kECg",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Learn linear search, binary search, bubble sort, and algorithm efficiency.",
            "steps": ["Understand algorithm efficiency", "Learn linear search", "Learn binary search", "Learn bubble sort", "Compare algorithms"],
            "quiz": [
                {"question": "Binary search requires?", "answer": "Sorted list"},
                {"question": "Best case bubble sort?", "answer": "O(n)"},
                {"question": "Linear search time?", "answer": "O(n)"},
                {"question": "Sorting means?", "answer": "Arranging data"}
            ]
        },
        {
            "title": "Time & Space Complexity (Big-O)",
            "description": "Analyze algorithm complexity using Big-O notation.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=V6mKVRU1evU",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 29,
            "information": "Learn Big-O notation, common cases, and how to compare algorithms.",
            "steps": ["Learn why complexity matters", "Understand Big-O notation", "Learn common Big-O cases", "Compare algorithms", "Optimize code"],
            "quiz": [
                {"question": "O(1) means?", "answer": "Constant time"},
                {"question": "O(n) means?", "answer": "Linear time"},
                {"question": "Worst case refers to?", "answer": "Maximum operations"},
                {"question": "Why Big-O used?", "answer": "Measure efficiency"}
            ]
        },
        {
            "title": "Object-Oriented Concepts (Deep Understanding)",
            "description": "Master the four pillars of object-oriented programming.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=pTB0EiLXUC8",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Deep dive into abstraction, encapsulation, inheritance, and polymorphism.",
            "steps": ["Understand abstraction", "Learn encapsulation", "Learn inheritance", "Learn polymorphism", "Apply OOP in designs"],
            "quiz": [
                {"question": "OOP pillars?", "answer": "Abstraction, Encapsulation, Inheritance, Polymorphism"},
                {"question": "Encapsulation means?", "answer": "Data hiding"},
                {"question": "Inheritance means?", "answer": "Reusing features"},
                {"question": "Polymorphism means?", "answer": "Multiple behaviors"}
            ]
        },
        {
            "title": "Operating Systems (Advanced Concepts)",
            "description": "Explore advanced OS concepts and system management.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=26QPDBe-NB8",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 33,
            "information": "Learn process management, memory management, scheduling, and deadlocks.",
            "steps": ["Learn process management", "Understand memory management", "Learn scheduling algorithms", "Understand deadlocks", "Learn multitasking"],
            "quiz": [
                {"question": "CPU scheduling is?", "answer": "Process execution order"},
                {"question": "Deadlock means?", "answer": "Infinite waiting"},
                {"question": "RAM stores?", "answer": "Running programs"},
                {"question": "Multitasking means?", "answer": "Running multiple tasks"}
            ]
        },
        {
            "title": "Computer Networks (Advanced)",
            "description": "Deep understanding of networking protocols and architecture.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=3QhU9jd03a0",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 34,
            "information": "Learn OSI model, TCP/IP, protocols, DNS, and data transmission.",
            "steps": ["Learn OSI model", "Understand TCP/IP", "Learn protocols", "Understand DNS", "Learn data transmission"],
            "quiz": [
                {"question": "OSI has how many layers?", "answer": "7"},
                {"question": "TCP ensures?", "answer": "Reliable transmission"},
                {"question": "DNS does?", "answer": "Converts domain to IP"},
                {"question": "HTTP is?", "answer": "Web protocol"}
            ]
        },
        {
            "title": "Databases & Data Management",
            "description": "Master database design and management concepts.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Learn relational databases, keys, normalization, SQL, and NoSQL.",
            "steps": ["Learn relational databases", "Understand tables & keys", "Learn normalization", "Learn SQL basics", "Compare SQL vs NoSQL"],
            "quiz": [
                {"question": "Primary key is?", "answer": "Unique identifier"},
                {"question": "SQL stands for?", "answer": "Structured Query Language"},
                {"question": "Normalization reduces?", "answer": "Redundancy"},
                {"question": "NoSQL example?", "answer": "MongoDB"}
            ]
        },
        {
            "title": "Software Engineering & SDLC",
            "description": "Understand software development methodologies and practices.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=Fi3_BjVzpqk",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Learn SDLC phases, Agile model, Waterfall model, and best practices.",
            "steps": ["Learn software engineering", "Understand SDLC phases", "Learn Agile model", "Learn Waterfall model", "Compare methodologies"],
            "quiz": [
                {"question": "SDLC stands for?", "answer": "Software Development Life Cycle"},
                {"question": "Agile focuses on?", "answer": "Iterations"},
                {"question": "Waterfall is?", "answer": "Sequential model"},
                {"question": "Testing phase purpose?", "answer": "Find bugs"}
            ]
        },
        {
            "title": "Cybersecurity Fundamentals",
            "description": "Learn cybersecurity concepts and protection strategies.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=FJxW2a0XK_g",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Learn attacks, encryption, authentication, and ethical hacking basics.",
            "steps": ["Learn security basics", "Types of cyber attacks", "Learn encryption basics", "Learn authentication", "Learn ethical hacking basics"],
            "quiz": [
                {"question": "Malware is?", "answer": "Malicious software"},
                {"question": "Phishing means?", "answer": "Fake communication attack"},
                {"question": "Encryption does?", "answer": "Secures data"},
                {"question": "Authentication means?", "answer": "Identity verification"}
            ]
        },
        {
            "title": "Artificial Intelligence & Machine Learning (Intro)",
            "description": "Introduction to AI and machine learning concepts.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=JMUxmLyrhSk",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Learn AI, ML, real-world applications, and the importance of data.",
            "steps": ["Understand AI", "Difference between AI & ML", "Learn real-world AI apps", "Learn data importance", "Understand future scope"],
            "quiz": [
                {"question": "AI stands for?", "answer": "Artificial Intelligence"},
                {"question": "ML is?", "answer": "Learning from data"},
                {"question": "AI example?", "answer": "Voice assistants"},
                {"question": "ML needs?", "answer": "Data"}
            ]
        },
        {
            "title": "Ethics, Careers & Future of CS",
            "description": "Explore CS ethics, career paths, and future technologies.",
            "subject": "Computer Science",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=V6G5f3XzJkA",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Learn ethical practices, career opportunities, and emerging technologies.",
            "steps": ["Learn CS ethics", "Understand AI ethics", "Learn career paths", "Learn skill roadmap", "Prepare for future tech"],
            "quiz": [
                {"question": "CS ethics means?", "answer": "Responsible tech use"},
                {"question": "Data privacy is?", "answer": "Protecting personal data"},
                {"question": "CS career example?", "answer": "Software engineer"},
                {"question": "Future tech example?", "answer": "AI / Quantum computing"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if advanced CS lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "Computer Science",
                Lesson.difficulty == "Advanced"
            ).first()
            
            if existing:
                print("Advanced Computer Science lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} Advanced Computer Science lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_advanced_computer_science()
