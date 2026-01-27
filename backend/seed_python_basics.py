#!/usr/bin/env python
"""
Seed Python Basics: Full Course Content for Beginners (8 Lessons)
"""
import json
from app import create_app, db
from models.lesson import Lesson

def seed_python_basics_course():
    """Add Python Basics course with 8 comprehensive lessons"""
    
    app = create_app()
    with app.app_context():
        # Clear existing Python Basics lessons
        Lesson.query.filter_by(subject="Python Basics").delete()
        db.session.commit()
        
        lessons_data = [
            {
                "title": "Lesson 1: What is a Variable?",
                "description": "Learn what variables are and how to create them",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 15,
                "video_url": "https://www.youtube.com/watch?v=ZDa-Z5JzLYM",
                "content": """
# Lesson 1: What is a Variable?

## Understanding Variables
A variable is a container for storing data values. Think of it like a labeled box where you store information.

## Creating Variables
```python
# Syntax: variable_name = value
age = 15
name = "Akshu"
price = 99.99
is_student = True
```

## Variable Naming Rules
✅ **Valid names:**
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (age ≠ Age)
- Use meaningful names

❌ **Invalid names:**
- Cannot start with a number (1age)
- Cannot contain spaces
- Cannot contain special characters (@, $, %)
- Cannot use Python keywords

## Examples
```python
# Valid
user_age = 20
_total = 100
age_1 = 25

# Invalid
1age = 20  # Error: starts with number
class = 10  # Error: 'class' is a keyword
user-age = 20  # Error: hyphen not allowed
```
                """,
                "information": [
                    "A variable stores data in memory",
                    "Variables are created using the = operator",
                    "Variable names must start with a letter or underscore",
                    "Python is case-sensitive: age and Age are different",
                    "Use descriptive variable names for readability"
                ],
                "steps": [
                    "Understand what a variable is (a container for data)",
                    "Learn rules for naming variables",
                    "Assign values using =",
                    "Print variables using print()",
                    "Change variable values and observe output"
                ],
                "quiz": [
                    {
                        "question": "What is a variable?",
                        "options": ["A mathematical formula", "A container for data", "A Python function"],
                        "correct": 1
                    },
                    {
                        "question": "Which is a valid variable name?",
                        "options": ["1age", "age_1", "class"],
                        "correct": 1
                    },
                    {
                        "question": "What does x = 5 mean?",
                        "options": ["x equals 5", "Assigns value 5 to variable x", "Compares x and 5"],
                        "correct": 1
                    },
                    {
                        "question": "How do you display a variable?",
                        "options": ["show(x)", "print(x)", "display(x)"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 2: Python Data Types (Introduction)",
                "description": "Learn about the main data types in Python",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 20,
                "video_url": "https://www.youtube.com/watch?v=khKv-8q7YmY",
                "content": """
# Lesson 2: Python Data Types (Introduction)

## What are Data Types?
Data types tell Python what kind of information a variable contains and what operations can be performed on it.

## The Four Main Data Types

### int (Integer)
Whole numbers without decimals.
```python
age = 25
score = -10
count = 0
```

### float (Floating Point)
Numbers with decimal points.
```python
height = 5.9
price = 19.99
temperature = -2.5
```

### str (String)
Text data enclosed in quotes.
```python
name = "Alice"
message = 'Hello World'
city = "New York"
```

### bool (Boolean)
Logical values: True or False.
```python
is_student = True
is_adult = False
has_license = True
```

## Checking Data Types
Use the type() function to check data types:
```python
print(type(25))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```
                """,
                "information": [
                    "int: whole numbers without decimals",
                    "float: numbers with decimal points",
                    "str: text enclosed in quotes (single or double)",
                    "bool: True or False values",
                    "Use type() function to check data types"
                ],
                "steps": [
                    "Learn what data types are",
                    "Understand common types: int, float, str, bool",
                    "Create examples of each type",
                    "Use type() to check data types",
                    "Mix data types in simple programs"
                ],
                "quiz": [
                    {
                        "question": "Name any four Python data types.",
                        "options": ["int, float, str, bool", "int, text, number, logic", "list, tuple, set, dict"],
                        "correct": 0
                    },
                    {
                        "question": "What type is 'Hello'?",
                        "options": ["int", "str", "bool"],
                        "correct": 1
                    },
                    {
                        "question": "What type is True?",
                        "options": ["str", "int", "bool"],
                        "correct": 2
                    },
                    {
                        "question": "What does type() do?",
                        "options": ["Creates a variable", "Shows the data type of a value", "Converts data types"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 3: Integer (int)",
                "description": "Work with whole numbers and integer operations",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 20,
                "video_url": "https://www.youtube.com/watch?v=H2EJuAcrZYU",
                "content": """
# Lesson 3: Integer (int)

## What is an Integer?
An integer is a whole number (positive, negative, or zero) without a decimal point.

```python
age = 25
temperature = -10
population = 1000000
balance = 0
```

## Integer Arithmetic Operations

### Addition (+)
```python
sum = 10 + 5  # Result: 15
```

### Subtraction (-)
```python
difference = 10 - 3  # Result: 7
```

### Multiplication (*)
```python
product = 10 * 3  # Result: 30
```

### Division (/)
```python
division = 10 / 3  # Result: 3.333... (Note: returns float)
```

### Integer Division (//)
Returns the whole number part, discarding decimals.
```python
quotient = 10 // 3  # Result: 3
quotient = 15 // 4  # Result: 3
quotient = 20 // 5  # Result: 4
```

### Modulo (%)
Returns the remainder after division.
```python
remainder = 10 % 3  # Result: 1
remainder = 15 % 4  # Result: 3
remainder = 20 % 5  # Result: 0
```

## Converting Strings to Integers
```python
age_str = "25"
age = int(age_str)  # Now it's 25 (integer)
print(age + 5)      # Works! Result: 30
```
                """,
                "information": [
                    "An integer is a whole number without decimals",
                    "Can be positive, negative, or zero",
                    "+ for addition, - for subtraction, * for multiplication",
                    "/ gives float result, // gives integer result",
                    "% gives the remainder (modulo operator)",
                    "Convert strings to integers using int()"
                ],
                "steps": [
                    "Learn what integers are",
                    "Perform addition, subtraction, multiplication",
                    "Understand division / vs //",
                    "Use modulo %",
                    "Convert strings to integers"
                ],
                "quiz": [
                    {
                        "question": "What is an integer?",
                        "options": ["A decimal number", "Whole numbers without decimals", "Text data"],
                        "correct": 1
                    },
                    {
                        "question": "What is 10 // 3?",
                        "options": ["3.333", "3", "4"],
                        "correct": 1
                    },
                    {
                        "question": "Which operator gives remainder?",
                        "options": ["/", "//", "%"],
                        "correct": 2
                    },
                    {
                        "question": "How to convert '25' to int?",
                        "options": ["int('25')", "integer('25')", "to_int('25')"],
                        "correct": 0
                    }
                ]
            },
            {
                "title": "Lesson 4: Floating Point (float)",
                "description": "Work with decimal numbers",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 20,
                "video_url": "https://www.youtube.com/watch?v=7t2alSnE2-I",
                "content": """
# Lesson 4: Floating Point (float)

## What is a Float?
A float is a number with a decimal point. It can represent fractional values.

```python
height = 5.9
price = 19.99
temperature = -2.5
percentage = 95.5
```

## Float Arithmetic
```python
a = 10.5
b = 3.2

print(a + b)   # 13.7
print(a - b)   # 7.3
print(a * b)   # 33.6
print(a / b)   # 3.28125
print(a // b)  # 3.0 (still returns float)
```

## Mixing int and float
When you mix integers and floats in operations, Python automatically converts to float.

```python
x = 10        # int
y = 3.5       # float

result = x + y
print(result)        # 13.5
print(type(result))  # <class 'float'>
```

## Precision and Rounding
```python
pi = 3.141592653589793
print(pi)              # 3.141592653589793
print(round(pi, 2))    # 3.14
print(round(pi, 4))    # 3.1416
```

## Converting Strings and Integers to Float
```python
price_str = "19.99"
price = float(price_str)  # 19.99

number = 10
decimal = float(number)   # 10.0
```
                """,
                "information": [
                    "A float is a number with a decimal point",
                    "Used for measurements, prices, percentages",
                    "More memory than integers",
                    "Mixing int and float produces float",
                    "Use round() function for precision",
                    "Convert strings to float using float()"
                ],
                "steps": [
                    "Learn what decimal numbers are",
                    "Perform arithmetic with floats",
                    "Understand float precision",
                    "Round decimal values",
                    "Convert int to float"
                ],
                "quiz": [
                    {
                        "question": "What is a float?",
                        "options": ["A whole number", "A decimal number", "Text data"],
                        "correct": 1
                    },
                    {
                        "question": "What is 5 / 2?",
                        "options": ["2", "2.0", "2.5"],
                        "correct": 2
                    },
                    {
                        "question": "How to round 3.456 to 2 decimals?",
                        "options": ["round(3.456, 2)", "round(3.456)", "round(2, 3.456)"],
                        "correct": 0
                    },
                    {
                        "question": "Is 2.0 an int or float?",
                        "options": ["int", "float", "both"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 5: String (str)",
                "description": "Learn to work with text data",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 25,
                "video_url": "https://www.youtube.com/watch?v=k9TUPpGqYTo",
                "content": """
# Lesson 5: String (str)

## What is a String?
A string is text data enclosed in quotes. You can use single or double quotes.

```python
name = "Alice"
message = 'Hello World'
city = "New York"
quote = "She said 'Hi'"
```

## String Concatenation
Combine strings using the + operator:
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe
```

## String Length
Use len() to find the number of characters:
```python
text = "Python"
print(len(text))  # 6
```

## Accessing Characters
Use indexing (starting from 0) to get individual characters:
```python
word = "Python"
print(word[0])    # P
print(word[1])    # y
print(word[5])    # n
print(word[-1])   # n (last character)
print(word[-2])   # o (second from last)
```

## String Methods
```python
text = "Hello World"
print(text.upper())    # HELLO WORLD
print(text.lower())    # hello world
print(text.replace("World", "Python"))  # Hello Python
```

## F-Strings (Modern Way)
```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 25
```
                """,
                "information": [
                    "A string is text data enclosed in quotes",
                    "Can use single or double quotes",
                    "Concatenate strings with + operator",
                    "Use len() to find string length",
                    "Access characters by index (0-based)",
                    "Use string methods like .upper(), .lower()",
                    "F-strings allow embedding variables in text"
                ],
                "steps": [
                    "Learn what strings are",
                    "Create strings using quotes",
                    "Concatenate strings",
                    "Use string methods",
                    "Use f-strings"
                ],
                "quiz": [
                    {
                        "question": "What is a string?",
                        "options": ["A number", "Text data", "A variable"],
                        "correct": 1
                    },
                    {
                        "question": "What is 'Hi' + 'There'?",
                        "options": ["HiThere", "Hi There", "Error"],
                        "correct": 0
                    },
                    {
                        "question": "How to find string length?",
                        "options": ["length(string)", "len(string)", "size(string)"],
                        "correct": 1
                    },
                    {
                        "question": "What does .upper() do?",
                        "options": ["Deletes text", "Converts to uppercase", "Counts characters"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 6: Boolean (bool)",
                "description": "Understand True and False values",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 15,
                "video_url": "https://www.youtube.com/watch?v=VchuKL44s6E",
                "content": """
# Lesson 6: Boolean (bool)

## What are Booleans?
Booleans represent one of two values: True or False. They are used in logical operations and conditions.

```python
is_student = True
is_adult = False
has_license = True
```

## Comparison Operators
These operators return boolean values:

```python
age = 15

print(age > 18)    # False
print(age < 18)    # True
print(age == 15)   # True
print(age != 10)   # True
print(age >= 15)   # True
print(age <= 20)   # True
```

## Logical Operators

### and (Both must be True)
```python
age = 15
has_id = True

if age > 13 and has_id:
    print("Can attend")  # This will print
```

### or (At least one must be True)
```python
has_car = False
has_bike = True

if has_car or has_bike:
    print("Has transportation")  # This will print
```

### not (Reverses the value)
```python
is_raining = True
print(not is_raining)  # False
```

## Comparison Examples
```python
# Equal to
5 == 5     # True
5 == 3     # False

# Not equal to
5 != 3     # True
5 != 5     # False

# Greater than / Less than
10 > 5     # True
3 < 2      # False

# Greater or equal / Less or equal
5 >= 5     # True
3 <= 2     # False
```
                """,
                "information": [
                    "Booleans are True or False values",
                    "Result of comparison operations",
                    "Used in conditional statements",
                    "> means greater than, < means less than",
                    "== means equal to, != means not equal",
                    "and, or, not are logical operators",
                    "Essential for decision making in code"
                ],
                "steps": [
                    "Learn True and False",
                    "Compare values using operators",
                    "Use logical operators",
                    "Apply booleans in if statements",
                    "Understand truthy and falsy values"
                ],
                "quiz": [
                    {
                        "question": "What are boolean values?",
                        "options": ["Numbers", "True and False", "Text"],
                        "correct": 1
                    },
                    {
                        "question": "Result of 5 > 3?",
                        "options": ["True", "False", "2"],
                        "correct": 0
                    },
                    {
                        "question": "Which operator means AND?",
                        "options": ["or", "and", "&"],
                        "correct": 1
                    },
                    {
                        "question": "Is 0 True or False?",
                        "options": ["True", "False", "Both"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 7: Checking Data Types (type())",
                "description": "Use type() function to identify data types",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 15,
                "video_url": "https://www.youtube.com/watch?v=OhK7i6U2k-4",
                "content": """
# Lesson 7: Checking Data Types (type())

## The type() Function
Use type() to identify what type of data a variable contains.

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

## Why is type() Useful?
1. **Debugging** - Identify unexpected data types
2. **Validation** - Check if data is in correct format
3. **Understanding** - Learn about Python's type system
4. **Error Prevention** - Catch type issues early

## Using type() in Programs
```python
user_input = input("Enter a number: ")
print(f"Type of input: {type(user_input)}")  # <class 'str'>

# If you need it as a number, convert it
number = int(user_input)
print(f"After conversion: {type(number)}")  # <class 'int'>
```

## isinstance() Function
Another way to check types:
```python
x = 5
print(isinstance(x, int))      # True
print(isinstance(x, float))    # False
print(isinstance(x, str))      # False
```

## Common Examples
```python
print(type(5))           # <class 'int'>
print(type("5"))         # <class 'str'>
print(type(5.0))         # <class 'float'>
print(type(5 > 3))       # <class 'bool'>
print(type([1, 2, 3]))   # <class 'list'>
```
                """,
                "information": [
                    "type() function returns the data type",
                    "Returns format: <class 'typename'>",
                    "Useful for debugging and verification",
                    "helps identify type mismatches",
                    "isinstance() is another way to check types",
                    "Important for writing robust code"
                ],
                "steps": [
                    "Learn why type checking is important",
                    "Use type() function",
                    "Check types of variables",
                    "Use isinstance()",
                    "Handle different types safely"
                ],
                "quiz": [
                    {
                        "question": "What does type(5) return?",
                        "options": ["int", "<class 'int'>", "integer"],
                        "correct": 1
                    },
                    {
                        "question": "What is type of '5'?",
                        "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>"],
                        "correct": 1
                    },
                    {
                        "question": "What does isinstance(5, int) return?",
                        "options": ["5", "True", "int"],
                        "correct": 1
                    },
                    {
                        "question": "Is True an int?",
                        "options": ["Yes", "No", "Sometimes"],
                        "correct": 1
                    }
                ]
            },
            {
                "title": "Lesson 8: Type Conversion (VERY IMPORTANT)",
                "description": "Convert between different data types",
                "subject": "Python Basics",
                "difficulty": "beginner",
                "min_age": 10,
                "max_age": 18,
                "duration_minutes": 25,
                "video_url": "https://www.youtube.com/watch?v=cQT33yu9pY8",
                "content": """
# Lesson 8: Type Conversion (VERY IMPORTANT)

## Why Convert Types?
- User input is always a string
- Mathematical operations need numbers
- Combining different types requires conversion
- Displaying numbers as text

## Convert to Integer: int()
```python
# From string
age_str = "25"
age = int(age_str)
print(age + 5)  # Works! Result: 30

# From float
height_float = 5.9
height_int = int(height_float)  # 5 (truncates decimal)

# From boolean
true_value = int(True)   # 1
false_value = int(False) # 0
```

## Convert to Float: float()
```python
# From string
price_str = "19.99"
price = float(price_str)

# From integer
count = 10
decimal_count = float(count)  # 10.0

# From boolean
true_value = float(True)   # 1.0
false_value = float(False) # 0.0
```

## Convert to String: str()
```python
# From integer
age = 25
message = "I am " + str(age) + " years old"

# From float
price = 19.99
print("Price: $" + str(price))

# From boolean
is_student = True
print(str(is_student))  # "True"
```

## Common Problem & Solution
❌ **This doesn't work:**
```python
age = 25
print("My age is " + age)  # ERROR!
```

✅ **This works:**
```python
age = 25
print("My age is " + str(age))  # Works!
# Or use f-strings:
print(f"My age is {age}")  # Also works!
```

## User Input Example
```python
# User input is always a string
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int
height = float(input("Enter your height: "))  # Convert to float

print(f"{name} is {age} years old and {height}m tall")
```

## Handling Conversion Errors
```python
try:
    number = int("abc")  # This will cause an error
except ValueError:
    print("Cannot convert 'abc' to integer")
```
                """,
                "information": [
                    "Type conversion is critical in Python",
                    "int() converts strings and other types to integers",
                    "float() converts to decimal numbers",
                    "str() converts any type to string",
                    "Needed when combining different types",
                    "Common source of beginner errors",
                    "User input is always a string by default"
                ],
                "steps": [
                    "Learn why conversion is needed",
                    "Convert string to int",
                    "Convert int to float",
                    "Convert numbers to string",
                    "Handle conversion errors"
                ],
                "quiz": [
                    {
                        "question": "Convert '10' to int.",
                        "options": ["integer('10')", "int('10')", "to_int('10')"],
                        "correct": 1
                    },
                    {
                        "question": "Convert 5 to string.",
                        "options": ["string(5)", "str(5)", "to_str(5)"],
                        "correct": 1
                    },
                    {
                        "question": "What error for int('abc')?",
                        "options": ["TypeError", "ValueError", "ConversionError"],
                        "correct": 1
                    },
                    {
                        "question": "Why convert input data?",
                        "options": ["It's optional", "Input is always string", "To save memory"],
                        "correct": 1
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
        print("✅ Successfully added 8 Python Basics lessons!")
        print("\nLessons created:")
        for i, lesson_data in enumerate(lessons_data, 1):
            print(f"  {i}. {lesson_data['title']}")


if __name__ == "__main__":
    seed_python_basics_course()
