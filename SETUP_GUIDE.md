# SmartEDU Setup & Troubleshooting Guide

## ✅ Completed Setup

All necessary components have been installed and configured for the SmartEDU application.

### 1. Virtual Environment
✅ **Created:** Python virtual environment at `e:\SmartEDU_Aks\venv`

### 2. Dependencies Installed
✅ **Backend Requirements:**
- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- Flask-Cors (cross-origin requests)
- python-dotenv (environment variables)
- requests (HTTP library)
- python-docx (Word document handling)
- PyPDF2 (PDF handling)
- All dependencies automatically installed successfully

### 3. Database
✅ **Populated:** Database seeded with:
- 8 books with age-appropriate recommendations
- 121 lessons across 10+ subjects:
  - Python Basics (8 lessons)
  - Advanced Python (12 lessons)
  - JavaScript (15 lessons)
  - Advanced JavaScript (14 lessons)
  - Web Development (12 lessons)
  - Advanced Web Development (12 lessons)
  - Computer Science (12 lessons)
  - Advanced Computer Science (12 lessons)
  - Artificial Intelligence (12 lessons)
  - Advanced AI (12 lessons)

### 4. API Endpoints Fixed
✅ **Chatbot Endpoint** (`POST /api/chatbot`)
- Fixed to support both book recommendations and chat messages
- Handles `age` and `interest` parameters for book recommendations
- Fallback to chat mode with `user_message` if needed

✅ **Worksheet Generator** (`POST /api/generate-worksheet`)
- Fully functional
- Accepts: subject, difficulty, numQuestions, questionType, topic

✅ **Content Analyzer** (`POST /api/analyze-content`)
- Supports both file uploads and text analysis
- Accepts: analysisType, detailLevel, optional assessment metrics

✅ **eLearning Routes** (`GET /api/lessons`)
- Retrieves all lessons with filtering support
- Includes subject and difficulty filtering

### 5. Configuration Files
✅ **Created `.env` file** with:
```
FLASK_ENV=development
FLASK_APP=backend/app.py
CORS_ORIGINS=http://localhost:3000,http://localhost:5000,http://127.0.0.1:5000,http://127.0.0.1:3000
DATABASE_URL=sqlite:///smartedu.db
SECRET_KEY=your-secret-key-change-this-in-production
```

### 6. Fixed Issues
✅ **requirements.txt** - Fixed malformed dependency (`requestspython-docx` → `requests` & `python-docx`)
✅ **Chatbot Routes** - Updated to handle book recommendations properly
✅ **CORS Configuration** - Properly configured for local development

## 🚀 How to Run

### 1. Activate Virtual Environment
```powershell
cd e:\SmartEDU_Aks
.\venv\Scripts\Activate.ps1
```

### 2. Run Flask Application
```powershell
python backend/app.py
```

The server will start at:
- http://127.0.0.1:5000 (localhost)
- http://10.0.0.66:5000 (network IP)

### 3. Access the Application
Open in browser:
- **Home:** http://localhost:5000
- **eLearning:** http://localhost:5000/elearning.html
- **AI Tools:** http://localhost:5000/ai-tools.html
- **AI Chatbot:** http://localhost:5000/chatbot.html

## 📋 Feature Summary

### AI Chatbot (`/chatbot.html`)
- **Purpose:** Book recommendations based on age and interest
- **API:** `POST /api/chatbot`
- **Features:**
  - Age-appropriate recommendations
  - Fallback database search
  - Optional Groq API integration (if API key provided)

### AI Tools (`/ai-tools.html`)
Includes two main tools:

**1. Worksheet Generator**
- Generate custom worksheets for different subjects
- Adjustable difficulty levels
- Multiple question types (Multiple Choice, Short Answer, Essay, Mixed)
- Download as HTML file

**2. Content Analyzer**
- Analyze educational content
- Supports PDF, DOCX, and text input
- Multiple analysis types (Summary, Summary with Quiz, Assessment)
- Performance tracking with answer metrics

### eLearning Platform (`/elearning.html`)
- Browse 121 lessons across 10+ subjects
- Filter by subject and difficulty level
- Search functionality
- Progress tracking (dashboard)
- Responsive design with dark mode support

## 🔧 Troubleshooting

### Issue: Server won't start
**Solution:**
1. Make sure port 5000 is not in use
2. Check that virtual environment is activated
3. Verify all dependencies are installed: `pip list`

### Issue: 404 errors for static files
**Solution:**
- Missing fonts and favicon files are non-critical
- The application will still function normally
- These are cosmetic assets (woff2 fonts, favicon.ico)

### Issue: Database errors
**Solution:**
1. Delete the database file: `rm backend/instance/database.db`
2. Reseed the database: `python backend/seed.py`

### Issue: CORS errors in browser
**Solution:**
- Check `.env` file has correct CORS_ORIGINS
- Make sure you're accessing from listed origins

## 📦 Project Structure

```
e:\SmartEDU_Aks/
├── backend/
│   ├── app.py                 # Main Flask app
│   ├── config.py              # Configuration
│   ├── requirements.txt        # Python dependencies
│   ├── seed.py                # Database seeding script
│   ├── models/                # Database models
│   │   ├── book.py
│   │   ├── lesson.py
│   │   └── user.py
│   ├── routes/                # API endpoints
│   │   ├── chatbot_routes.py
│   │   ├── ai_tools_routes.py
│   │   ├── lesson_routes.py
│   │   └── book_routes.py
│   └── services/              # Business logic
│       └── ai_service.py
├── frontend/
│   ├── index.html
│   ├── elearning.html
│   ├── ai-tools.html
│   ├── chatbot.html
│   ├── css/
│   │   ├── style.css
│   │   └── ai-tools.css
│   └── js/
│       ├── main.js
│       ├── elearning.js
│       ├── ai-tools.js
│       ├── chatbot.js
│       └── theme.js
├── venv/                      # Virtual environment
├── .env                       # Environment variables
└── test_api.py               # API test script
```

## 🔐 Security Notes

- The application uses a default SECRET_KEY in development
- **CHANGE THIS** for production deployments
- Update .env file with production values
- Consider using environment variables for sensitive data

## 📞 Support

For issues with specific endpoints, check the API test script:
```powershell
python test_api.py
```

This will verify:
- Lessons endpoint
- Chatbot endpoint
- Worksheet generation
- Content analysis
- Individual lesson retrieval

---

**Setup Date:** January 30, 2026
**Status:** ✅ Ready for Development
