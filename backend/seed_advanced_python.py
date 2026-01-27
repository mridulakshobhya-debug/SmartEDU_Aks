#!/usr/bin/env python
"""
Seed Advanced Python Programming: Full Course Content (12 Lessons)
"""
import json
from app import create_app, db
from models.lesson import Lesson

def seed_advanced_python_course():
    """Add Advanced Python Programming course with 12 lessons"""
    
    app = create_app()
    with app.app_context():
        # Clear existing Advanced Python lessons
        Lesson.query.filter_by(subject="Python").filter(Lesson.title.like("Lesson %")).delete()
        db.session.commit()
        
        lessons_data = [
            {
                "title": "Lesson 1: Functions (Advanced Usage)",
                "description": "Master function scope, arguments, and documentation",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=9Os0o3wzS_I",
                "content": "Learn advanced function techniques including scope, default arguments, keyword arguments, returning multiple values, and writing reusable functions with proper documentation.",
                "information": ["Function scope determines variable accessibility", "Default arguments provide fallback values", "Keyword arguments allow flexible argument order", "Functions can return multiple values as tuples", "Docstrings document function purpose and usage", "Write reusable functions for different inputs"],
                "steps": ["Understand function scope (local vs global)", "Use default and keyword arguments", "Return multiple values", "Use docstrings for documentation", "Write reusable functions"],
                "quiz": [{"question": "What keyword defines a function?", "options": ["function", "def", "func"], "correct": 1}, {"question": "What does return do?", "options": ["Exits the function", "Sends a value back to the caller", "Restarts the function"], "correct": 1}, {"question": "Can a function return multiple values?", "options": ["No", "Yes (as tuple)", "Only two values"], "correct": 1}, {"question": "What is a docstring?", "options": ["A comment", "Documentation string inside a function", "A code error"], "correct": 1}]
            },
            {
                "title": "Lesson 2: Lambda Functions",
                "description": "Learn anonymous functions and functional programming",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 25,
                "video_url": "https://www.youtube.com/watch?v=25ovCm9jKfA",
                "content": "Master lambda functions - anonymous functions for simple operations. Learn syntax, use with map() and filter(), and understand when to use lambda vs regular functions.",
                "information": ["Lambda functions are anonymous (unnamed) functions", "Can only contain a single expression", "Useful for simple operations", "Often used with map(), filter(), and sorted()", "Not suitable for complex multi-line logic", "Return value is implicit (no return keyword needed)"],
                "steps": ["Learn what lambda functions are", "Understand syntax of lambda", "Use lambda with map()", "Use lambda with filter()", "Compare lambda vs normal functions"],
                "quiz": [{"question": "What is a lambda function?", "options": ["A regular function", "An anonymous function", "A class"], "correct": 1}, {"question": "How many expressions can lambda have?", "options": ["Two", "One", "Unlimited"], "correct": 1}, {"question": "Which lambda adds two numbers?", "options": ["lambda a: a + b", "lambda a, b: a + b", "def a, b: a + b"], "correct": 1}, {"question": "Can lambda have multiple lines?", "options": ["Yes", "No", "Only two lines"], "correct": 1}]
            },
            {
                "title": "Lesson 3: Lists, Tuples, Sets & Dictionaries (Deep Dive)",
                "description": "Master Python's core data structures",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 35,
                "video_url": "https://www.youtube.com/watch?v=W8KRzm-HUcc",
                "content": "Deep dive into Python data structures. Learn mutable vs immutable types, advanced list methods, set operations, dictionary iteration, and conversion between data structures.",
                "information": ["Mutable data types can be modified after creation", "Immutable data types cannot be changed once created", "Lists are mutable and ordered", "Tuples are immutable and ordered", "Sets are mutable but unordered and contain unique elements", "Dictionaries store key-value pairs", "Set operations: union, intersection, difference", "Master conversion between data structures"],
                "steps": ["Understand mutable vs immutable", "Learn list methods deeply", "Use set operations", "Iterate dictionaries efficiently", "Convert between data structures"],
                "quiz": [{"question": "Which data type is immutable?", "options": ["List", "Tuple", "Dictionary"], "correct": 1}, {"question": "What does set() remove?", "options": ["Odd numbers", "Duplicates", "First element"], "correct": 1}, {"question": "How to access dictionary value?", "options": ["dict.key", "dict[key]", "dict->key"], "correct": 1}, {"question": "Which structure uses key-value pairs?", "options": ["List", "Set", "Dictionary"], "correct": 2}]
            },
            {
                "title": "Lesson 4: List, Dict & Set Comprehensions",
                "description": "Write concise and readable code with comprehensions",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=3dt4OGnU5sM",
                "content": "Learn comprehensions - a Pythonic way to create lists, dictionaries, and sets. Convert loops into comprehensions, use conditionals, and improve code readability.",
                "information": ["List comprehension replaces for loops for simple operations", "Syntax: [expression for item in iterable]", "Can use if conditions inside comprehensions", "Dict comprehension creates dictionaries concisely", "Set comprehension creates sets with unique elements", "Comprehensions are faster than traditional loops", "Keep comprehensions simple for readability", "Nested comprehensions flatten complex data structures"],
                "steps": ["Understand comprehension syntax", "Convert loops into comprehensions", "Use conditionals inside comprehensions", "Create dict comprehensions", "Improve code readability"],
                "quiz": [{"question": "What does list comprehension replace?", "options": ["Functions", "Loops", "Classes"], "correct": 1}, {"question": "Comprehension syntax starts with?", "options": ["Parentheses ()", "Curly braces {}", "Square brackets []"], "correct": 2}, {"question": "Can we use if inside comprehension?", "options": ["No", "Yes", "Only once"], "correct": 1}, {"question": "Result type of dict comprehension?", "options": ["List", "Set", "Dictionary"], "correct": 2}]
            },
            {
                "title": "Lesson 5: Object-Oriented Programming (OOP)",
                "description": "Master classes, objects, and OOP principles",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 40,
                "video_url": "https://www.youtube.com/watch?v=Ej_02ICOIgs",
                "content": "Learn Object-Oriented Programming. Understand classes and objects, use constructors, work with attributes and methods, and create multiple objects from one class.",
                "information": ["A class is a blueprint for objects", "An object is an instance of a class", "__init__() initializes object attributes", "self refers to the instance (the object itself)", "Attributes store data (properties)", "Methods define behaviors (actions)", "Can create multiple objects from one class", "OOP allows organizing code into logical units"],
                "steps": ["Learn class and object concepts", "Use __init__() constructor", "Understand attributes and methods", "Create multiple objects", "Apply real-world examples"],
                "quiz": [{"question": "What is a class?", "options": ["An object", "Blueprint for objects", "A function"], "correct": 1}, {"question": "What is an object?", "options": ["A class", "Instance of a class", "A variable"], "correct": 1}, {"question": "Purpose of __init__()?", "options": ["Ends the class", "Initializes object", "Prints output"], "correct": 1}, {"question": "Keyword to access instance variables?", "options": ["this", "self", "me"], "correct": 1}]
            },
            {
                "title": "Lesson 6: Inheritance & Polymorphism",
                "description": "Reuse code through inheritance and polymorphism",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 35,
                "video_url": "https://www.youtube.com/watch?v=RSl87lqOXDE",
                "content": "Learn inheritance to reuse parent class code and polymorphism for flexible design. Understand method overriding and the super() keyword.",
                "information": ["Inheritance allows code reuse between classes", "Parent class passes attributes and methods to child class", "Method overriding redefines parent methods in child class", "Polymorphism: same method name, different behavior", "super() accesses parent class methods", "Can have multi-level inheritance", "Inheritance creates relationships (is-a relationships)", "Makes code more maintainable and organized"],
                "steps": ["Understand inheritance", "Use parent and child classes", "Override methods", "Learn polymorphism", "Use super() keyword"],
                "quiz": [{"question": "What is inheritance?", "options": ["Creating a new class", "Reusing parent class features", "Copying code"], "correct": 1}, {"question": "Syntax for inheritance?", "options": ["class Child extends Parent", "class Child(Parent)", "class Child -> Parent"], "correct": 1}, {"question": "What does method overriding mean?", "options": ["Deleting parent method", "Redefining parent method", "Ignoring method"], "correct": 1}, {"question": "What is polymorphism?", "options": ["Multiple classes", "Same function, different behavior", "Many objects"], "correct": 1}]
            },
            {
                "title": "Lesson 7: Exception Handling",
                "description": "Handle errors gracefully in your programs",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=NIWwJbo-9_8",
                "content": "Master exception handling with try-except blocks, handle multiple exceptions, use finally, and create custom exceptions.",
                "information": ["Exceptions are runtime errors that can be caught", "try block contains code that might cause error", "except block handles specific exceptions", "Multiple except blocks handle different errors", "finally block executes regardless of errors", "raise keyword throws custom exceptions", "Custom exceptions inherit from Exception class", "Exception handling prevents program crashes"],
                "steps": ["Understand runtime errors", "Use try and except", "Handle multiple exceptions", "Use finally", "Create custom exceptions"],
                "quiz": [{"question": "What block handles errors?", "options": ["try", "except", "handle"], "correct": 1}, {"question": "Which block always executes?", "options": ["try", "except", "finally"], "correct": 2}, {"question": "Error for invalid int conversion?", "options": ["TypeError", "ValueError", "ConversionError"], "correct": 1}, {"question": "Can we define custom exceptions?", "options": ["No", "Yes", "Only built-in ones"], "correct": 1}]
            },
            {
                "title": "Lesson 8: File Handling",
                "description": "Read, write, and manage files",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
                "content": "Learn file operations - reading, writing, and managing files. Use the with statement for safe file handling and implement error handling.",
                "information": ["open() function opens files in different modes", "Read mode (r) reads files without modifying", "Write mode (w) overwrites file content", "Append mode (a) adds to end of file", "read() returns entire file as string", "readlines() returns list of lines", "with statement automatically closes files", "Always handle file errors with try-except"],
                "steps": ["Open files using open()", "Read files using read() and readlines()", "Write and append data", "Use with statement", "Handle file errors"],
                "quiz": [{"question": "Mode to read file?", "options": ["w", "r", "a"], "correct": 1}, {"question": "Mode to write file?", "options": ["r", "w", "x"], "correct": 1}, {"question": "Why use with statement?", "options": ["Write files", "Auto close file", "Read files"], "correct": 1}, {"question": "What auto-closes files?", "options": ["close()", "with", "end()"], "correct": 1}]
            },
            {
                "title": "Lesson 9: Modules & Packages",
                "description": "Organize code and reuse libraries",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=1RuMJ53CKds",
                "content": "Learn modules and packages for code organization. Import built-in modules, create custom modules, and use pip to manage external libraries.",
                "information": ["A module is a Python file with reusable code", "import loads an entire module", "from...import loads specific items", "Built-in modules: math, random, datetime, os", "A package is a directory of modules", "__init__.py makes a directory a package", "pip installs external packages", "Follow naming conventions for modules and packages"],
                "steps": ["Understand modules", "Import built-in modules", "Create custom modules", "Learn packages", "Use pip for libraries"],
                "quiz": [{"question": "What is a module?", "options": ["A class", "Python file with code", "A function"], "correct": 1}, {"question": "How to import math module?", "options": ["use math", "import math", "load math"], "correct": 1}, {"question": "What file makes a package?", "options": ["package.py", "__init__.py", "main.py"], "correct": 1}, {"question": "Tool to install packages?", "options": ["npm", "pip", "apt"], "correct": 1}]
            },
            {
                "title": "Lesson 10: Decorators & Generators",
                "description": "Master advanced function techniques",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 35,
                "video_url": "https://www.youtube.com/watch?v=FsAPt_9Bf3U",
                "content": "Learn decorators to modify function behavior and generators to create memory-efficient sequences. Use @ syntax and yield keyword.",
                "information": ["A decorator modifies function behavior", "@symbol marks decorator syntax", "Decorators are functions that return functions", "Generators use yield keyword", "yield returns values one at a time", "Generators are memory efficient", "Generator expressions use () syntax", "next() gets next value from generator"],
                "steps": ["Understand decorators concept", "Create simple decorators", "Use @ syntax", "Learn generators", "Use yield"],
                "quiz": [{"question": "What does a decorator do?", "options": ["Deletes function", "Modifies function behavior", "Creates class"], "correct": 1}, {"question": "Symbol used for decorators?", "options": ["%", "@", "#"], "correct": 1}, {"question": "What keyword creates generator?", "options": ["return", "yield", "generate"], "correct": 1}, {"question": "Generator returns values using?", "options": ["return", "yield", "send"], "correct": 1}]
            },
            {
                "title": "Lesson 11: Multithreading & Multiprocessing",
                "description": "Run multiple tasks concurrently",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 40,
                "video_url": "https://www.youtube.com/watch?v=IEEhzQoKtQU",
                "content": "Learn concurrent programming with threading for I/O tasks and multiprocessing for CPU-bound tasks. Understand when to use each approach.",
                "information": ["Concurrency: multiple tasks appear to run together", "Parallelism: tasks run on different CPU cores", "Threading is best for I/O-bound operations", "Multiprocessing is best for CPU-bound operations", "threading module: lightweight, shares memory", "multiprocessing module: heavyweight, separate processes", "GIL (Global Interpreter Lock) limits threading", "Locks prevent race conditions in multithreading"],
                "steps": ["Understand concurrency", "Learn threading module", "Learn multiprocessing module", "Compare threads vs processes", "Write simple concurrent programs"],
                "quiz": [{"question": "What is multithreading?", "options": ["One task", "Running tasks in parallel", "Writing multiple files"], "correct": 1}, {"question": "Which module uses CPU cores?", "options": ["threading", "multiprocessing", "asyncio"], "correct": 1}, {"question": "Threading is best for?", "options": ["CPU tasks", "I/O bound tasks", "Game development"], "correct": 1}, {"question": "Multiprocessing is best for?", "options": ["Web requests", "CPU bound tasks", "User input"], "correct": 1}]
            },
            {
                "title": "Lesson 12: Virtual Environments & Best Practices",
                "description": "Professional Python development practices",
                "subject": "Python",
                "difficulty": "advanced",
                "min_age": 14,
                "max_age": 18,
                "duration_minutes": 30,
                "video_url": "https://www.youtube.com/watch?v=N5vscPTWKOk",
                "content": "Learn virtual environments for project isolation and Python best practices including PEP 8, docstrings, type hints, and error handling.",
                "information": ["Virtual environments isolate Python installations", "Prevents dependency conflicts between projects", "python -m venv creates virtual environment", "requirements.txt lists project dependencies", "PEP 8 is Python's style guide", "Docstrings document functions and classes", "Type hints improve code clarity", "Professional projects follow best practices"],
                "steps": ["Understand virtual environments", "Create venv", "Activate venv", "Install packages safely", "Follow Python best practices"],
                "quiz": [{"question": "Why use virtual environment?", "options": ["For speed", "Avoid dependency conflicts", "For security"], "correct": 1}, {"question": "Command to create venv?", "options": ["pip venv", "python -m venv venv", "create-venv"], "correct": 1}, {"question": "What file stores dependencies?", "options": ["config.txt", "requirements.txt", "packages.txt"], "correct": 1}, {"question": "Why follow PEP8?", "options": ["Required by law", "Code readability and standards", "Faster execution"], "correct": 1}]
            }
        ]
        
        # Create all lessons with JSON serialization
        for lesson_data in lessons_data:
            # Convert lists to JSON strings
            lesson_data['information'] = json.dumps(lesson_data['information'])
            lesson_data['steps'] = json.dumps(lesson_data['steps'])
            lesson_data['quiz'] = json.dumps(lesson_data['quiz'])
            lesson = Lesson(**lesson_data)
            db.session.add(lesson)
        
        db.session.commit()
        print("Successfully added 12 Advanced Python lessons!")
        print("\nLessons created:")
        for i, lesson_data in enumerate(lessons_data, 1):
            print(f"  {i}. {lesson_data['title']}")


if __name__ == "__main__":
    seed_advanced_python_course()
