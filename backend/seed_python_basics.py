#!/usr/bin/env python
"""
Seed Python Basics: Variables and Data Types course with 10 lessons
"""
import json
from app import create_app, db
from models.lesson import Lesson

def seed_python_basics_course():
    """Add Python Basics course with 10 lessons"""
    
    app = create_app()
    with app.app_context():
        # Clear existing Python Basics lessons
        Lesson.query.filter_by(subject="Python Basics").delete()
        db.session.commit()
        
        lessons_data = [
            {
                "title": "Lesson 1: What is a Variable?",
                "description": "Learn what variables are and how Python stores data",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 15,
                "content": """
# What is a Variable?

Think of a variable as a labeled box that stores something.

**Box name → Value inside**

## Python Example
```python
age = 15
```

- `age` → variable name
- `=` → assignment operator
- `15` → value stored

## Rules for Variable Names

✅ **Allowed:**
- letters, numbers, underscore
- must start with a letter or underscore

❌ **Not Allowed:**
- starting with a number
- spaces
- special symbols (@, $, %)

## Valid Examples:
```python
name = "Akshu"
user_age = 20
_total = 100
```
                """,
                "information": [
                    "Variables are containers for storing data values",
                    "Variable names must start with a letter or underscore",
                    "Python is case-sensitive: age ≠ Age",
                    "Use meaningful variable names for better code readability"
                ],
                "steps": [
                    "Understand what variables are",
                    "Learn variable naming rules",
                    "Create your first variable",
                    "Practice with multiple variables"
                ],
                "quiz": [
                    {
                        "question": "What does the '=' symbol do in Python?",
                        "options": ["Equals comparison", "Assignment operator", "Less than"],
                        "correct": 1
                    },
                    {
                        "question": "Can a variable name start with a number?",
                        "options": ["Yes", "No", "Sometimes"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 2: Python Data Types (Introduction)",
                "description": "Explore the main data types in Python",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 20,
                "content": """
# Python Data Types (Introduction)

Python needs to know what kind of data it is working with.

## Main Built-in Data Types (Basics)

| Data Type | Example | Meaning |
|-----------|---------|---------|
| int | 10 | Whole numbers |
| float | 3.14 | Decimal numbers |
| str | "Hello" | Text |
| bool | True / False | Yes / No |

Each data type has its own characteristics and operations you can perform on it.
                """,
                "information": [
                    "Python has multiple data types for different kinds of data",
                    "int: whole numbers without decimals",
                    "float: numbers with decimal points",
                    "str: text enclosed in quotes",
                    "bool: True or False values"
                ],
                "steps": [
                    "Learn about int type",
                    "Learn about float type",
                    "Learn about str type",
                    "Learn about bool type"
                ],
                "quiz": [
                    {
                        "question": "Which data type would you use for the text 'Hello'?",
                        "options": ["int", "float", "str"],
                        "correct": 2
                    },
                    {
                        "question": "What data type is 3.14?",
                        "options": ["int", "float", "str"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 3: Integer (int)",
                "description": "Master working with whole numbers",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 20,
                "content": """
# Integer (int)

## Definition
Whole numbers (no decimals).

```python
score = 95
temperature = -5
```

## Operations
```python
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a // b)  # Division (integer result): 3
```

## Key Points:
- Integers can be positive or negative
- No decimal point
- Supports basic arithmetic operations
                """,
                "information": [
                    "Integers are whole numbers",
                    "Can be positive, negative, or zero",
                    "Support arithmetic operations: +, -, *, //, %",
                    "Use // for integer division (no decimals in result)"
                ],
                "steps": [
                    "Create integer variables",
                    "Perform addition with integers",
                    "Perform multiplication with integers",
                    "Use integer division operator"
                ],
                "quiz": [
                    {
                        "question": "What is 10 // 3 in Python?",
                        "options": ["3.33", "3", "4"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 4: Floating Point (float)",
                "description": "Work with decimal numbers",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 20,
                "content": """
# Floating Point (float)

## Definition
Numbers with decimal points.

```python
price = 99.99
height = 5.8
```

## Mixing int and float
```python
x = 10
y = 3.5

result = x + y
print(result)        # 13.5
print(type(result))  # <class 'float'>
```

## Key Points:
- Can represent fractional values
- More precise than integers
- When int and float mix, result is float
                """,
                "information": [
                    "Floats represent decimal numbers",
                    "More memory than integers",
                    "Mixing int and float produces float",
                    "Used for measurements, prices, etc."
                ],
                "steps": [
                    "Create float variables",
                    "Perform arithmetic with floats",
                    "Mix integers and floats",
                    "Observe type conversion"
                ],
                "quiz": [
                    {
                        "question": "What is the type of 10 + 3.5?",
                        "options": ["int", "float", "str"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 5: String (str)",
                "description": "Learn to work with text data",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 25,
                "content": """
# String (str)

## Definition
Text data inside quotes.

```python
name = "Akshu"
message = 'Welcome to Python'
```

## String Operations
```python
first = "Hello"
second = "World"

print(first + " " + second)  # Hello World
```

## Accessing Characters
```python
word = "Python"
print(word[0])  # P
print(word[3])  # h
print(word[-1]) # n (last character)
```

## Key Points:
- Use single or double quotes
- Can concatenate strings with +
- Can access individual characters by index
- Indexing starts at 0
                """,
                "information": [
                    "Strings are sequences of characters",
                    "Can use single or double quotes",
                    "Concatenate with + operator",
                    "Access characters by index (0-based)",
                    "Negative indexing works from end"
                ],
                "steps": [
                    "Create string variables",
                    "Concatenate strings",
                    "Access characters by positive index",
                    "Use negative indexing"
                ],
                "quiz": [
                    {
                        "question": "What is word[0] for 'Python'?",
                        "options": ["y", "P", "o"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 6: Boolean (bool)",
                "description": "Understand True and False values",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 15,
                "content": """
# Boolean (bool)

## Definition
Logical values:
- True
- False

```python
is_student = True
is_adult = False
```

## Comparison Example
```python
age = 15
print(age > 18)   # False
print(age == 15)  # True
print(age < 13)   # False
```

## Key Points:
- Used in conditions and logic
- Result of comparison operations
- Essential for decision making in code
                """,
                "information": [
                    "Booleans represent True or False",
                    "Result of comparison operations",
                    "Used in conditional statements",
                    "Essential for logical operations"
                ],
                "steps": [
                    "Create boolean variables",
                    "Use comparison operators",
                    "Understand True/False results",
                    "Apply in logical operations"
                ],
                "quiz": [
                    {
                        "question": "What is the result of 15 > 18?",
                        "options": ["True", "False", "Error"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 7: Checking Data Types (type())",
                "description": "Use type() function to identify data types",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 15,
                "content": """
# Checking Data Types (type())

Use `type()` to see what kind of data Python is storing.

```python
x = 10
y = 3.14
z = "Hello"
a = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(a))  # <class 'bool'>
```

## Why Use type()?
- Debug your code
- Understand data being stored
- Check if conversion is needed
- Learn about Python's type system

## Key Points:
- type() is a built-in function
- Returns the class/type of the variable
- Helpful for troubleshooting
                """,
                "information": [
                    "type() function returns the data type",
                    "Useful for debugging and verification",
                    "Shows <class 'typename'>",
                    "Helps identify type mismatches"
                ],
                "steps": [
                    "Create variables of different types",
                    "Use type() to check each one",
                    "Observe the output format",
                    "Use type() for debugging"
                ],
                "quiz": [
                    {
                        "question": "What does type('hello') return?",
                        "options": ["<class 'str'>", "<class 'int'>", "error"],
                        "correct": 0
                    }
                ]
            },
            {
                "title": "Lesson 8: Type Conversion (VERY IMPORTANT)",
                "description": "Convert between different data types",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 25,
                "content": """
# Type Conversion (VERY IMPORTANT)

Sometimes you must convert data types.

## Convert to Integer
```python
num = "10"
num = int(num)  # Now it's 10 (integer)
```

## Convert to Float
```python
price = "99.5"
price = float(price)  # Now it's 99.5 (float)
```

## Convert to String
```python
age = 15
print("My age is " + str(age))  # Works!
```

## ⚠️ Common Mistake

```python
print("Age: " + 15)  # ERROR!
```

**Correct way:**
```python
print("Age: " + str(15))  # Works!
```

## Key Points:
- int() converts to integer
- float() converts to float
- str() converts to string
- Use for user input processing
- Essential for mixing data types
                """,
                "information": [
                    "Type conversion is critical in Python",
                    "int() converts strings to integers",
                    "float() converts to decimal numbers",
                    "str() converts any type to string",
                    "Needed when combining different types",
                    "Common source of beginner errors"
                ],
                "steps": [
                    "Convert string to integer",
                    "Convert string to float",
                    "Convert number to string",
                    "Combine different types correctly"
                ],
                "quiz": [
                    {
                        "question": "How do you convert 'Hello' to string? (It's already a string, but the conversion function is:)",
                        "options": ["int('Hello')", "float('Hello')", "str('Hello')"],
                        "correct": 2
                    },
                    {
                        "question": "What does int('25') return?",
                        "options": ["'25'", "25.0", "25"],
                        "correct": 2
                    }
                ]
            },
            {
                "title": "Lesson 9: Multiple Variable Assignment",
                "description": "Assign multiple variables efficiently",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 15,
                "content": """
# Multiple Variable Assignment

## Assign Different Values
```python
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30
```

## Assign Same Value
```python
x = y = z = 100
print(x, y, z)  # 100 100 100
```

## Unpack Lists
```python
numbers = [1, 2, 3]
x, y, z = numbers
print(x, y, z)  # 1 2 3
```

## Key Points:
- Multiple assignments on one line
- Must have same number of values and variables
- Makes code more concise
- Easier to read and maintain
                """,
                "information": [
                    "Assign multiple variables at once",
                    "Number of variables must match values",
                    "Assign same value to multiple variables",
                    "Unpack sequences into variables",
                    "Makes code cleaner and more Pythonic"
                ],
                "steps": [
                    "Assign different values to multiple variables",
                    "Assign same value to multiple variables",
                    "Unpack a list into variables",
                    "Use multiple assignments in practice"
                ],
                "quiz": [
                    {
                        "question": "What are the values of a, b, c after: a, b, c = 1, 2, 3?",
                        "options": ["1, 2, 3", "3, 2, 1", "Error"],
                        "correct": 0
                    }
                ]
            },
            {
                "title": "Lesson 10: User Input (Using Variables)",
                "description": "Get input from users and store in variables",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 12,
                "max_age": 18,
                "duration_minutes": 20,
                "content": """
# User Input (Using Variables)

## Getting Input from User
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("Next year you will be", age + 1)
```

## Important Points:
- input() always returns a string
- Convert to int or float when needed
- Use meaningful prompts
- Store result in a variable

## Example Program:
```python
name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("What's your height in cm? "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Next year you'll be {age + 1}")
```

## Key Points:
- input() waits for user to type
- Always returns string type
- Must convert if you need numbers
- Can use for interactive programs
                """,
                "information": [
                    "input() function gets user input",
                    "Always returns string type",
                    "Convert with int() or float()",
                    "Use for interactive programs",
                    "Store input in variables for reuse"
                ],
                "steps": [
                    "Use input() to get name",
                    "Use input() with int() for number",
                    "Store input in variables",
                    "Process and display user data"
                ],
                "quiz": [
                    {
                        "question": "What type does input() always return?",
                        "options": ["int", "float", "str"],
                        "correct": 2
                    }
                ]
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
        print("✅ Successfully added 10 Python Basics lessons!")
        print("\nLessons created:")
        for i, lesson_data in enumerate(lessons_data, 1):
            print(f"  {i}. {lesson_data['title']}")


if __name__ == "__main__":
    seed_python_basics_course()
