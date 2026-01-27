"""
Seed JavaScript course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_javascript():
    """Seed JavaScript lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "What is JavaScript?",
            "description": "Introduction to JavaScript and its role in web development.",
            "subject": "JavaScript",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 18,
            "information": "Learn what JavaScript is, where it runs, and how it adds interactivity to web pages.",
            "steps": ["Understand what JavaScript is", "Learn where JavaScript runs", "Difference between HTML, CSS, JS", "How JS adds interactivity", "Setup environment (browser & VS Code)"],
            "quiz": [
                {"question": "JavaScript is?", "answer": "Programming language"},
                {"question": "JS runs in?", "answer": "Browser"},
                {"question": "JS used for?", "answer": "Interactivity"},
                {"question": "JS file extension?", "answer": ".js"}
            ]
        },
        {
            "title": "Variables & Data Types",
            "description": "Master variables, data types, and scope in JavaScript.",
            "subject": "JavaScript",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=9WIJQDvt4Us",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Learn var, let, const keywords, scope, and different data types in JavaScript.",
            "steps": ["Learn var, let, const", "Understand scope", "Learn data types", "Use typeof", "Write simple programs"],
            "quiz": [
                {"question": "Keyword for constant?", "answer": "const"},
                {"question": "Type of \"hello\"?", "answer": "string"},
                {"question": "typeof 10?", "answer": "number"},
                {"question": "let scope is?", "answer": "Block scope"}
            ]
        },
        {
            "title": "Operators & Expressions",
            "description": "Learn all types of operators and how to write expressions in JavaScript.",
            "subject": "JavaScript",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=JcW5YfFp6rA",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "Understand arithmetic, comparison, logical, and assignment operators with precedence.",
            "steps": ["Arithmetic operators", "Comparison operators", "Logical operators", "Assignment operators", "Operator precedence"],
            "quiz": [
                {"question": "== vs ===?", "answer": "Loose vs strict equality"},
                {"question": "AND operator?", "answer": "&&"},
                {"question": "Output of 5 + \"5\"?", "answer": "\"55\""},
                {"question": "Greater-than operator?", "answer": ">"}
            ]
        },
        {
            "title": "Control Flow (Conditions)",
            "description": "Learn conditional statements to make decisions in code.",
            "subject": "JavaScript",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=IsG4Xd6LlsM",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 21,
            "information": "Master if, else, else if, switch statements, and ternary operators.",
            "steps": ["if, else, else if", "Comparison logic", "Switch statement", "Ternary operator", "Decision making programs"],
            "quiz": [
                {"question": "if used for?", "answer": "Decision making"},
                {"question": "Switch is alternative to?", "answer": "if-else"},
                {"question": "Ternary operator symbol?", "answer": "? :"},
                {"question": "Condition must return?", "answer": "Boolean"}
            ]
        },
        {
            "title": "Loops & Iteration",
            "description": "Master loops to repeat code blocks efficiently.",
            "subject": "JavaScript",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=s9wW2PpJsmQ",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 23,
            "information": "Learn for, while, do...while loops, loop control, and array iteration.",
            "steps": ["for loop", "while loop", "do...while", "Loop control (break, continue)", "Iterating arrays"],
            "quiz": [
                {"question": "Loop for known count?", "answer": "for"},
                {"question": "Loop that runs at least once?", "answer": "do-while"},
                {"question": "break does?", "answer": "Exits loop"},
                {"question": "Loop through array?", "answer": "for / forEach"}
            ]
        },
        {
            "title": "Functions (Beginner → Intermediate)",
            "description": "Learn to write and use functions for code reusability.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=R8rmfD9Y5-c",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 25,
            "information": "Master function declaration, parameters, return values, and arrow functions.",
            "steps": ["Function declaration", "Parameters & arguments", "Return values", "Arrow functions", "Function reuse"],
            "quiz": [
                {"question": "Function keyword?", "answer": "function"},
                {"question": "Arrow function symbol?", "answer": "=>"},
                {"question": "Return does?", "answer": "Sends value back"},
                {"question": "Function without return returns?", "answer": "undefined"}
            ]
        },
        {
            "title": "Arrays (Deep Basics)",
            "description": "Master arrays and array methods in JavaScript.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=R8rmfD9Y5-c",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Learn array creation, access, methods, iteration, and modification.",
            "steps": ["Create arrays", "Access elements", "Array methods", "Loop arrays", "Modify arrays"],
            "quiz": [
                {"question": "Array index starts at?", "answer": "0"},
                {"question": "Method to add end?", "answer": "push()"},
                {"question": "Remove last element?", "answer": "pop()"},
                {"question": "Length property?", "answer": "length"}
            ]
        },
        {
            "title": "Objects (Core Concept)",
            "description": "Understand objects and key-value pair data structures.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=0W6q4p8h2Dg",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Learn object creation, properties, methods, and iteration.",
            "steps": ["Understand objects", "Key-value pairs", "Access properties", "Add methods", "Object iteration"],
            "quiz": [
                {"question": "Object stores data as?", "answer": "Key-value pairs"},
                {"question": "Access using dot?", "answer": "Yes"},
                {"question": "Method is?", "answer": "Function inside object"},
                {"question": "Object loop?", "answer": "for...in"}
            ]
        },
        {
            "title": "DOM Manipulation",
            "description": "Learn to interact with and modify the HTML DOM.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=0ik6X4DJKCc",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Master DOM selection, content modification, and event handling.",
            "steps": ["What is DOM?", "Select elements", "Change content", "Handle events", "Build interactions"],
            "quiz": [
                {"question": "DOM stands for?", "answer": "Document Object Model"},
                {"question": "Select by ID?", "answer": "getElementById"},
                {"question": "Change text?", "answer": "innerText"},
                {"question": "Click event?", "answer": "click"}
            ]
        },
        {
            "title": "Events & Event Handling",
            "description": "Understand events and how to handle them in web applications.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=XF1_MlZ5l6Q",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 23,
            "information": "Learn event types, addEventListener, event objects, bubbling, and preventing defaults.",
            "steps": ["Event types", "addEventListener", "Event object", "Event bubbling", "Prevent default actions"],
            "quiz": [
                {"question": "addEventListener does?", "answer": "Attaches event"},
                {"question": "Event object holds?", "answer": "Event info"},
                {"question": "Bubbling means?", "answer": "Event moves upward"},
                {"question": "Prevent default method?", "answer": "preventDefault()"}
            ]
        },
        {
            "title": "Asynchronous JavaScript (Intro)",
            "description": "Introduction to asynchronous programming with callbacks, promises, and async/await.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=PoRJizFvM7s",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Understand async behavior, callbacks, promises, async/await, and error handling.",
            "steps": ["Understand async behavior", "Callbacks", "Promises", "async/await", "Error handling"],
            "quiz": [
                {"question": "JS is?", "answer": "Non-blocking"},
                {"question": "Promise states?", "answer": "Pending, fulfilled, rejected"},
                {"question": "async function returns?", "answer": "Promise"},
                {"question": "await waits for?", "answer": "Promise resolution"}
            ]
        },
        {
            "title": "Fetch API & APIs (Beginner Level)",
            "description": "Learn to fetch data from APIs and work with JSON.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=cuEtnrL9-H0",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 25,
            "information": "Understand APIs, Fetch API, JSON data format, and displaying API data.",
            "steps": ["Understand APIs", "Fetch data", "Handle JSON", "Display API data", "Handle errors"],
            "quiz": [
                {"question": "API stands for?", "answer": "Application Programming Interface"},
                {"question": "Fetch returns?", "answer": "Promise"},
                {"question": "JSON is?", "answer": "Data format"},
                {"question": "Method to convert JSON?", "answer": ".json()"}
            ]
        },
        {
            "title": "ES6+ Features (Intermediate)",
            "description": "Learn modern JavaScript ES6+ features for cleaner code.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=NCwa_xi0Uuc",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Master destructuring, spread operator, template literals, and modules.",
            "steps": ["Destructuring", "Spread operator", "Template literals", "Modules", "Clean code"],
            "quiz": [
                {"question": "Template literals use?", "answer": "Backticks `"},
                {"question": "Spread operator symbol?", "answer": "..."},
                {"question": "Destructuring extracts?", "answer": "Values"},
                {"question": "Import syntax?", "answer": "import"}
            ]
        },
        {
            "title": "Error Handling & Debugging",
            "description": "Learn to handle errors and debug JavaScript code effectively.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=NIWwJbo-9_8",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "Master try-catch blocks, browser debugging tools, console methods, and safe coding.",
            "steps": ["Common JS errors", "try-catch", "Debug using browser tools", "Console methods", "Write safe code"],
            "quiz": [
                {"question": "try block does?", "answer": "Runs risky code"},
                {"question": "catch block does?", "answer": "Handles errors"},
                {"question": "Console for error?", "answer": "console.error()"},
                {"question": "Debugger keyword?", "answer": "debugger"}
            ]
        },
        {
            "title": "Mini Projects (Beginner → Intermediate)",
            "description": "Build real projects to apply JavaScript skills.",
            "subject": "JavaScript",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Build calculator, to-do list, counter app, and API-based projects.",
            "steps": ["Build calculator", "Build to-do list", "Build counter app", "Use API project", "Improve UI"],
            "quiz": [
                {"question": "Project improves?", "answer": "Skills"},
                {"question": "DOM used for?", "answer": "Interactivity"},
                {"question": "API project uses?", "answer": "External data"},
                {"question": "Practice leads to?", "answer": "Mastery"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if JavaScript lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "JavaScript"
            ).first()
            
            if existing:
                print("JavaScript lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} JavaScript lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_javascript()
