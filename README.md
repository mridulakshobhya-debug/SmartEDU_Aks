# 📚 SmartEDU - Safe, Age-Aware Learning Platform Unh

An intelligent educational platform that provides age-appropriate learning content and book recommendations using AI.

## ✨ Features

- **🎓 Interactive Learning**: Structured lessons across multiple subjects
- **📖 Digital Library**: Age-filtered book recommendations
- **🤖 AI Chatbot**: Personalized recommendations using Groq API
- **🔐 Age Guard**: Content filtering based on user age
- **🌙 Professional UI**: Modern, responsive design with dark mode support
- **⚡ RESTful API**: Clean, well-documented backend API

## 📋 Project Structure

```
smartedu/
├── backend/                    # Flask API server
│   ├── app.py                 # Application factory
│   ├── config.py              # Configuration management
│   ├── extensions.py          # SQLAlchemy setup
│   ├── requirements.txt        # Python dependencies
│   ├── seed.py                # Database seeding script
│   ├── .env                   # Environment variables
│   ├── models/                # Database models
│   ├── routes/                # API endpoints
│   └── services/              # Business logic
│
└── frontend/                  # HTML/CSS/JS frontend
    ├── index.html             # Home page
    ├── elearning.html         # Learning section
    ├── elibrary.html          # Book library & AI chatbot
    ├── css/
    │   └── style.css          # Professional styling
    └── js/
        ├── main.js            # App initialization
        ├── elearning.js       # Lesson loading logic
        ├── chatbot.js         # AI recommendation UI
        └── elibrary.js        # Book management
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Backend Setup

```bash
# Navigate to backend directory
cd smartedu/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Edit .env file and add your Groq API key
# GROQ_API_KEY=your_actual_api_key_here
```

### 2. Seed Database with Demo Data

```bash
# From backend directory (with venv activated)
python seed.py
```

This populates the database with:
- 8 sample books across various genres
- 6 sample lessons on different subjects
- 4 sample users

### 3. Run the Server

```bash
# From backend directory (with venv activated)
python app.py
```

The application will be available at `http://localhost:5000`

## 📖 API Endpoints

### Books
- `GET /api/books?age=12` - Get age-appropriate books
- `GET /api/books/<id>` - Get specific book details

### Lessons
- `GET /api/lessons?age=12` - Get age-appropriate lessons
- `GET /api/lessons?age=12&subject=Programming` - Filter by subject
- `GET /api/lessons?age=12&difficulty=beginner` - Filter by difficulty
- `GET /api/lessons/<id>` - Get specific lesson details

### Chatbot
- `POST /api/chatbot` - Get AI-powered recommendations
  ```json
  {
    "age": 12,
    "interest": "science fiction"
  }
  ```

## 🎨 Frontend Pages

### Home (index.html)
- Hero section with call-to-action
- Features overview
- Statistics showcase
- Professional layout

### eLearning (elearning.html)
- Interactive lesson browsing
- Age-based filtering
- Difficulty levels
- Subject categorization

### eLibrary (elibrary.html)
- Book recommendations
- AI chatbot integration
- Interest-based search
- Personalized suggestions

## ⚙️ Configuration

### Environment Variables (.env)

```env
# API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Database
DATABASE_URL=sqlite:///database.db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Flask
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key_here_change_in_production

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5000
```

## 🛠️ Technology Stack

### Backend
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM
- **Flask-CORS** - Cross-origin support
- **Groq API** - AI recommendations
- **SQLite** - Database

### Frontend
- **HTML5** - Markup
- **CSS3** - Professional styling
- **Vanilla JavaScript** - Interactivity
- **Responsive Design** - Mobile-friendly

## 🔒 Age Guard System

Content is filtered based on age ranges:
- Books and lessons have `min_age` and `max_age` fields
- Users only see age-appropriate content
- Flexible ranges accommodate different content types

## 🤖 AI Integration

The chatbot uses **Groq's LLaMA API** for intelligent recommendations:
- Falls back to database if API unavailable
- Context-aware suggestions
- Age-appropriate filtering
- Personalized responses

## 🧪 Testing

```bash
# Run with test config
export FLASK_ENV=testing
python app.py
```

## 📝 Database Models

### User
- `id` - Primary key
- `age` - User's age (5-100)
- `created_at`, `updated_at` - Timestamps

### Book
- `title`, `author`, `description`
- `min_age`, `max_age` - Age range
- `category` - Genre/category
- `content` - Book text
- `cover_url` - Cover image

### Lesson
- `title`, `description`, `content`
- `subject` - Subject area
- `difficulty` - Level (beginner/intermediate/advanced)
- `min_age`, `max_age` - Age range
- `duration_minutes` - Lesson length

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
gunicorn wsgi:app
```

## 📊 Project Statistics

- **8 Demo Books** - Various genres
- **6 Sample Lessons** - Multiple subjects
- **Professional CSS** - 600+ lines of styling
- **RESTful API** - 8 endpoints
- **Error Handling** - Comprehensive validation

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 standards
- Database models have proper validation
- API endpoints include error handling
- Frontend is responsive and accessible

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Database Issues
```bash
# Reset database
rm database.db
python seed.py
```

### Port Already in Use
```bash
# Run on different port
export FLASK_ENV=development
python app.py --port 5001
```

### CORS Errors
Update `CORS_ORIGINS` in `.env` to include your frontend URL

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Made with ❤️ for Safe, Accessible Learning**
