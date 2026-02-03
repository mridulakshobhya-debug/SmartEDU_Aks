"""
Database seeding script - populates SmartEDU LMS with sample data
Run: python seed.py
"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from extensions import db
from models.book import Book
from models.lesson import Lesson
from models.user import User

# Import all seed functions
from seed_python_basics import seed_python_basics_course
from seed_advanced_python import seed_advanced_python_course
from seed_javascript import seed_javascript
from seed_javascript_advanced import seed_advanced_javascript
from seed_web_development import seed_web_development
from seed_web_development_advanced import seed_advanced_web_development
from seed_computer_science import seed_computer_science
from seed_computer_science_advanced import seed_advanced_computer_science
from seed_artificial_intelligence import seed_artificial_intelligence
from seed_artificial_intelligence_advanced import seed_advanced_artificial_intelligence


def seed_books():
    """Add sample books to database"""
    books_data = [
        {
            "title": "Harry Potter and the Sorcerer's Stone",
            "author": "J.K. Rowling",
            "description": "A young wizard discovers his magical heritage and begins his adventures at Hogwarts School.",
            "min_age": 8,
            "max_age": 18,
            "category": "Fantasy",
            "content": "Harry Potter is a young wizard..."
        },
        {
            "title": "The Lion, the Witch and the Wardrobe",
            "author": "C.S. Lewis",
            "description": "Four siblings discover a magical wardrobe that leads to the enchanted land of Narnia.",
            "min_age": 7,
            "max_age": 14,
            "category": "Fantasy",
            "content": "Lucy finds the wardrobe..."
        },
        {
            "title": "Journey to the Center of the Earth",
            "author": "Jules Verne",
            "description": "An exciting adventure story about exploring the mysteries beneath Earth's surface.",
            "min_age": 10,
            "max_age": 16,
            "category": "Science Fiction",
            "content": "The journey begins underground..."
        },
        {
            "title": "Charlotte's Web",
            "author": "E.B. White",
            "description": "A touching tale of friendship between a pig and a spider.",
            "min_age": 6,
            "max_age": 12,
            "category": "Classic",
            "content": "Wilbur the pig meets Charlotte..."
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "description": "An unexpected journey of a small hobbit through Middle-earth.",
            "min_age": 10,
            "max_age": 18,
            "category": "Fantasy",
            "content": "In a hole in the ground..."
        },
        {
            "title": "Percy Jackson and the Olympians: The Lightning Thief",
            "author": "Rick Riordan",
            "description": "A boy discovers he's a demigod and must go on a quest across America.",
            "min_age": 9,
            "max_age": 16,
            "category": "Fantasy",
            "content": "I didn't want to be a half-blood..."
        },
        {
            "title": "Diary of a Wimpy Kid",
            "author": "Jeff Kinney",
            "description": "Humorous misadventures of a middle school student and his journal entries.",
            "min_age": 8,
            "max_age": 14,
            "category": "Comedy",
            "content": "Today is the first day of a new year..."
        },
        {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "description": "An accessible explanation of black holes, the Big Bang, and the nature of time.",
            "min_age": 13,
            "max_age": 18,
            "category": "Science",
            "content": "Our goal is nothing less than a complete description..."
        }
    ]
    
    for book_data in books_data:
        existing = Book.query.filter_by(title=book_data["title"]).first()
        if not existing:
            book = Book(**book_data)
            db.session.add(book)
        print(f"[+] Added book: {book_data['title']}")
    db.session.commit()


def seed_lessons():
    """Add comprehensive lessons with quiz, steps, information, and video"""
    lessons_data = [
        # Python Courses
        {
            "title": "Python Basics: Variables and Data Types",
            "description": "Learn variables, integers, floats, strings and basic data types",
            "subject": "Python",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 45,
            "information": "Python is a versatile programming language. Variables store data in different formats: integers (whole numbers), floats (decimals), strings (text), and booleans (True/False).",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Python+Basics",
            "steps": [
                "Understand what variables are and why we use them",
                "Learn about different data types in Python",
                "Create your first variables",
                "Perform basic operations with data",
                "Practice type conversion"
            ],
            "quiz": [
                {"question": "What type is 42?", "options": ["String", "Integer", "Float"], "answer": 1},
                {"question": "What type is 'hello'?", "options": ["String", "Integer", "Boolean"], "answer": 0}
            ]
        },
        {
            "title": "Python: Control Flow and Loops",
            "description": "Master if statements, for loops, and while loops",
            "subject": "Python",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "Control flow statements allow your code to make decisions and repeat tasks. Use if/elif/else for decisions and for/while loops for repetition.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Control+Flow",
            "steps": [
                "Learn boolean logic and comparisons",
                "Write if statements",
                "Use elif for multiple conditions",
                "Create for loops with ranges",
                "Build while loops with conditions"
            ],
            "quiz": [
                {"question": "What does 'elif' mean?", "options": ["Else for", "Else if", "Else if-for"], "answer": 1},
                {"question": "Is 5 > 3?", "options": ["Yes", "No", "Maybe"], "answer": 0}
            ]
        },
        {
            "title": "Python: Functions and Modules",
            "description": "Create reusable functions and organize code with modules",
            "subject": "Python",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Functions are reusable blocks of code that perform a specific task. They make your code more organized and maintainable.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Functions",
            "steps": [
                "Define a function with def keyword",
                "Use parameters and arguments",
                "Return values from functions",
                "Understand variable scope",
                "Import and use modules"
            ],
            "quiz": [
                {"question": "What does 'def' do?", "options": ["Defines a function", "Defers code", "Defines value"], "answer": 0},
                {"question": "How do you return from a function?", "options": ["exit", "return", "break"], "answer": 1}
            ]
        },
        {
            "title": "Python: Object-Oriented Programming Basics",
            "description": "Understanding classes, objects, and inheritance in Python",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "OOP helps organize code into objects and classes, making large programs easier to manage and more reusable.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=OOP+Python",
            "steps": [
                "Understand classes and objects",
                "Create instance variables",
                "Define methods in classes",
                "Use constructors (__init__)",
                "Explore inheritance basics"
            ],
            "quiz": [
                {"question": "What is a class?", "options": ["Instance", "Blueprint", "Variable"], "answer": 1},
                {"question": "What is self?", "options": ["Variable", "Instance reference", "Function"], "answer": 1}
            ]
        },
        {
            "title": "Advanced Python: Decorators and Generators",
            "description": "Master advanced Python concepts for expert programmers",
            "subject": "Python",
            "difficulty": "advanced",
            "min_age": 14,
            "max_age": 18,
            "duration_minutes": 75,
            "information": "Decorators modify functions, and generators create memory-efficient sequences. These advanced features power much of professional Python code.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Advanced+Python",
            "steps": [
                "Understand higher-order functions",
                "Create decorators",
                "Apply decorators to functions",
                "Learn generator functions",
                "Optimize with yield statements"
            ],
            "quiz": [
                {"question": "What symbol creates a decorator?", "options": ["#", "@", "&"], "answer": 1},
                {"question": "What does yield do?", "options": ["Returns", "Generates sequence", "Gives control"], "answer": 1}
            ]
        },
        {
            "title": "Python: File Handling and I/O",
            "description": "Read, write, and manipulate files in Python",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "File I/O operations allow your programs to read from and write to files on disk, making data persistent.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=File+IO",
            "steps": [
                "Open files in different modes",
                "Read file contents",
                "Write to files",
                "Append data to files",
                "Handle file paths and exceptions"
            ],
            "quiz": [
                {"question": "What mode reads files?", "options": ["'w'", "'r'", "'a'"], "answer": 1},
                {"question": "What mode appends to files?", "options": ["'w'", "'r'", "'a'"], "answer": 2}
            ]
        },
        {
            "title": "Python: Web Development with Flask",
            "description": "Build web applications using Flask framework",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Flask is a lightweight web framework that makes building web applications fun and easy.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Flask",
            "steps": [
                "Setup Flask environment",
                "Create basic routes",
                "Use templates with Jinja2",
                "Handle forms and input",
                "Deploy Flask apps"
            ],
            "quiz": [
                {"question": "Flask is a what?", "options": ["CMS", "Framework", "Database"], "answer": 1},
                {"question": "What is a route?", "options": ["URL path", "Function", "Template"], "answer": 0}
            ]
        },
        {
            "title": "Python: Data Structures",
            "description": "Lists, tuples, dictionaries, and sets in Python",
            "subject": "Python",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Data structures organize data efficiently. Lists, tuples, dictionaries, and sets have different properties and uses.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Data+Structures",
            "steps": [
                "Understand lists and list operations",
                "Learn about tuples and immutability",
                "Create and use dictionaries",
                "Work with sets",
                "Choose the right data structure"
            ],
            "quiz": [
                {"question": "Lists are what?", "options": ["Immutable", "Mutable", "Permanent"], "answer": 1},
                {"question": "Dictionary stores what?", "options": ["Values only", "Keys and values", "Lists"], "answer": 1}
            ]
        },
        # Web Development Courses
        {
            "title": "HTML Fundamentals",
            "description": "Learn the structure of web pages with HTML",
            "subject": "Web Development",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 40,
            "information": "HTML (HyperText Markup Language) is the foundation of all web pages. It provides structure and content using semantic tags.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=HTML+Tutorial",
            "steps": [
                "Learn HTML document structure",
                "Understand semantic HTML elements",
                "Create forms and input fields",
                "Add links and images",
                "Build multi-page websites"
            ],
            "quiz": [
                {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "Home Tool Markup Language", "High Tech Modern Language"], "answer": 0},
                {"question": "What tag creates a heading?", "options": ["<h1>", "<head>", "<header>"], "answer": 0}
            ]
        },
        {
            "title": "CSS Styling Essentials",
            "description": "Master CSS for beautiful web page styling",
            "subject": "Web Development",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "CSS (Cascading Style Sheets) controls the visual appearance of web pages. Master selectors, properties, and layouts.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=CSS+Tutorial",
            "steps": [
                "Learn CSS selectors",
                "Apply colors and fonts",
                "Understand the box model",
                "Create layouts with flexbox",
                "Build responsive designs"
            ],
            "quiz": [
                {"question": "CSS controls what?", "options": ["Structure", "Styling", "Behavior"], "answer": 1},
                {"question": "What is a selector?", "options": ["Style rule", "Element target", "Property"], "answer": 1}
            ]
        },
        {
            "title": "JavaScript Fundamentals",
            "description": "Interactive web pages with JavaScript",
            "subject": "Web Development",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "JavaScript brings interactivity to web pages. Learn syntax, variables, functions, and DOM manipulation.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=JavaScript",
            "steps": [
                "JavaScript syntax and variables",
                "Operators and expressions",
                "Control flow statements",
                "Create and call functions",
                "Handle user events"
            ],
            "quiz": [
                {"question": "JavaScript runs where?", "options": ["Server", "Browser", "Database"], "answer": 1},
                {"question": "What declares a variable?", "options": ["var", "let", "const"], "answer": 0}
            ]
        },
        {
            "title": "React: Building Interactive UIs",
            "description": "Frontend library for component-based web development",
            "subject": "Web Development",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "React makes building interactive user interfaces easier by using reusable components and efficient rendering.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=React",
            "steps": [
                "Setup React development environment",
                "Create functional components",
                "Understand JSX syntax",
                "Use hooks and state",
                "Build component hierarchies"
            ],
            "quiz": [
                {"question": "React is a what?", "options": ["Framework", "Library", "Language"], "answer": 1},
                {"question": "JSX compiles to what?", "options": ["HTML", "JavaScript", "Python"], "answer": 1}
            ]
        },
        # Mathematics Courses
        {
            "title": "Algebra Basics: Equations",
            "description": "Solve linear and quadratic equations",
            "subject": "Mathematics",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 16,
            "duration_minutes": 50,
            "information": "Algebra uses symbols to represent numbers and solve equations. It's the foundation for advanced mathematics.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Algebra",
            "steps": [
                "Understand equations and variables",
                "Solve linear equations",
                "Work with polynomials",
                "Factor expressions",
                "Solve word problems"
            ],
            "quiz": [
                {"question": "Solve: 2x + 3 = 7", "options": ["1", "2", "3"], "answer": 1},
                {"question": "What is x in x - 5 = 10?", "options": ["5", "10", "15"], "answer": 2}
            ]
        },
        {
            "title": "Geometry: Shapes and Angles",
            "description": "Properties of geometric shapes and spatial reasoning",
            "subject": "Mathematics",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 16,
            "duration_minutes": 55,
            "information": "Geometry explores shapes, angles, and spatial relationships. It combines visual and analytical thinking.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Geometry",
            "steps": [
                "Learn angle types",
                "Study triangle properties",
                "Understand quadrilaterals",
                "Calculate areas and perimeters",
                "Explore 3D shapes"
            ],
            "quiz": [
                {"question": "Sum of triangle angles?", "options": ["90°", "180°", "360°"], "answer": 1},
                {"question": "Circle has how many sides?", "options": ["0", "1", "Infinite"], "answer": 2}
            ]
        },
        {
            "title": "Trigonometry Essentials",
            "description": "Sine, cosine, tangent, and angle relationships",
            "subject": "Mathematics",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Trigonometry studies relationships between angles and sides in triangles. Essential for advanced math and physics.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Trigonometry",
            "steps": [
                "Understand right triangles",
                "Learn sine, cosine, tangent",
                "Use trigonometric ratios",
                "Solve triangles",
                "Apply to real problems"
            ],
            "quiz": [
                {"question": "SOH-CAH-TOA is what?", "options": ["Acronym", "Word", "Formula"], "answer": 0},
                {"question": "sin(90°) equals?", "options": ["0", "1", "0.5"], "answer": 1}
            ]
        },
        {
            "title": "Calculus: Limits and Derivatives",
            "description": "Rates of change and fundamental calculus concepts",
            "subject": "Mathematics",
            "difficulty": "advanced",
            "min_age": 15,
            "max_age": 18,
            "duration_minutes": 80,
            "information": "Calculus analyzes continuous change. Derivatives measure rates of change, essential for physics and engineering.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Calculus",
            "steps": [
                "Understand limits",
                "Learn the derivative concept",
                "Calculate derivatives",
                "Apply power rule",
                "Optimize functions"
            ],
            "quiz": [
                {"question": "Derivative measures what?", "options": ["Area", "Rate of change", "Distance"], "answer": 1},
                {"question": "Derivative of x² is?", "options": ["x", "2x", "2x²"], "answer": 1}
            ]
        },
        # Science Courses
        {
            "title": "Physics: Motion and Forces",
            "description": "Newton's laws and mechanical motion",
            "subject": "Physics",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Motion describes how objects move. Forces cause motion according to Newton's Laws of Motion.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Physics",
            "steps": [
                "Understand distance and displacement",
                "Learn velocity and acceleration",
                "Explore Newton's First Law",
                "Study Newton's Second Law (F=ma)",
                "Understand Newton's Third Law"
            ],
            "quiz": [
                {"question": "What is velocity?", "options": ["Speed only", "Speed with direction", "Acceleration"], "answer": 1},
                {"question": "F = ma is Newton's what?", "options": ["First Law", "Second Law", "Third Law"], "answer": 1}
            ]
        },
        {
            "title": "Physics: Energy and Waves",
            "description": "Energy forms, conservation, and wave motion",
            "subject": "Physics",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Energy drives everything in the universe. Waves are how energy travels through space.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Energy+Waves",
            "steps": [
                "Understand kinetic and potential energy",
                "Learn energy conservation",
                "Study wave characteristics",
                "Explore sound waves",
                "Understand light as waves"
            ],
            "quiz": [
                {"question": "Energy is never what?", "options": ["Created", "Destroyed", "Changed"], "answer": 1},
                {"question": "Wavelength symbol?", "options": ["f", "λ", "v"], "answer": 1}
            ]
        },
        {
            "title": "Biology: Cells and Organisms",
            "description": "Cell structure and biological life processes",
            "subject": "Biology",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 17,
            "duration_minutes": 50,
            "information": "Cells are the basic units of life. Understanding cell structure and function is key to biology.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Biology",
            "steps": [
                "Learn prokaryotic vs eukaryotic cells",
                "Study cell membrane and nucleus",
                "Understand organelles and functions",
                "Learn cell division",
                "Explore cellular energy production"
            ],
            "quiz": [
                {"question": "Cell's control center?", "options": ["Nucleus", "Mitochondria", "Ribosome"], "answer": 0},
                {"question": "Prokaryotes lack what?", "options": ["DNA", "Nucleus", "Ribosomes"], "answer": 1}
            ]
        },
        {
            "title": "Biology: Genetics and Evolution",
            "description": "Heredity, DNA, and natural selection",
            "subject": "Biology",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Genetics explains how traits pass through generations. Evolution shows how life changes over time.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Genetics",
            "steps": [
                "Understand DNA structure",
                "Learn Mendelian inheritance",
                "Study genes and proteins",
                "Explore natural selection",
                "Understand evolutionary concepts"
            ],
            "quiz": [
                {"question": "DNA contains what?", "options": ["Proteins", "Genes", "Cells"], "answer": 1},
                {"question": "Who proposed evolution?", "options": ["Newton", "Darwin", "Einstein"], "answer": 1}
            ]
        },
        {
            "title": "Chemistry: Atoms and Molecules",
            "description": "Structure of atoms and chemical bonding",
            "subject": "Chemistry",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Chemistry is the study of matter and its reactions. Start with atomic structure and how atoms bond.",
            "video_url": "https://via.placeholder.com/640x360/fcbad3/ffffff?text=Chemistry",
            "steps": [
                "Learn atomic structure",
                "Understand electrons and protons",
                "Study chemical bonding",
                "Learn about molecules",
                "Explore the periodic table"
            ],
            "quiz": [
                {"question": "Smallest unit of matter?", "options": ["Molecule", "Atom", "Particle"], "answer": 1},
                {"question": "Oxygen's symbol?", "options": ["O", "Ox", "Oxx"], "answer": 0}
            ]
        },
        {
            "title": "Chemistry: Chemical Reactions",
            "description": "Reactions, equations, and energy changes",
            "subject": "Chemistry",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Chemical reactions rearrange atoms to form new substances. Understanding reactions is essential to chemistry.",
            "video_url": "https://via.placeholder.com/640x360/fcbad3/ffffff?text=Reactions",
            "steps": [
                "Write chemical equations",
                "Balance chemical equations",
                "Understand reaction types",
                "Study endothermic vs exothermic",
                "Apply rates of reaction"
            ],
            "quiz": [
                {"question": "H2O + CO2 produces?", "options": ["H2CO3", "H3O", "CO"], "answer": 0},
                {"question": "Reactants appear where?", "options": ["Left side", "Right side", "Middle"], "answer": 0}
            ]
        },
        # History and Social Studies
        {
            "title": "World History: Ancient Civilizations",
            "description": "Egypt, Mesopotamia, Greece, and Rome",
            "subject": "History",
            "difficulty": "intermediate",
            "min_age": 11,
            "max_age": 17,
            "duration_minutes": 60,
            "information": "Ancient civilizations laid the foundation for modern society, developing writing, government, and culture.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=History",
            "steps": [
                "Study Mesopotamian civilization",
                "Learn about Ancient Egypt",
                "Explore Ancient Greece",
                "Understand the Roman Empire",
                "Compare ancient cultures"
            ],
            "quiz": [
                {"question": "Where did writing first appear?", "options": ["Egypt", "Mesopotamia", "Greece"], "answer": 1},
                {"question": "Capital of Ancient Rome?", "options": ["Milan", "Rome", "Athens"], "answer": 1}
            ]
        },
        {
            "title": "World History: Medieval Period",
            "description": "Middle Ages in Europe and world",
            "subject": "History",
            "difficulty": "intermediate",
            "min_age": 11,
            "max_age": 17,
            "duration_minutes": 65,
            "information": "The Medieval Period shaped European culture, featuring feudalism, religion, and castle building.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=Medieval",
            "steps": [
                "Understand feudal system",
                "Learn about knights and chivalry",
                "Study Medieval church",
                "Explore crusades",
                "Understand Black Death impact"
            ],
            "quiz": [
                {"question": "Feudal system based on what?", "options": ["Money", "Land", "Religion"], "answer": 1},
                {"question": "Knights served whom?", "options": ["Kings", "Nobles", "Church"], "answer": 1}
            ]
        },
        {
            "title": "Geography: Continents and Oceans",
            "description": "Physical geography and world regions",
            "subject": "Geography",
            "difficulty": "beginner",
            "min_age": 9,
            "max_age": 15,
            "duration_minutes": 40,
            "information": "Geography studies Earth's physical features and human cultures. Learn about continents, oceans, and world regions.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=Geography",
            "steps": [
                "Learn the 7 continents",
                "Study major oceans and seas",
                "Understand mountain ranges",
                "Explore climate zones",
                "Map population distribution"
            ],
            "quiz": [
                {"question": "How many continents?", "options": ["5", "7", "9"], "answer": 1},
                {"question": "Largest ocean?", "options": ["Atlantic", "Pacific", "Indian"], "answer": 1}
            ]
        },
        {
            "title": "Geography: Climate and Weather",
            "description": "Weather patterns, climate zones, and meteorology",
            "subject": "Geography",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 16,
            "duration_minutes": 50,
            "information": "Climate shapes where people live and what they can grow. Weather affects our daily lives.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=Weather",
            "steps": [
                "Understand weather components",
                "Learn climate classification",
                "Study tropical climates",
                "Explore dry and temperate zones",
                "Understand climate change"
            ],
            "quiz": [
                {"question": "What causes seasons?", "options": ["Orbit", "Axis tilt", "Distance"], "answer": 1},
                {"question": "Tropical zone lies where?", "options": ["Arctic", "Equator", "Poles"], "answer": 1}
            ]
        },
        # Languages and Literature
        {
            "title": "English: Grammar Fundamentals",
            "description": "Nouns, verbs, adjectives, and sentence structure",
            "subject": "English",
            "difficulty": "beginner",
            "min_age": 9,
            "max_age": 15,
            "duration_minutes": 45,
            "information": "Grammar is the system of rules for using language correctly. Master parts of speech and sentence structure.",
            "video_url": "https://via.placeholder.com/640x360/a8d8ea/ffffff?text=Grammar",
            "steps": [
                "Learn parts of speech",
                "Understand sentence structure",
                "Master verb tenses",
                "Use pronouns correctly",
                "Apply punctuation rules"
            ],
            "quiz": [
                {"question": "What is a noun?", "options": ["Person, place, thing", "Action word", "Descriptive word"], "answer": 0},
                {"question": "What is a verb?", "options": ["Person", "Action", "Adjective"], "answer": 1}
            ]
        },
        {
            "title": "English: Literature Analysis",
            "description": "Reading comprehension, themes, and literary devices",
            "subject": "English",
            "difficulty": "intermediate",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Literature analysis teaches how to find meaning in texts through understanding themes and devices.",
            "video_url": "https://via.placeholder.com/640x360/a8d8ea/ffffff?text=Literature",
            "steps": [
                "Identify literary devices",
                "Analyze themes",
                "Study characterization",
                "Explore narrative structure",
                "Compare texts"
            ],
            "quiz": [
                {"question": "What is a metaphor?", "options": ["Direct comparison", "Implied comparison", "Opposite"], "answer": 1},
                {"question": "Setting is what?", "options": ["Plot", "Time and place", "Characters"], "answer": 1}
            ]
        },
        {
            "title": "Spanish: Beginners",
            "description": "Basic Spanish vocabulary and phrases",
            "subject": "Spanish",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "Spanish is spoken by 500+ million people worldwide. Start with essential greetings and basic conversation.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Spanish",
            "steps": [
                "Learn Spanish pronunciation",
                "Master common greetings",
                "Introduce yourself",
                "Learn polite expressions",
                "Have basic conversations"
            ],
            "quiz": [
                {"question": "'Hola' means?", "options": ["Goodbye", "Hello", "Thanks"], "answer": 1},
                {"question": "'Gracias' means?", "options": ["Thank you", "Please", "Yes"], "answer": 0}
            ]
        },
        {
            "title": "French: Beginner",
            "description": "Essential French vocabulary and phrases",
            "subject": "French",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "French is an elegant language spoken worldwide. Begin with basics for travel and communication.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=French",
            "steps": [
                "Learn French pronunciation",
                "Master basic greetings",
                "Order food and drinks",
                "Ask directions",
                "Have simple conversations"
            ],
            "quiz": [
                {"question": "'Bonjour' means?", "options": ["Good evening", "Good morning", "Goodbye"], "answer": 1},
                {"question": "'Au revoir' means?", "options": ["Hello", "Thank you", "Goodbye"], "answer": 2}
            ]
        },
        {
            "title": "German: Beginner",
            "description": "Fundamentals of German language",
            "subject": "German",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "German is spoken in central Europe. Learn basics for travel, business, and cultural exchange.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=German",
            "steps": [
                "German pronunciation",
                "Common greetings",
                "Numbers and time",
                "Shopping phrases",
                "Basic travel expressions"
            ],
            "quiz": [
                {"question": "'Guten Tag' means?", "options": ["Goodbye", "Good morning", "Good day"], "answer": 2},
                {"question": "'Danke' means?", "options": ["Please", "Thank you", "Yes"], "answer": 1}
            ]
        },
        {
            "title": "Japanese: Beginner",
            "description": "Introduction to Japanese language and culture",
            "subject": "Japanese",
            "difficulty": "beginner",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Japanese is unique with three writing systems. Start with survival phrases and hiragana.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Japanese",
            "steps": [
                "Learn hiragana basics",
                "Master key greetings",
                "Understand counting",
                "Essential travel phrases",
                "Cultural etiquette"
            ],
            "quiz": [
                {"question": "'Konnichiwa' means?", "options": ["Hello", "Goodbye", "Thank you"], "answer": 0},
                {"question": "'Arigatou' means?", "options": ["Hello", "Thank you", "Please"], "answer": 1}
            ]
        },
        # Arts and Humanities
        {
            "title": "Visual Arts: Drawing Basics",
            "description": "Shapes, perspective, and shading techniques",
            "subject": "Art",
            "difficulty": "beginner",
            "min_age": 9,
            "max_age": 18,
            "duration_minutes": 45,
            "information": "Drawing is the foundation of visual art. Learn techniques to draw anything from simple shapes to complex portraits.",
            "video_url": "https://via.placeholder.com/640x360/ffaaa5/ffffff?text=Drawing",
            "steps": [
                "Choose drawing materials",
                "Practice basic shapes",
                "Learn shading techniques",
                "Study perspective drawing",
                "Create portrait studies"
            ],
            "quiz": [
                {"question": "Basic shapes in drawing?", "options": ["Circles, squares, triangles", "Lines", "Dots"], "answer": 0},
                {"question": "What is shading?", "options": ["Dark areas", "Creating depth", "Erasing"], "answer": 1}
            ]
        },
        {
            "title": "Art History: Renaissance",
            "description": "Art and artists of the Renaissance period",
            "subject": "Art",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "The Renaissance was a rebirth of classical art and humanism, producing masterpieces still admired today.",
            "video_url": "https://via.placeholder.com/640x360/ffaaa5/ffffff?text=Renaissance",
            "steps": [
                "Understand Renaissance origins",
                "Study Leonardo da Vinci",
                "Explore Michelangelo's works",
                "Learn perspective techniques",
                "Analyze famous artworks"
            ],
            "quiz": [
                {"question": "Renaissance means what?", "options": ["Revival", "Beginning", "Ending"], "answer": 0},
                {"question": "Who painted Mona Lisa?", "options": ["Michelangelo", "Da Vinci", "Raphael"], "answer": 1}
            ]
        },
        {
            "title": "Music Theory Basics",
            "description": "Notes, scales, and rhythm fundamentals",
            "subject": "Music",
            "difficulty": "beginner",
            "min_age": 9,
            "max_age": 17,
            "duration_minutes": 40,
            "information": "Music theory is the study of how music works. Learn notes, scales, rhythm, and composition basics.",
            "video_url": "https://via.placeholder.com/640x360/ffb3ba/ffffff?text=Music+Theory",
            "steps": [
                "Learn the musical alphabet",
                "Understand scales",
                "Study rhythm and time signatures",
                "Learn chords",
                "Compose simple melodies"
            ],
            "quiz": [
                {"question": "How many notes in an octave?", "options": ["8", "12", "7"], "answer": 0},
                {"question": "What is a scale?", "options": ["Instrument", "Series of notes", "Rhythm"], "answer": 1}
            ]
        },
        # Computer Science
        {
            "title": "Computer Science: Algorithms",
            "description": "Problem-solving and algorithm design",
            "subject": "Computer Science",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Algorithms are step-by-step procedures to solve problems. They're at the heart of computer science.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=Algorithms",
            "steps": [
                "Understand what algorithms are",
                "Learn sorting algorithms",
                "Study searching techniques",
                "Analyze time complexity",
                "Optimize algorithm performance"
            ],
            "quiz": [
                {"question": "What is an algorithm?", "options": ["Program", "Procedure", "Function"], "answer": 1},
                {"question": "Binary search needs what?", "options": ["Any list", "Sorted list", "Random list"], "answer": 1}
            ]
        },
        {
            "title": "Computer Networks Basics",
            "description": "Internet, protocols, and data communication",
            "subject": "Computer Science",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Networks connect computers to share data. Understanding TCP/IP and protocols is essential.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=Networks",
            "steps": [
                "Understand network basics",
                "Learn about IP addresses",
                "Study packet transmission",
                "Learn about DNS",
                "Understand security basics"
            ],
            "quiz": [
                {"question": "What is IP address?", "options": ["Port", "Identifier", "Protocol"], "answer": 1},
                {"question": "HTTP uses what port?", "options": ["21", "80", "443"], "answer": 1}
            ]
        },
        {
            "title": "Database Design Basics",
            "description": "Relational databases and SQL fundamentals",
            "subject": "Computer Science",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Databases store and manage data efficiently. SQL is the language for working with databases.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=Databases",
            "steps": [
                "Understand database concepts",
                "Learn table structure",
                "Write SELECT queries",
                "Use WHERE clauses",
                "Join multiple tables"
            ],
            "quiz": [
                {"question": "SQL stands for?", "options": ["Simple Query Language", "Structured Query Language", "Standard Query Language"], "answer": 1},
                {"question": "SELECT is used for?", "options": ["Insert", "Delete", "Retrieve"], "answer": 2}
            ]
        },
        # Physical Education and Health
        {
            "title": "Physical Education: Fitness Basics",
            "description": "Exercise, nutrition, and health",
            "subject": "Physical Education",
            "difficulty": "beginner",
            "min_age": 9,
            "max_age": 18,
            "duration_minutes": 40,
            "information": "Physical fitness is essential for health and wellbeing. Learn cardio, strength, and flexibility training.",
            "video_url": "https://via.placeholder.com/640x360/c7ceea/ffffff?text=Fitness",
            "steps": [
                "Understand fitness components",
                "Learn warm-up and cool-down",
                "Practice cardio exercises",
                "Do strength training",
                "Create workout plans"
            ],
            "quiz": [
                {"question": "What is cardio?", "options": ["Strength", "Heart exercise", "Flexibility"], "answer": 1},
                {"question": "Warm-up duration?", "options": ["1 min", "5-10 min", "30 min"], "answer": 1}
            ]
        },
        {
            "title": "Health: Nutrition Essentials",
            "description": "Balanced diet and healthy eating habits",
            "subject": "Health",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 45,
            "information": "Good nutrition supports health and development. Learn about food groups and balanced diets.",
            "video_url": "https://via.placeholder.com/640x360/c7ceea/ffffff?text=Nutrition",
            "steps": [
                "Understand food groups",
                "Learn food pyramid",
                "Calculate calories",
                "Plan balanced meals",
                "Understand food labels"
            ],
            "quiz": [
                {"question": "Main food groups are?", "options": ["3", "5", "7"], "answer": 1},
                {"question": "Protein comes from?", "options": ["Meat only", "Legumes and dairy", "Vegetables"], "answer": 1}
            ]
        },
        # Additional Python Courses
        {
            "title": "Python: Testing and Debugging",
            "description": "Unit tests, debugging, and code quality",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Testing ensures code works correctly. Learn unit testing frameworks and debugging techniques.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Testing",
            "steps": [
                "Understand why testing matters",
                "Write unit tests with pytest",
                "Use assertions effectively",
                "Debug with breakpoints",
                "Measure code coverage"
            ],
            "quiz": [
                {"question": "What is a unit test?", "options": ["Full app test", "Single function test", "User test"], "answer": 1},
                {"question": "pytest is what?", "options": ["Editor", "Framework", "Library"], "answer": 2}
            ]
        },
        {
            "title": "Python: Async Programming",
            "description": "Asynchronous programming with async/await",
            "subject": "Python",
            "difficulty": "advanced",
            "min_age": 14,
            "max_age": 18,
            "duration_minutes": 75,
            "information": "Async programming allows multiple tasks to run concurrently, improving app performance.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Async",
            "steps": [
                "Understand async vs sync",
                "Learn async/await syntax",
                "Create coroutines",
                "Handle concurrent tasks",
                "Avoid common pitfalls"
            ],
            "quiz": [
                {"question": "async/await does what?", "options": ["Waits", "Pauses", "Non-blocking"], "answer": 2},
                {"question": "Coroutine is what?", "options": ["Loop", "Function", "Class"], "answer": 1}
            ]
        },
        {
            "title": "Python: Web Scraping",
            "description": "Extract data from websites using Python",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Web scraping extracts data from websites. Learn BeautifulSoup and Selenium for automation.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Web+Scraping",
            "steps": [
                "Understand HTTP requests",
                "Parse HTML with BeautifulSoup",
                "Extract data patterns",
                "Handle dynamic content",
                "Respect robots.txt"
            ],
            "quiz": [
                {"question": "BeautifulSoup parses what?", "options": ["URLs", "HTML", "Databases"], "answer": 1},
                {"question": "Selenium automates what?", "options": ["Networks", "Browsers", "Servers"], "answer": 1}
            ]
        },
        {
            "title": "Python: Data Analysis with Pandas",
            "description": "Data manipulation and analysis with Pandas",
            "subject": "Python",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Pandas is the go-to library for data analysis. Learn DataFrames and data wrangling.",
            "video_url": "https://via.placeholder.com/640x360/1f5cf0/ffffff?text=Pandas",
            "steps": [
                "Understand DataFrames",
                "Read and write data",
                "Clean messy data",
                "Group and aggregate",
                "Visualize findings"
            ],
            "quiz": [
                {"question": "DataFrame is what?", "options": ["List", "Dictionary", "Table"], "answer": 2},
                {"question": "Pandas reads what files?", "options": ["HTML only", "CSV, Excel, etc", "Code only"], "answer": 1}
            ]
        },
        # Additional Web Development
        {
            "title": "Vue.js: Progressive Framework",
            "description": "Build interactive UIs with Vue.js",
            "subject": "Web Development",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Vue.js is a progressive framework for building user interfaces incrementally.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=Vue.js",
            "steps": [
                "Vue basics and templates",
                "Component architecture",
                "State management",
                "Handle events",
                "Build full applications"
            ],
            "quiz": [
                {"question": "Vue is what kind of framework?", "options": ["Backend", "Progressive", "Rigid"], "answer": 1},
                {"question": "Components in Vue are?", "options": ["Static", "Reusable", "One-time"], "answer": 1}
            ]
        },
        {
            "title": "Node.js Fundamentals",
            "description": "Server-side JavaScript with Node.js",
            "subject": "Web Development",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Node.js allows JavaScript to run on servers. Build scalable backend applications.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=Node.js",
            "steps": [
                "Setup Node environment",
                "Understand modules",
                "Use npm packages",
                "Build HTTP servers",
                "Handle asynchronous code"
            ],
            "quiz": [
                {"question": "Node.js runs where?", "options": ["Browser", "Server", "Mobile"], "answer": 1},
                {"question": "npm stands for?", "options": ["Node", "Node Package Manager", "Network"], "answer": 1}
            ]
        },
        {
            "title": "Express.js: Web Server",
            "description": "Build REST APIs with Express.js",
            "subject": "Web Development",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Express is a minimal Node.js framework for building web servers and APIs.",
            "video_url": "https://via.placeholder.com/640x360/ff6b6b/ffffff?text=Express",
            "steps": [
                "Setup Express server",
                "Create routes",
                "Handle requests/responses",
                "Use middleware",
                "Connect to databases"
            ],
            "quiz": [
                {"question": "Express is what?", "options": ["Frontend", "Framework", "Language"], "answer": 1},
                {"question": "Routes in Express are?", "options": ["URLs", "Functions", "Data"], "answer": 0}
            ]
        },
        # Additional Mathematics
        {
            "title": "Statistics Basics",
            "description": "Data analysis and probability",
            "subject": "Mathematics",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Statistics helps us understand data. Learn distributions, probability, and inference.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Statistics",
            "steps": [
                "Understand populations and samples",
                "Calculate mean, median, mode",
                "Learn standard deviation",
                "Study probability distributions",
                "Hypothesis testing"
            ],
            "quiz": [
                {"question": "Mean is what?", "options": ["Average", "Middle", "Most frequent"], "answer": 0},
                {"question": "Normal distribution is?", "options": ["Skewed", "Bell curve", "Flat"], "answer": 1}
            ]
        },
        {
            "title": "Linear Algebra Basics",
            "description": "Vectors, matrices, and transformations",
            "subject": "Mathematics",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Linear algebra is fundamental to computer science and machine learning.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Linear+Algebra",
            "steps": [
                "Understand vectors",
                "Learn matrix operations",
                "Calculate determinants",
                "Solve systems of equations",
                "Applications in ML"
            ],
            "quiz": [
                {"question": "Matrix is what?", "options": ["Vector", "Array", "Number"], "answer": 1},
                {"question": "Determinant shows what?", "options": ["Size", "Invertibility", "Direction"], "answer": 1}
            ]
        },
        {
            "title": "Precalculus: Functions",
            "description": "Polynomial, exponential, and trigonometric functions",
            "subject": "Mathematics",
            "difficulty": "intermediate",
            "min_age": 14,
            "max_age": 18,
            "duration_minutes": 75,
            "information": "Precalculus prepares you for calculus by mastering functions and their properties.",
            "video_url": "https://via.placeholder.com/640x360/4ecdc4/ffffff?text=Precalc",
            "steps": [
                "Understand function notation",
                "Graph functions",
                "Study function transformations",
                "Learn exponential functions",
                "Master inverse functions"
            ],
            "quiz": [
                {"question": "f(x) notation means?", "options": ["Multiply", "Function evaluation", "Variable"], "answer": 1},
                {"question": "Inverse function does what?", "options": ["Multiplies", "Reverses", "Adds"], "answer": 1}
            ]
        },
        # Additional Sciences
        {
            "title": "Physics: Electricity and Magnetism",
            "description": "Electric circuits and magnetic fields",
            "subject": "Physics",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Electricity and magnetism power modern technology. Learn circuits, fields, and induction.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=E&M",
            "steps": [
                "Understand electric charges",
                "Learn Ohm's law",
                "Analyze circuits",
                "Study magnetic fields",
                "Electromagnetic induction"
            ],
            "quiz": [
                {"question": "Ohm's law is?", "options": ["V=IR", "I=V/R", "Both"], "answer": 2},
                {"question": "Current measures what?", "options": ["Voltage", "Resistance", "Charge flow"], "answer": 2}
            ]
        },
        {
            "title": "Physics: Quantum Mechanics Intro",
            "description": "Introduction to quantum theory",
            "subject": "Physics",
            "difficulty": "advanced",
            "min_age": 15,
            "max_age": 18,
            "duration_minutes": 80,
            "information": "Quantum mechanics explains the behavior of atoms and subatomic particles.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Quantum",
            "steps": [
                "Photons and quanta",
                "Uncertainty principle",
                "Wave-particle duality",
                "Atomic models",
                "Applications in technology"
            ],
            "quiz": [
                {"question": "Photon is what?", "options": ["Particle", "Light quantum", "Wave"], "answer": 1},
                {"question": "Planck constant is?", "options": ["h", "c", "G"], "answer": 0}
            ]
        },
        {
            "title": "Biology: Human Body Systems",
            "description": "Circulatory, respiratory, and digestive systems",
            "subject": "Biology",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Human body systems work together to keep us alive. Learn how they function.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Body+Systems",
            "steps": [
                "Circulatory system function",
                "Heart and blood vessels",
                "Respiratory gas exchange",
                "Digestive process",
                "Interconnected systems"
            ],
            "quiz": [
                {"question": "Heart pumps what?", "options": ["Air", "Blood", "Nutrients"], "answer": 1},
                {"question": "Lungs exchange what?", "options": ["Nutrients", "Oxygen/CO2", "Hormones"], "answer": 1}
            ]
        },
        {
            "title": "Biology: Ecology and Ecosystems",
            "description": "Food chains, habitats, and biodiversity",
            "subject": "Biology",
            "difficulty": "intermediate",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Ecology studies relationships between organisms and their environment.",
            "video_url": "https://via.placeholder.com/640x360/95e1d3/ffffff?text=Ecology",
            "steps": [
                "Understand ecosystems",
                "Study food webs",
                "Learn energy flow",
                "Explore population dynamics",
                "Biodiversity importance"
            ],
            "quiz": [
                {"question": "Food chain starts with?", "options": ["Animals", "Producers", "Decomposers"], "answer": 1},
                {"question": "Predator eats what?", "options": ["Plants", "Prey", "Fungi"], "answer": 1}
            ]
        },
        {
            "title": "Chemistry: Organic Chemistry Basics",
            "description": "Carbon compounds and organic synthesis",
            "subject": "Chemistry",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Organic chemistry studies carbon-based compounds, the chemistry of life.",
            "video_url": "https://via.placeholder.com/640x360/fcbad3/ffffff?text=Organic",
            "steps": [
                "Carbon properties",
                "Organic functional groups",
                "Isomers and naming",
                "Reaction mechanisms",
                "Biological molecules"
            ],
            "quiz": [
                {"question": "Organic chemistry studies?", "options": ["Metals", "Carbon compounds", "Energy"], "answer": 1},
                {"question": "Hydrocarbons contain?", "options": ["Oxygen", "C and H", "Nitrogen"], "answer": 1}
            ]
        },
        # Additional History
        {
            "title": "World History: Renaissance to Enlightenment",
            "description": "Cultural rebirth and scientific revolution",
            "subject": "History",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "The Renaissance and Enlightenment transformed European thought and science.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=Renaissance",
            "steps": [
                "Renaissance origins in Italy",
                "Humanism movement",
                "Scientific revolution",
                "Key discoveries",
                "Enlightenment thinkers"
            ],
            "quiz": [
                {"question": "Renaissance means?", "options": ["End", "Rebirth", "Dark"], "answer": 1},
                {"question": "Copernicus proposed what?", "options": ["Gravity", "Heliocentric model", "Atoms"], "answer": 1}
            ]
        },
        {
            "title": "World History: Industrial Revolution",
            "description": "Machines, factories, and social change",
            "subject": "History",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "The Industrial Revolution transformed society from agrarian to industrial.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=Industrial",
            "steps": [
                "Causes of industrialization",
                "Textile industry innovations",
                "Steam engine impact",
                "Factory system",
                "Social consequences"
            ],
            "quiz": [
                {"question": "Industrial Revolution started where?", "options": ["France", "Germany", "Britain"], "answer": 2},
                {"question": "Steam engine powered?", "options": ["Ships", "Factories", "All"], "answer": 2}
            ]
        },
        {
            "title": "World History: World Wars",
            "description": "World War I and World War II",
            "subject": "History",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 75,
            "information": "The World Wars shaped the modern era, causing unprecedented death and change.",
            "video_url": "https://via.placeholder.com/640x360/f38181/ffffff?text=World+Wars",
            "steps": [
                "WW1 causes and course",
                "Treaty of Versailles",
                "Rise of fascism",
                "WW2 timeline",
                "Holocaust and aftermath"
            ],
            "quiz": [
                {"question": "WW1 started in?", "options": ["1914", "1918", "1920"], "answer": 0},
                {"question": "WW2 ended in?", "options": ["1943", "1945", "1947"], "answer": 1}
            ]
        },
        # Additional Languages
        {
            "title": "Chinese Mandarin: Basics",
            "description": "Essential Mandarin Chinese phrases",
            "subject": "Chinese",
            "difficulty": "beginner",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Mandarin is spoken by over 1 billion people. Start with essential survival phrases.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Mandarin",
            "steps": [
                "Chinese phonetic system",
                "Tones in Mandarin",
                "Numbers and counting",
                "Daily greetings",
                "Basic conversations"
            ],
            "quiz": [
                {"question": "Mandarin has how many tones?", "options": ["2", "4", "6"], "answer": 1},
                {"question": "'Ni hao' means?", "options": ["Goodbye", "Hello", "Thank you"], "answer": 1}
            ]
        },
        {
            "title": "Italian: Beginner",
            "description": "The language of art and passion",
            "subject": "Italian",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "Italian is a melodic language spoken by 85+ million people worldwide.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Italian",
            "steps": [
                "Italian pronunciation",
                "Basic greetings",
                "Numbers and dates",
                "Food and dining",
                "Travel phrases"
            ],
            "quiz": [
                {"question": "'Ciao' means?", "options": ["Hello", "Hello/Goodbye", "Good evening"], "answer": 1},
                {"question": "'Grazie' means?", "options": ["Please", "Thank you", "Yes"], "answer": 1}
            ]
        },
        # Computer Science and Technology
        {
            "title": "Machine Learning Basics",
            "description": "Supervised learning and prediction models",
            "subject": "Computer Science",
            "difficulty": "advanced",
            "min_age": 14,
            "max_age": 18,
            "duration_minutes": 80,
            "information": "Machine learning enables computers to learn from data. Essential for AI applications.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=ML",
            "steps": [
                "Machine learning concepts",
                "Training and testing",
                "Supervised vs unsupervised",
                "Classification algorithms",
                "Evaluate model performance"
            ],
            "quiz": [
                {"question": "ML learns from what?", "options": ["Code", "Data", "Rules"], "answer": 1},
                {"question": "Training set is used to?", "options": ["Test", "Learn", "Deploy"], "answer": 1}
            ]
        },
        {
            "title": "Cloud Computing Fundamentals",
            "description": "AWS, Azure, and cloud deployment",
            "subject": "Computer Science",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 70,
            "information": "Cloud computing provides on-demand computing resources over the internet.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=Cloud",
            "steps": [
                "Cloud computing models",
                "IaaS, PaaS, SaaS",
                "AWS services overview",
                "Deploying applications",
                "Cost optimization"
            ],
            "quiz": [
                {"question": "Cloud computing provides?", "options": ["Servers", "Services", "Both"], "answer": 2},
                {"question": "AWS stands for?", "options": ["Amazon Web", "Amazon Web Services", "Application"], "answer": 1}
            ]
        },
        {
            "title": "Cybersecurity Basics",
            "description": "Protection against digital threats",
            "subject": "Computer Science",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 65,
            "information": "Cybersecurity protects systems and data from digital attacks.",
            "video_url": "https://via.placeholder.com/640x360/aa96da/ffffff?text=Security",
            "steps": [
                "Common threats and attacks",
                "Encryption basics",
                "Password security",
                "Network security",
                "Best practices"
            ],
            "quiz": [
                {"question": "Encryption does what?", "options": ["Hides", "Protects", "Scrambles"], "answer": 2},
                {"question": "Phishing is what?", "options": ["Fish", "Scam", "Network"], "answer": 1}
            ]
        },
        # Additional Specialized Topics
        {
            "title": "Environmental Science Essentials",
            "description": "Ecosystems, climate, and sustainability",
            "subject": "Environmental Science",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Environmental science studies Earth's systems and how to protect them.",
            "video_url": "https://via.placeholder.com/640x360/52b788/ffffff?text=Environment",
            "steps": [
                "Earth's systems",
                "Climate and weather",
                "Biomes and biodiversity",
                "Conservation",
                "Sustainability solutions"
            ],
            "quiz": [
                {"question": "Greenhouse gases cause?", "options": ["Ozone", "Warming", "Cooling"], "answer": 1},
                {"question": "Conservation protects what?", "options": ["Money", "Resources", "Computers"], "answer": 1}
            ]
        },
        {
            "title": "Economics Basics",
            "description": "Supply, demand, and markets",
            "subject": "Economics",
            "difficulty": "intermediate",
            "min_age": 12,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Economics studies how people make choices about limited resources.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Economics",
            "steps": [
                "Scarcity and opportunity cost",
                "Supply and demand",
                "Market equilibrium",
                "Economic systems",
                "Inflation and interest"
            ],
            "quiz": [
                {"question": "Supply curve goes?", "options": ["Down", "Up", "Flat"], "answer": 1},
                {"question": "Demand curve goes?", "options": ["Down", "Up", "Flat"], "answer": 0}
            ]
        },
        {
            "title": "Business Management Basics",
            "description": "Leadership, organization, and planning",
            "subject": "Business",
            "difficulty": "intermediate",
            "min_age": 13,
            "max_age": 18,
            "duration_minutes": 60,
            "information": "Business management applies organizational and leadership principles.",
            "video_url": "https://via.placeholder.com/640x360/ffd89b/ffffff?text=Management",
            "steps": [
                "Management functions",
                "Organizational structure",
                "Leadership styles",
                "Decision making",
                "Teams and culture"
            ],
            "quiz": [
                {"question": "Management includes?", "options": ["Planning", "Organizing", "Both"], "answer": 2},
                {"question": "Leadership is about?", "options": ["Rules", "Influence", "Power"], "answer": 1}
            ]
        },
        {
            "title": "Public Speaking Essentials",
            "description": "Presentation skills and communication",
            "subject": "Communication",
            "difficulty": "beginner",
            "min_age": 11,
            "max_age": 18,
            "duration_minutes": 50,
            "information": "Public speaking is a valuable skill for school, work, and life.",
            "video_url": "https://via.placeholder.com/640x360/a8d8ea/ffffff?text=Speaking",
            "steps": [
                "Overcome nervousness",
                "Organize your thoughts",
                "Create visuals",
                "Delivery techniques",
                "Handle questions"
            ],
            "quiz": [
                {"question": "Good speech needs?", "options": ["Script", "Planning", "Microphone"], "answer": 1},
                {"question": "Eye contact shows?", "options": ["Nervousness", "Confidence", "Boredom"], "answer": 1}
            ]
        },
        {
            "title": "Creative Writing Workshop",
            "description": "Storytelling, dialogue, and character development",
            "subject": "Writing",
            "difficulty": "beginner",
            "min_age": 10,
            "max_age": 18,
            "duration_minutes": 55,
            "information": "Creative writing develops imagination and communication skills.",
            "video_url": "https://via.placeholder.com/640x360/a8d8ea/ffffff?text=Writing",
            "steps": [
                "Story structure",
                "Character creation",
                "Dialogue writing",
                "Worldbuilding",
                "Revision techniques"
            ],
            "quiz": [
                {"question": "Story has how many acts?", "options": ["1", "3", "5"], "answer": 1},
                {"question": "Dialogue reveals?", "options": ["Info", "Character", "Both"], "answer": 2}
            ]
        }
    ]
    
    for lesson_data in lessons_data:
        existing = Lesson.query.filter_by(title=lesson_data["title"]).first()
        if not existing:
            lesson = Lesson(**lesson_data)
            db.session.add(lesson)
    
    db.session.commit()
    print(f"[+] Added {len(lessons_data)} comprehensive lessons")


def seed_users():
    """Add sample users to database"""
    users_data = [
        {"username": "student_10", "email": "student10@smartedu.com", "age": 10, "full_name": "Student 10"},
        {"username": "student_12", "email": "student12@smartedu.com", "age": 12, "full_name": "Student 12"},
        {"username": "student_14", "email": "student14@smartedu.com", "age": 14, "full_name": "Student 14"},
        {"username": "student_16", "email": "student16@smartedu.com", "age": 16, "full_name": "Student 16"},
    ]
    
    # Clear existing users
    User.query.delete()
    
    for user_data in users_data:
        user = User(**user_data)
        user.set_password("password123")
        db.session.add(user)
        print(f"[+] Added user: {user_data['username']}")
    
    db.session.commit()


def main():
    """Initialize the database with sample data"""
    app = create_app()
    
    with app.app_context():
        print("\n[*] Seeding SmartEDU LMS database...\n")
        
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        print("\nAdding books...")
        seed_books()
        
        print("\nAdding lessons from seed files...")
        # Call all individual seed functions
        print("  → Python Basics...")
        seed_python_basics_course()
        
        print("  → Python Advanced...")
        seed_advanced_python_course()
        
        print("  → JavaScript...")
        seed_javascript()
        
        print("  → JavaScript Advanced...")
        seed_advanced_javascript()
        
        print("  → Web Development...")
        seed_web_development()
        
        print("  → Web Development Advanced...")
        seed_advanced_web_development()
        
        print("  → Computer Science...")
        seed_computer_science()
        
        print("  → Computer Science Advanced...")
        seed_advanced_computer_science()
        
        print("  → Artificial Intelligence...")
        seed_artificial_intelligence()
        
        print("  → Artificial Intelligence Advanced...")
        seed_advanced_artificial_intelligence()
        
        print("\nAdding users...")
        seed_users()
        
        # Count total lessons
        total_lessons = Lesson.query.count()
        print(f"\n[+] Database seeded successfully!")
        print(f"[+] Total lessons in database: {total_lessons}\n")


if __name__ == "__main__":
    main()
