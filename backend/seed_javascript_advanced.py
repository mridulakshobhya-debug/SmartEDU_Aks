"""
Seed Advanced JavaScript course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_advanced_javascript():
    """Seed Advanced JavaScript lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "JavaScript Engine & Execution Context",
            "description": "Understand how JavaScript engines work and execute code internally.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=8aGhZQkoFbQ",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Learn about call stack, memory heap, execution context, and hoisting mechanisms.",
            "steps": ["Understand how JS engine works", "Call stack and memory heap", "Execution context", "Hoisting", "How JS runs code internally"],
            "quiz": [
                {"question": "JS engine example?", "answer": "V8"},
                {"question": "Call stack stores?", "answer": "Function calls"},
                {"question": "Hoisting means?", "answer": "Moving declarations to top"},
                {"question": "Execution context has?", "answer": "Variables, scope, this"}
            ]
        },
        {
            "title": "Scope, Closures & Lexical Environment",
            "description": "Master closures and lexical scoping in JavaScript.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=qikxEIxsXco",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 29,
            "information": "Understand global vs local scope, closures, and memory implications.",
            "steps": ["Global vs local scope", "Lexical scoping", "Understand closures", "Practical closure examples", "Memory implications"],
            "quiz": [
                {"question": "Closure is?", "answer": "Function with preserved scope"},
                {"question": "Lexical scope means?", "answer": "Scope defined by position"},
                {"question": "Closure remembers?", "answer": "Outer variables"},
                {"question": "Common use of closure?", "answer": "Data privacy"}
            ]
        },
        {
            "title": "this Keyword & Binding Rules",
            "description": "Master the 'this' keyword and function binding in JavaScript.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=gvicrj31JOM",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 27,
            "information": "Learn this binding in different contexts, call, apply, bind methods, and arrow functions.",
            "steps": ["this in global scope", "this in functions", "this in methods", "call, apply, bind", "Arrow function behavior"],
            "quiz": [
                {"question": "this refers to?", "answer": "Context object"},
                {"question": "call() does?", "answer": "Calls function with this"},
                {"question": "bind() returns?", "answer": "New function"},
                {"question": "Arrow function this?", "answer": "Lexical this"}
            ]
        },
        {
            "title": "Prototypes & Inheritance",
            "description": "Understand prototype-based inheritance and ES6 classes.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=wstwjQ1yqWQ",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 33,
            "information": "Learn prototype chain, constructor functions, ES6 classes, and method overriding.",
            "steps": ["Prototype chain", "Object inheritance", "Constructor functions", "ES6 classes vs prototypes", "Method overriding"],
            "quiz": [
                {"question": "Prototype is?", "answer": "Shared object"},
                {"question": "Inheritance allows?", "answer": "Code reuse"},
                {"question": "proto links?", "answer": "Objects"},
                {"question": "Class syntax is?", "answer": "Syntactic sugar"}
            ]
        },
        {
            "title": "Advanced Functions & Functional Programming",
            "description": "Master functional programming concepts and higher-order functions.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=BMUiFMZr7vk",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Learn first-class functions, higher-order functions, pure functions, and function composition.",
            "steps": ["First-class functions", "Higher-order functions", "Pure functions", "Immutability", "Function composition"],
            "quiz": [
                {"question": "Higher-order function?", "answer": "Function taking function"},
                {"question": "Pure function?", "answer": "No side effects"},
                {"question": "Immutability means?", "answer": "Cannot change"},
                {"question": "map() returns?", "answer": "New array"}
            ]
        },
        {
            "title": "Asynchronous JavaScript (Deep Dive)",
            "description": "Deep understanding of event loops, promises, and async/await.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=PoRJizFvM7s",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 35,
            "information": "Master event loop, microtasks vs macrotasks, promise internals, and async/await mechanics.",
            "steps": ["Event loop", "Microtasks vs macrotasks", "Promises internals", "async/await under the hood", "Error handling strategies"],
            "quiz": [
                {"question": "Event loop does?", "answer": "Manages async tasks"},
                {"question": "Promise callback goes to?", "answer": "Microtask queue"},
                {"question": "async returns?", "answer": "Promise"},
                {"question": "await pauses?", "answer": "Function execution"}
            ]
        },
        {
            "title": "Modules & Bundlers",
            "description": "Learn ES modules, import/export, and module bundlers.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=cRHQNNcYf6s",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Understand ES modules, module scope, bundlers, and tree shaking optimization.",
            "steps": ["ES modules", "import/export syntax", "Module scope", "Bundlers purpose", "Tree shaking"],
            "quiz": [
                {"question": "Module scope means?", "answer": "File-level scope"},
                {"question": "export used for?", "answer": "Share code"},
                {"question": "Bundler example?", "answer": "Webpack"},
                {"question": "Tree shaking removes?", "answer": "Unused code"}
            ]
        },
        {
            "title": "Memory Management & Performance",
            "description": "Optimize JavaScript performance and manage memory efficiently.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=0Z0ZP6Z4JZc",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Learn memory allocation, garbage collection, memory leaks, and performance profiling.",
            "steps": ["Memory allocation", "Garbage collection", "Memory leaks", "Performance profiling", "Optimization techniques"],
            "quiz": [
                {"question": "Garbage collector frees?", "answer": "Unused memory"},
                {"question": "Memory leak is?", "answer": "Unreleased memory"},
                {"question": "Global variables cause?", "answer": "Leaks"},
                {"question": "Profiling checks?", "answer": "Performance"}
            ]
        },
        {
            "title": "Browser APIs & Web Storage",
            "description": "Master browser APIs and different web storage mechanisms.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=HfK4KzG5iD8",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Learn LocalStorage, SessionStorage, cookies, and modern web APIs.",
            "steps": ["LocalStorage", "SessionStorage", "Cookies basics", "Web APIs", "Use cases"],
            "quiz": [
                {"question": "LocalStorage persists?", "answer": "Yes"},
                {"question": "SessionStorage cleared?", "answer": "Tab close"},
                {"question": "Cookies sent with?", "answer": "Requests"},
                {"question": "Web API example?", "answer": "Geolocation"}
            ]
        },
        {
            "title": "Security in JavaScript",
            "description": "Understand JavaScript security threats and protection strategies.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=FJxW2a0XK_g",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Learn about XSS, CSRF, secure coding practices, and Content Security Policy.",
            "steps": ["XSS attacks", "CSRF basics", "Secure coding", "Input validation", "Content Security Policy"],
            "quiz": [
                {"question": "XSS means?", "answer": "Cross-site scripting"},
                {"question": "CSRF means?", "answer": "Cross-site request forgery"},
                {"question": "Input validation prevents?", "answer": "Attacks"},
                {"question": "CSP controls?", "answer": "Resource loading"}
            ]
        },
        {
            "title": "Design Patterns in JavaScript",
            "description": "Learn common design patterns for better code organization.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=tv-_1er1mWI",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Master module, factory, singleton, and observer design patterns.",
            "steps": ["Module pattern", "Factory pattern", "Singleton pattern", "Observer pattern", "When to use patterns"],
            "quiz": [
                {"question": "Singleton allows?", "answer": "One instance"},
                {"question": "Factory creates?", "answer": "Objects"},
                {"question": "Observer used for?", "answer": "Event handling"},
                {"question": "Pattern benefit?", "answer": "Maintainability"}
            ]
        },
        {
            "title": "Testing & Debugging (Advanced)",
            "description": "Master testing frameworks and advanced debugging techniques.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=7r4xVDI2vHo",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 29,
            "information": "Learn unit testing, test frameworks like Jest, TDD, and async debugging.",
            "steps": ["Unit testing", "Test frameworks", "Writing test cases", "Debugging async code", "Test-driven mindset"],
            "quiz": [
                {"question": "Unit test tests?", "answer": "Small code units"},
                {"question": "JS test framework?", "answer": "Jest"},
                {"question": "TDD means?", "answer": "Test-driven development"},
                {"question": "Debug async using?", "answer": "Breakpoints"}
            ]
        },
        {
            "title": "Build Advanced Projects",
            "description": "Create complex JavaScript applications and optimize for production.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 34,
            "information": "Build games, SPAs, API projects, and optimize for production deployment.",
            "steps": ["Build JS game", "Create SPA without framework", "API-heavy project", "Performance optimization", "Production readiness"],
            "quiz": [
                {"question": "Advanced project shows?", "answer": "Mastery"},
                {"question": "SPA means?", "answer": "Single Page Application"},
                {"question": "API project needs?", "answer": "Async handling"},
                {"question": "Optimization improves?", "answer": "Speed"}
            ]
        },
        {
            "title": "JavaScript Career & Next Steps",
            "description": "Plan your JavaScript career and prepare for professional development.",
            "subject": "JavaScript",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=QvyTEx1wyOY",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Explore career paths, frameworks, portfolio building, and interview preparation.",
            "steps": ["JS career paths", "Frontend vs backend", "Learn frameworks", "Build portfolio", "Interview preparation"],
            "quiz": [
                {"question": "JS framework example?", "answer": "React"},
                {"question": "Backend JS uses?", "answer": "Node.js"},
                {"question": "Portfolio shows?", "answer": "Skills"},
                {"question": "Next after JS?", "answer": "Frameworks / backend"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if advanced JavaScript lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "JavaScript",
                Lesson.difficulty == "Advanced"
            ).first()
            
            if existing:
                print("Advanced JavaScript lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} Advanced JavaScript lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_advanced_javascript()
