from app import create_app
from models.lesson import Lesson
from extensions import db

app = create_app()
with app.app_context():
    lessons = db.session.query(Lesson).all()
    subjects = {}
    
    for lesson in lessons:
        if lesson.subject not in subjects:
            subjects[lesson.subject] = {'Beginner': 0, 'Intermediate': 0, 'Advanced': 0, 'beginner': 0, 'intermediate': 0, 'advanced': 0}
        subjects[lesson.subject][lesson.difficulty] += 1
    
    print("\n" + "="*60)
    print("   SMARTEDU LMS PLATFORM - COMPLETE COURSE LIBRARY 2026")
    print("="*60 + "\n")
    
    for subj in sorted(subjects.keys()):
        print(f"📚 {subj}")
        counts = subjects[subj]
        if counts['Beginner'] > 0:
            print(f"   └─ Beginner: {counts['Beginner']} lessons")
        if counts['beginner'] > 0:
            print(f"   └─ beginner: {counts['beginner']} lessons")
        if counts['Intermediate'] > 0:
            print(f"   └─ Intermediate: {counts['Intermediate']} lessons")
        if counts['intermediate'] > 0:
            print(f"   └─ intermediate: {counts['intermediate']} lessons")
        if counts['Advanced'] > 0:
            print(f"   └─ Advanced: {counts['Advanced']} lessons")
        if counts['advanced'] > 0:
            print(f"   └─ advanced: {counts['advanced']} lessons")
        print()
    
    print("📊 PLATFORM SUMMARY:")
    print(f"   ├─ Total Lessons: {len(lessons)}")
    print(f"   ├─ Total Courses: {len(subjects)}")
    print(f"   └─ Age Range: 12-100 years")
    print("\n" + "="*60 + "\n")
