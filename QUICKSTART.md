# 🚀 Quick Start Guide - SmartEDU

## 1️⃣ Activate Virtual Environment

```powershell
cd e:\SmartEDU_Aks
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` in your PowerShell prompt.

## 2️⃣ Start the Server

```powershell
python backend/app.py
```

You'll see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

## 3️⃣ Open in Browser

Visit these URLs:

| Feature | URL |
|---------|-----|
| 🏠 Home | http://localhost:5000 |
| 📚 eLearning | http://localhost:5000/elearning.html |
| 🤖 AI Chatbot | http://localhost:5000/chatbot.html |
| ✨ AI Tools | http://localhost:5000/ai-tools.html |

## ✅ What's Fixed

### AI Chatbot (`/chatbot.html`)
- ✅ Book recommendations by age and interest
- ✅ Displays AI-powered suggestions
- ✅ All 8 sample books loaded from database

### AI Tools (`/ai-tools.html`)
**Worksheet Generator:**
- ✅ Create custom worksheets
- ✅ Choose subject, difficulty, question type
- ✅ Download as HTML file

**Content Analyzer:**
- ✅ Paste text or upload files (PDF, DOCX, TXT)
- ✅ Get AI analysis and summaries
- ✅ Generate quiz questions
- ✅ Track assessment performance

### eLearning (`/elearning.html`)
- ✅ Browse 121 lessons across 10+ subjects
- ✅ Search and filter by subject/difficulty
- ✅ View course details

## 🧪 Test the API

Run the test script to verify all endpoints:
```powershell
python test_api.py
```

## 🛑 Stop the Server

Press `CTRL+C` in the terminal where the server is running.

## ❓ Troubleshooting

**Server won't start?**
- Make sure port 5000 is not in use
- Check that virtual environment is activated
- Run: `pip list` to verify dependencies

**404 errors for static files?**
- This is normal - non-critical assets (fonts, favicon)
- Application still works correctly

**Database issues?**
```powershell
python backend/seed.py
```
This will recreate the database with all lessons and books.

## 📚 Sample Data

The application comes pre-loaded with:
- **121 Lessons** across Python, JavaScript, Web Dev, Computer Science, AI
- **8 Books** for age-appropriate recommendations (ages 5-18)
- **4 Test Users** for authentication testing

## 🎯 Next Steps

1. Click "eLearning" to browse available courses
2. Try the "AI Chatbot" to get book recommendations
3. Test "Worksheet Generator" to create a custom worksheet
4. Use "Content Analyzer" to analyze educational materials

---

**Happy Learning! 🎓**
