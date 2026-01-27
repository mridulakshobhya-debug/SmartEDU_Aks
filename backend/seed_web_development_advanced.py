"""
Seed Advanced Web Development course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_advanced_web_development():
    """Seed Advanced Web Development lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "Advanced HTML & Accessibility (a11y)",
            "description": "Master semantic HTML and accessibility standards for inclusive web development.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=0hqhAIjE_8I",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Learn semantic HTML tags, ARIA roles, and keyboard navigation to create accessible websites.",
            "steps": ["Learn semantic HTML tags", "Understand accessibility (a11y)", "Use ARIA roles correctly", "Improve keyboard navigation", "Test accessibility with tools"],
            "quiz": [
                {"question": "What is semantic HTML?", "answer": "HTML with meaningful tags"},
                {"question": "What does a11y mean?", "answer": "Accessibility"},
                {"question": "Purpose of ARIA?", "answer": "Improve screen reader support"},
                {"question": "Name one semantic tag", "answer": "<header>, <nav>, <main>, <section>"}
            ]
        },
        {
            "title": "Advanced CSS (Animations & Transitions)",
            "description": "Create beautiful animations and transitions with advanced CSS techniques.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=YszONjKpgg4",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Master CSS transitions, keyframe animations, and performance optimization.",
            "steps": ["Learn CSS transitions", "Create keyframe animations", "Control animation timing", "Optimize animations for performance", "Use hover and focus effects"],
            "quiz": [
                {"question": "Property to create animation?", "answer": "animation"},
                {"question": "What is @keyframes?", "answer": "Defines animation steps"},
                {"question": "Transition vs animation?", "answer": "Animation is multi-step"},
                {"question": "Property to control duration?", "answer": "animation-duration"}
            ]
        },
        {
            "title": "CSS Architecture & Preprocessors",
            "description": "Learn CSS best practices with BEM naming and SCSS preprocessing.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=Zz6eOVaaelI",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "Understand CSS modularity, BEM conventions, and SCSS preprocessor features.",
            "steps": ["Learn BEM naming convention", "Understand CSS modularity", "Use SCSS variables", "Nest styles safely", "Compile SCSS to CSS"],
            "quiz": [
                {"question": "What is BEM?", "answer": "Block Element Modifier"},
                {"question": "SCSS is?", "answer": "CSS preprocessor"},
                {"question": "Advantage of preprocessors?", "answer": "Reusable and maintainable CSS"},
                {"question": "SCSS variable syntax?", "answer": "$color"}
            ]
        },
        {
            "title": "Advanced JavaScript (ES6+)",
            "description": "Learn modern JavaScript features and best practices.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=NCwa_xi0Uuc",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Master ES6+ features including arrow functions, destructuring, and modules.",
            "steps": ["Learn let, const", "Arrow functions", "Destructuring", "Spread and rest operators", "Modules import/export"],
            "quiz": [
                {"question": "Arrow function symbol?", "answer": "=>"},
                {"question": "const means?", "answer": "Cannot be reassigned"},
                {"question": "What is destructuring?", "answer": "Extract values from arrays/objects"},
                {"question": "Purpose of spread operator?", "answer": "Copy or merge data"}
            ]
        },
        {
            "title": "Asynchronous JavaScript (Promises & Async/Await)",
            "description": "Master async programming patterns and error handling.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=PoRJizFvM7s",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 29,
            "information": "Learn promises, async/await syntax, and proper error handling.",
            "steps": ["Understand async programming", "Learn promises", "Handle resolve and reject", "Use async/await syntax", "Handle async errors"],
            "quiz": [
                {"question": "Promise states?", "answer": "Pending, fulfilled, rejected"},
                {"question": "Async function returns?", "answer": "Promise"},
                {"question": "Keyword to wait?", "answer": "await"},
                {"question": "Error handling block?", "answer": "try...catch"}
            ]
        },
        {
            "title": "Modern Frontend Frameworks (React Basics)",
            "description": "Introduction to React and component-based architecture.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=bMknfKXIFA8",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Learn React fundamentals including JSX, components, state, and props.",
            "steps": ["Understand component-based UI", "Create React app", "Use JSX", "Manage state", "Pass props"],
            "quiz": [
                {"question": "What is React?", "answer": "JavaScript UI library"},
                {"question": "JSX stands for?", "answer": "JavaScript XML"},
                {"question": "State is?", "answer": "Component data"},
                {"question": "Props are?", "answer": "Data passed to components"}
            ]
        },
        {
            "title": "Advanced React (Hooks & Performance)",
            "description": "Master React Hooks and performance optimization techniques.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=TNhaISOUy6Q",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Learn useState, useEffect, custom hooks, and memoization for optimal performance.",
            "steps": ["Learn useState and useEffect", "Custom hooks", "Memoization", "Optimize renders", "Code splitting"],
            "quiz": [
                {"question": "Hook for state?", "answer": "useState"},
                {"question": "Hook for lifecycle?", "answer": "useEffect"},
                {"question": "useMemo does?", "answer": "Memoize values"},
                {"question": "useCallback used for?", "answer": "Memoize functions"}
            ]
        },
        {
            "title": "Backend with Node.js & Express",
            "description": "Build server-side applications with Node.js and Express framework.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=Oe421EPjeBE",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 33,
            "information": "Setup Node.js server, create REST APIs with Express, and use middleware.",
            "steps": ["Setup Node.js server", "Create Express app", "Handle routes", "Use middleware", "Build REST APIs"],
            "quiz": [
                {"question": "Node.js is?", "answer": "JavaScript runtime"},
                {"question": "Express is?", "answer": "Web framework"},
                {"question": "HTTP method to create data?", "answer": "POST"},
                {"question": "Middleware is?", "answer": "Function between request & response"}
            ]
        },
        {
            "title": "Authentication & Authorization",
            "description": "Implement secure authentication and role-based access control.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=7nafaH9SddU",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Learn JWT tokens, password security, and authorization strategies.",
            "steps": ["Learn auth concepts", "Use JWT", "Secure passwords", "Protect routes", "Role-based access"],
            "quiz": [
                {"question": "JWT stands for?", "answer": "JSON Web Token"},
                {"question": "Purpose of authentication?", "answer": "Verify identity"},
                {"question": "Purpose of authorization?", "answer": "Verify permissions"},
                {"question": "Token stored where?", "answer": "Cookies or local storage"}
            ]
        },
        {
            "title": "Databases (MongoDB & SQL)",
            "description": "Work with both NoSQL and SQL databases effectively.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=-56x56UppqQ",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 34,
            "information": "Master MongoDB and SQL databases, CRUD operations, and data relationships.",
            "steps": ["Learn MongoDB basics", "Learn SQL basics", "Perform CRUD operations", "Connect DB to backend", "Handle relationships"],
            "quiz": [
                {"question": "MongoDB is?", "answer": "NoSQL database"},
                {"question": "SQL DB example?", "answer": "MySQL / PostgreSQL"},
                {"question": "CRUD means?", "answer": "Create Read Update Delete"},
                {"question": "Primary key is?", "answer": "Unique identifier"}
            ]
        },
        {
            "title": "Web Security Best Practices",
            "description": "Protect your applications from common security vulnerabilities.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=FJxW2a0XK_g",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Learn about XSS, CSRF, input sanitization, and secure communication.",
            "steps": ["Learn common attacks", "Prevent XSS", "Prevent CSRF", "Secure APIs", "Use HTTPS"],
            "quiz": [
                {"question": "XSS stands for?", "answer": "Cross-Site Scripting"},
                {"question": "CSRF stands for?", "answer": "Cross-Site Request Forgery"},
                {"question": "HTTPS provides?", "answer": "Encrypted communication"},
                {"question": "Why sanitize inputs?", "answer": "Prevent attacks"}
            ]
        },
        {
            "title": "Deployment, CI/CD & Performance",
            "description": "Deploy applications and optimize performance for production.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=1nxzOr6d0_c",
            "min_age": 14,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Learn deployment strategies, CI/CD pipelines, and performance optimization.",
            "steps": ["Build production-ready app", "Deploy frontend & backend", "Setup CI/CD", "Optimize performance", "Monitor app"],
            "quiz": [
                {"question": "What is CI/CD?", "answer": "Continuous Integration / Deployment"},
                {"question": "Tool for CI/CD?", "answer": "GitHub Actions"},
                {"question": "CDN used for?", "answer": "Fast content delivery"},
                {"question": "Lighthouse measures?", "answer": "Performance & SEO"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if advanced lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "Web Development",
                Lesson.title == "Advanced HTML & Accessibility (a11y)"
            ).first()
            
            if existing:
                print("Advanced Web Development lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} Advanced Web Development lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_advanced_web_development()
