"""
Seed Computer Science Fundamentals course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_computer_science():
    """Seed Computer Science Fundamentals lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "What Is Computer Science?",
            "description": "Understand the fundamentals of computer science and its real-world applications.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=QvyTEx1wyOY",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 18,
            "information": "Learn what computer science is, how it differs from computer usage, and explore CS careers.",
            "steps": ["Understand what computer science is", "Learn difference between computer science and computer usage", "Identify real-life applications of CS", "Learn how CS solves problems", "Explore careers in CS"],
            "quiz": [
                {"question": "What is computer science?", "answer": "Study of computation and problem-solving"},
                {"question": "Is CS only about coding?", "answer": "No"},
                {"question": "One real-world use of CS?", "answer": "Banking / healthcare / AI"},
                {"question": "CS focuses on solving what?", "answer": "Problems"}
            ]
        },
        {
            "title": "History of Computers (Generations)",
            "description": "Explore the evolution of computers through different generations and technological advances.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=O5nskjZ_GoI",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "Learn about early computers, computer generations, and how technology has evolved.",
            "steps": ["Learn about early computers", "Understand computer generations", "Learn input/output evolution", "Compare old vs modern computers", "Understand importance of innovation"],
            "quiz": [
                {"question": "First generation computers used?", "answer": "Vacuum tubes"},
                {"question": "Example of early computer?", "answer": "ENIAC"},
                {"question": "Modern computers use?", "answer": "Microprocessors"},
                {"question": "Generations are based on?", "answer": "Technology used"}
            ]
        },
        {
            "title": "Hardware vs Software",
            "description": "Understand the difference between hardware and software and how they work together.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=AkFi90lZmXA",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 17,
            "information": "Learn hardware components, system vs application software, and why both are essential.",
            "steps": ["Understand hardware components", "Understand software", "Learn system vs application software", "Identify real examples", "Learn why both are needed"],
            "quiz": [
                {"question": "Keyboard is hardware or software?", "answer": "Hardware"},
                {"question": "Windows is?", "answer": "System software"},
                {"question": "MS Word is?", "answer": "Application software"},
                {"question": "Hardware without software is?", "answer": "Useless"}
            ]
        },
        {
            "title": "Input, Process, Output (IPO Cycle)",
            "description": "Learn the fundamental IPO cycle that explains how computers work.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=8IlDmi4QZbA",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 16,
            "information": "Understand the Input-Process-Output cycle and apply it to real-world scenarios.",
            "steps": ["Learn IPO cycle", "Identify inputs", "Understand processing", "Understand outputs", "Apply IPO to real life"],
            "quiz": [
                {"question": "IPO stands for?", "answer": "Input Process Output"},
                {"question": "Example of input?", "answer": "Keyboard"},
                {"question": "CPU does?", "answer": "Processing"},
                {"question": "Output example?", "answer": "Monitor"}
            ]
        },
        {
            "title": "Data, Information & Binary System",
            "description": "Understand how computers store and process data using the binary system.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=9JvK9m8Z1Yg",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 19,
            "information": "Learn bits and bytes, binary system, and why computers use binary.",
            "steps": ["Understand data vs information", "Learn what binary is", "Understand bits and bytes", "Learn why computers use binary", "Convert small numbers to binary"],
            "quiz": [
                {"question": "Smallest data unit?", "answer": "Bit"},
                {"question": "Binary uses how many digits?", "answer": "Two"},
                {"question": "Binary digits are?", "answer": "0 and 1"},
                {"question": "1 byte equals?", "answer": "8 bits"}
            ]
        },
        {
            "title": "Operating Systems (Basics)",
            "description": "Learn what operating systems are and how they manage computer resources.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=26QPDBe-NB8",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 21,
            "information": "Understand operating systems, their functions, types, and real-world examples.",
            "steps": ["Learn what OS is", "Functions of OS", "Types of OS", "Examples of OS", "Role of OS in computer"],
            "quiz": [
                {"question": "OS stands for?", "answer": "Operating System"},
                {"question": "Example of OS?", "answer": "Windows"},
                {"question": "OS manages?", "answer": "Hardware & software"},
                {"question": "Mobile OS example?", "answer": "Android"}
            ]
        },
        {
            "title": "Computer Networks & Internet (Basics)",
            "description": "Introduction to computer networks and the internet.",
            "subject": "Computer Science",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=3QhU9jd03a0",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Learn about networks, LAN, WAN, internet basics, and IP addresses.",
            "steps": ["Understand networks", "Types of networks", "Learn internet basics", "Understand browser vs internet", "Learn IP address concept"],
            "quiz": [
                {"question": "Network means?", "answer": "Connected computers"},
                {"question": "LAN stands for?", "answer": "Local Area Network"},
                {"question": "Internet is?", "answer": "Network of networks"},
                {"question": "Browser example?", "answer": "Chrome"}
            ]
        },
        {
            "title": "Algorithms & Flowcharts (Light Intro)",
            "description": "Introduction to algorithms and flowcharts for problem solving.",
            "subject": "Computer Science",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=7dFQb6U2Fks",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 23,
            "information": "Learn algorithm basics, flowchart symbols, and how to visualize problem solving.",
            "steps": ["Understand algorithms", "Learn step-by-step logic", "Understand flowcharts", "Learn flowchart symbols", "Create simple algorithm"],
            "quiz": [
                {"question": "Algorithm is?", "answer": "Step-by-step solution"},
                {"question": "Flowchart is?", "answer": "Diagram of logic"},
                {"question": "Diamond symbol means?", "answer": "Decision"},
                {"question": "Algorithm must be?", "answer": "Clear & finite"}
            ]
        },
        {
            "title": "Programming Languages (Overview)",
            "description": "Overview of different programming languages and their characteristics.",
            "subject": "Computer Science",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=Z2lT3lPCm1I",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Learn about high vs low-level languages, compilers, interpreters, and language examples.",
            "steps": ["Learn what programming language is", "Types of languages", "High vs low level", "Compiler vs interpreter", "Examples of languages"],
            "quiz": [
                {"question": "Python is?", "answer": "High-level language"},
                {"question": "Low-level language?", "answer": "Assembly"},
                {"question": "Compiler does?", "answer": "Converts whole code"},
                {"question": "Interpreter does?", "answer": "Converts line by line"}
            ]
        },
        {
            "title": "Problem Solving & Computational Thinking",
            "description": "Learn computational thinking strategies for solving problems effectively.",
            "subject": "Computer Science",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=QvyTEx1wyOY",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 25,
            "information": "Master decomposition, pattern recognition, abstraction, and logical thinking.",
            "steps": ["Learn problem solving steps", "Understand decomposition", "Learn pattern recognition", "Learn abstraction", "Apply logic to daily life"],
            "quiz": [
                {"question": "First step in problem solving?", "answer": "Understand problem"},
                {"question": "Breaking problem means?", "answer": "Decomposition"},
                {"question": "Ignoring details means?", "answer": "Abstraction"},
                {"question": "CS thinking is useful in?", "answer": "Daily life"}
            ]
        },
        {
            "title": "Cyber Safety & Digital Ethics",
            "description": "Learn about online safety, digital footprints, and ethical internet usage.",
            "subject": "Computer Science",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=V6G5f3XzJkA",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "Understand password security, digital ethics, and responsible internet behavior.",
            "steps": ["Learn online safety", "Understand strong passwords", "Learn digital footprint", "Learn cyber ethics", "Responsible internet usage"],
            "quiz": [
                {"question": "Strong password includes?", "answer": "Letters, numbers, symbols"},
                {"question": "Sharing OTP is?", "answer": "Unsafe"},
                {"question": "Digital footprint is?", "answer": "Online activity record"},
                {"question": "Cyber ethics means?", "answer": "Responsible behavior online"}
            ]
        },
        {
            "title": "Introduction to Databases & Files (Light)",
            "description": "Introduction to how data is stored in files and databases.",
            "subject": "Computer Science",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
            "min_age": 12,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Learn the difference between files and databases, and their real-world applications.",
            "steps": ["Understand files", "Learn databases", "Difference between files & DB", "Examples of databases", "Real-life usage"],
            "quiz": [
                {"question": "File stores?", "answer": "Data"},
                {"question": "Database stores?", "answer": "Structured data"},
                {"question": "DB advantage?", "answer": "Fast access"},
                {"question": "Example DB?", "answer": "MySQL"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if Computer Science lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "Computer Science",
                Lesson.title == "What Is Computer Science?"
            ).first()
            
            if existing:
                print("Computer Science lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} Computer Science lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_computer_science()
