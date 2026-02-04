#!/usr/bin/env python
import sys
import traceback
sys.path.insert(0, 'backend')

try:
    from app import create_app
    print("Creating app...")
    app = create_app()
    print("✓ App created successfully")
    
    with app.app_context():
        from models.book import Book
        book_count = Book.query.count()
        print(f"✓ Database connected: {book_count} books found")
        
except Exception as e:
    print(f"✗ ERROR: {e}")
    traceback.print_exc()
