# SmartEDU - Quick Commands

## ✅ Start the Application

```powershell
cd e:\SmartEDU_Aks
python backend/app.py
```

**Server will be at:** http://localhost:5000

## 🌐 Access Points

| Feature | URL |
|---------|-----|
| Home | http://localhost:5000 |
| eLearning | http://localhost:5000/elearning.html |
| AI Chatbot | http://localhost:5000/chatbot.html |
| AI Tools | http://localhost:5000/ai-tools.html |
| Login | http://localhost:5000/login.html |
| Sign Up | http://localhost:5000/signup.html |

## 🔄 Rebuild Database

If you need to reset the database:

```powershell
cd e:\SmartEDU_Aks
python backend/seed.py
```

This will:
- Clear existing data
- Add 8 books
- Add 121 lessons
- Add 4 test users

## 🧪 Test API Endpoints

```powershell
cd e:\SmartEDU_Aks
python test_api.py
```

## ⚙️ Environment Setup

Virtual environment is at: `e:\SmartEDU_Aks\venv`

To manually activate:
```powershell
.\venv\Scripts\Activate.ps1
```

## 📋 File Structure

```
e:\SmartEDU_Aks/
├── backend/              # Flask backend
├── frontend/            # HTML/CSS/JS frontend
├── venv/               # Virtual environment
├── instance/           # Database folder
├── .env               # Configuration
└── FIXES_APPLIED.md   # This file
```

## ❌ If Server Stops

1. Check if port 5000 is in use
2. Restart: `python backend/app.py`
3. Check `.env` file for configuration

## 🆘 Database Issues

If you get database errors:

```powershell
# Delete old database
Remove-Item e:\SmartEDU_Aks\instance\* -ErrorAction SilentlyContinue

# Reseed
python backend/seed.py

# Restart server
python backend/app.py
```

---

**Everything should now work perfectly!** ✅
