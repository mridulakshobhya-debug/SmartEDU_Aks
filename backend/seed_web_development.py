"""
Seed Web Development Basics course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_web_development():
    """Seed Web Development Basics lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "Introduction to Web Development",
            "description": "Learn the fundamentals of web development, including frontend vs backend and how the internet works.",
            "subject": "Web Development",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=3JluqTojuME",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 15,
            "information": "This lesson covers the basics of web development including the client-server model and how browsers work.",
            "steps": ["Understand what websites and web apps are", "Learn frontend vs backend", "Understand client–server model", "Learn how browsers work", "Explore examples of real websites"],
            "quiz": [
                {"question": "What is web development?", "answer": "Creating websites and web applications"},
                {"question": "What are the two main parts of web development?", "answer": "Frontend and Backend"},
                {"question": "What is a browser?", "answer": "Software to access websites"},
                {"question": "What is a server?", "answer": "A system that stores and delivers website data"}
            ]
        },
        {
            "title": "HTML Basics (Structure of Web Pages)",
            "description": "Master HTML fundamentals and learn how to structure web pages using tags and elements.",
            "subject": "Web Development",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=UB1O30fR-EE",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "HTML is the foundation of web pages. Learn how to use tags and elements to create structured content.",
            "steps": ["Learn what HTML is", "Understand HTML tags and elements", "Learn basic tags: html, head, body", "Create your first HTML page", "Open HTML file in browser"],
            "quiz": [
                {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
                {"question": "Which tag contains page content?", "answer": "<body>"},
                {"question": "What tag is used for headings?", "answer": "<h1> to <h6>"},
                {"question": "What is an HTML element?", "answer": "Tag with content inside it"}
            ]
        },
        {
            "title": "HTML Forms & Inputs",
            "description": "Learn how to create forms and collect user input with various input types and validation.",
            "subject": "Web Development",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=fNcJuPIZ2WE",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 18,
            "information": "Forms are essential for user interaction. Learn about input types, labels, placeholders, and form validation.",
            "steps": ["Learn why forms are used", "Use input types (text, email, password)", "Use labels and placeholders", "Learn form validation basics", "Submit form data"],
            "quiz": [
                {"question": "Which tag creates a form?", "answer": "<form>"},
                {"question": "Input type for email?", "answer": "email"},
                {"question": "What attribute makes field required?", "answer": "required"},
                {"question": "Purpose of placeholder?", "answer": "Shows hint text"}
            ]
        },
        {
            "title": "CSS Basics (Styling Web Pages)",
            "description": "Learn CSS fundamentals to style your HTML pages with colors, fonts, and layouts.",
            "subject": "Web Development",
            "difficulty": "Beginner",
            "video_url": "https://www.youtube.com/watch?v=1Rs2ND1ryYc",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 22,
            "information": "CSS brings style and design to HTML pages. Learn inline, internal, and external CSS methods.",
            "steps": ["Understand what CSS does", "Learn inline, internal, external CSS", "Style text and colors", "Use classes and IDs", "Apply CSS to HTML"],
            "quiz": [
                {"question": "What does CSS stand for?", "answer": "Cascading Style Sheets"},
                {"question": "Which CSS is best practice?", "answer": "External CSS"},
                {"question": "How to select class?", "answer": ".class"},
                {"question": "How to select ID?", "answer": "#id"}
            ]
        },
        {
            "title": "CSS Layout (Flexbox & Grid)",
            "description": "Master CSS layout systems with Flexbox and Grid for creating responsive page layouts.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=JJSoEo8JSnc",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 25,
            "information": "Modern web layouts use Flexbox and Grid. Learn the box model and build responsive designs.",
            "steps": ["Learn box model", "Understand Flexbox", "Align items using Flexbox", "Learn Grid basics", "Build page layout"],
            "quiz": [
                {"question": "Which CSS property enables flex?", "answer": "display: flex"},
                {"question": "Property for horizontal alignment?", "answer": "justify-content"},
                {"question": "Grid is used for?", "answer": "Two-dimensional layouts"},
                {"question": "Box model includes?", "answer": "Margin, border, padding, content"}
            ]
        },
        {
            "title": "JavaScript Basics",
            "description": "Learn JavaScript fundamentals including variables, data types, conditions, loops, and functions.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "JavaScript is the programming language of the web. Learn the basics to make interactive pages.",
            "steps": ["Understand what JavaScript does", "Use variables and data types", "Write conditions and loops", "Use functions", "Run JS in browser"],
            "quiz": [
                {"question": "What is JavaScript?", "answer": "Programming language for web"},
                {"question": "Keyword to declare variable?", "answer": "let, var, const"},
                {"question": "What does if do?", "answer": "Conditional logic"},
                {"question": "Function keyword?", "answer": "function"}
            ]
        },
        {
            "title": "DOM Manipulation",
            "description": "Learn to interact with the DOM to create dynamic and interactive web pages.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=0ik6X4DJKCc",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 24,
            "information": "The DOM allows you to dynamically change page content. Learn selection and manipulation techniques.",
            "steps": ["Understand DOM", "Select HTML elements", "Change text and styles", "Handle button clicks", "Build interactive pages"],
            "quiz": [
                {"question": "What does DOM stand for?", "answer": "Document Object Model"},
                {"question": "Method to select element by ID?", "answer": "getElementById"},
                {"question": "How to change text?", "answer": "innerText"},
                {"question": "Event for button click?", "answer": "click"}
            ]
        },
        {
            "title": "Responsive Web Design",
            "description": "Learn to create websites that adapt to any screen size using responsive design techniques.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=srvUrASNj0s",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Responsive design ensures your site works on all devices. Learn media queries and flexible units.",
            "steps": ["Learn what responsiveness is", "Use media queries", "Use flexible units", "Design for mobile first", "Test on different screens"],
            "quiz": [
                {"question": "What is responsive design?", "answer": "Adapts to screen size"},
                {"question": "CSS feature for responsiveness?", "answer": "Media queries"},
                {"question": "Unit best for responsive text?", "answer": "em or rem"},
                {"question": "Mobile-first means?", "answer": "Design for mobile first"}
            ]
        },
        {
            "title": "Git & GitHub (Version Control)",
            "description": "Learn version control with Git and GitHub to manage code and collaborate with developers.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=RGOj5yH7evk",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 20,
            "information": "Version control is essential for professional development. Learn Git basics and GitHub collaboration.",
            "steps": ["Learn why version control is needed", "Install Git", "Use basic Git commands", "Push code to GitHub", "Collaborate using GitHub"],
            "quiz": [
                {"question": "What is Git?", "answer": "Version control system"},
                {"question": "Command to check status?", "answer": "git status"},
                {"question": "Command to push code?", "answer": "git push"},
                {"question": "What is GitHub?", "answer": "Code hosting platform"}
            ]
        },
        {
            "title": "Backend Basics (Intro)",
            "description": "Introduction to backend development, APIs, HTTP methods, and connecting frontend to backend.",
            "subject": "Web Development",
            "difficulty": "Intermediate",
            "video_url": "https://www.youtube.com/watch?v=ENrzD9HAZK4",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 23,
            "information": "Understand how the backend works and how it connects to the frontend through APIs.",
            "steps": ["Learn what backend is", "Understand APIs", "Learn HTTP methods", "Connect frontend to backend", "Overview of databases"],
            "quiz": [
                {"question": "Backend handles?", "answer": "Server logic and data"},
                {"question": "API stands for?", "answer": "Application Programming Interface"},
                {"question": "GET method is used for?", "answer": "Fetching data"},
                {"question": "POST method is used for?", "answer": "Sending data"}
            ]
        },
        {
            "title": "Databases (Basics)",
            "description": "Learn database fundamentals including SQL, NoSQL, and CRUD operations.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 27,
            "information": "Databases store and manage application data. Learn SQL, NoSQL, and how to perform CRUD operations.",
            "steps": ["Learn what databases are", "SQL vs NoSQL", "Tables and records", "Basic CRUD operations", "Connect database to backend"],
            "quiz": [
                {"question": "What is a database?", "answer": "Data storage system"},
                {"question": "SQL stands for?", "answer": "Structured Query Language"},
                {"question": "CRUD means?", "answer": "Create Read Update Delete"},
                {"question": "Example of NoSQL DB?", "answer": "MongoDB"}
            ]
        },
        {
            "title": "Deploying a Website",
            "description": "Learn how to deploy your website and make it accessible to the world.",
            "subject": "Web Development",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=nhBVL41-_Cw",
            "min_age": 13,
            "max_age": 100,
            "duration_minutes": 19,
            "information": "Deployment is the final step to make your website live. Learn hosting platforms and domains.",
            "steps": ["Understand deployment", "Choose hosting platform", "Upload frontend files", "Connect domain", "Make site live"],
            "quiz": [
                {"question": "What is deployment?", "answer": "Making website live"},
                {"question": "Example hosting platform?", "answer": "Netlify / Vercel"},
                {"question": "What is domain?", "answer": "Website address"},
                {"question": "Why deployment needed?", "answer": "To access site publicly"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if lessons already exist
            existing = db.session.query(Lesson).filter_by(subject="Web Development").first()
            if existing:
                print("Web Development lessons already exist in database. Skipping seeding.")
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
            print(f"✅ Successfully added {len(lessons_data)} Web Development lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_web_development()
