"""
Seed Advanced Artificial Intelligence course lessons into the database.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from extensions import db
from models.lesson import Lesson

def seed_advanced_artificial_intelligence():
    """Seed Advanced Artificial Intelligence lessons"""
    
    app = create_app()
    
    lessons_data = [
        {
            "title": "AI System Design & Architecture",
            "description": "Learn how to design and architect production AI systems.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=JMUxmLyrhSk",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Understand AI system components, data pipeline, model training, and deployment strategies.",
            "steps": ["Understand AI system components", "Learn data → model → deployment flow", "Centralized vs distributed AI", "Online vs offline inference", "Real-world AI system examples"],
            "quiz": [
                {"question": "AI system includes?", "answer": "Data, model, compute"},
                {"question": "Inference means?", "answer": "Making predictions"},
                {"question": "Deployment is?", "answer": "Making model live"},
                {"question": "Distributed AI means?", "answer": "AI across multiple systems"}
            ]
        },
        {
            "title": "Advanced Machine Learning Concepts",
            "description": "Master advanced ML concepts for better model performance.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=ukzFI9rgwfU",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Learn bias-variance tradeoff, overfitting, underfitting, cross-validation, and model generalization.",
            "steps": ["Bias vs variance", "Overfitting and underfitting", "Train/validation/test split", "Cross-validation concept", "Model generalization"],
            "quiz": [
                {"question": "Overfitting means?", "answer": "Learns noise"},
                {"question": "Underfitting means?", "answer": "Learns too little"},
                {"question": "Validation set used for?", "answer": "Model tuning"},
                {"question": "Good model does?", "answer": "Generalizes well"}
            ]
        },
        {
            "title": "Feature Engineering & Data Preprocessing",
            "description": "Learn to engineer powerful features and preprocess data effectively.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=ua-CiDNNj30",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Master feature selection, scaling, handling missing data, and categorical encoding.",
            "steps": ["Understand features", "Feature selection", "Feature scaling", "Handling missing data", "Encoding categorical data"],
            "quiz": [
                {"question": "Feature is?", "answer": "Input variable"},
                {"question": "Scaling helps?", "answer": "Faster learning"},
                {"question": "Missing data handled by?", "answer": "Remove or fill"},
                {"question": "Encoding converts?", "answer": "Text to numbers"}
            ]
        },
        {
            "title": "Model Evaluation & Metrics",
            "description": "Learn to properly evaluate ML models with appropriate metrics.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=4jRBRDbJemM",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 26,
            "information": "Understand accuracy, precision, recall, confusion matrix, ROC curves, and AUC metrics.",
            "steps": ["Classification vs regression metrics", "Accuracy limitations", "Precision & recall", "Confusion matrix", "ROC & AUC basics"],
            "quiz": [
                {"question": "Accuracy measures?", "answer": "Correct predictions"},
                {"question": "Precision focuses on?", "answer": "False positives"},
                {"question": "Recall focuses on?", "answer": "False negatives"},
                {"question": "Confusion matrix shows?", "answer": "Prediction breakdown"}
            ]
        },
        {
            "title": "Deep Learning Fundamentals",
            "description": "Master the foundations of deep learning and neural networks.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=aircAruvnKk",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 34,
            "information": "Learn deep networks, activation functions, loss functions, backpropagation, and training strategies.",
            "steps": ["Deep vs shallow networks", "Activation functions", "Loss functions", "Backpropagation intuition", "Training deep models"],
            "quiz": [
                {"question": "Deep learning uses?", "answer": "Neural networks"},
                {"question": "Activation function purpose?", "answer": "Non-linearity"},
                {"question": "Loss function measures?", "answer": "Error"},
                {"question": "Backpropagation updates?", "answer": "Weights"}
            ]
        },
        {
            "title": "Convolutional Neural Networks (CNNs)",
            "description": "Master CNNs for image processing and computer vision tasks.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=YRhxdVk_sIs",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 31,
            "information": "Learn image tensors, convolution operations, pooling, CNN architectures, and image classification.",
            "steps": ["Understand image tensors", "Learn convolution operation", "Pooling layers", "CNN architecture", "Image classification flow"],
            "quiz": [
                {"question": "CNN used for?", "answer": "Images"},
                {"question": "Convolution extracts?", "answer": "Features"},
                {"question": "Pooling reduces?", "answer": "Spatial size"},
                {"question": "CNN input is?", "answer": "Pixel data"}
            ]
        },
        {
            "title": "Natural Language Processing (Advanced)",
            "description": "Advanced NLP techniques for text understanding and processing.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=CMrHM8a3hqw",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 33,
            "information": "Learn word embeddings, sequence modeling, sentiment analysis, and text classification pipelines.",
            "steps": ["Word embeddings", "Bag of Words vs embeddings", "Sequence modeling", "Sentiment analysis", "Text classification pipelines"],
            "quiz": [
                {"question": "Embeddings represent?", "answer": "Meaning of words"},
                {"question": "NLP deals with?", "answer": "Language"},
                {"question": "Sequence means?", "answer": "Ordered data"},
                {"question": "NLP task example?", "answer": "Sentiment analysis"}
            ]
        },
        {
            "title": "Transformers & Large Language Models (LLMs)",
            "description": "Understand transformers and state-of-the-art large language models.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=wjZofJX0v4M",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 35,
            "information": "Learn attention mechanisms, transformer architecture, LLM training, and applications like ChatGPT.",
            "steps": ["Why transformers were created", "Attention mechanism", "Encoder–decoder concept", "LLM training overview", "Real-world LLM use cases"],
            "quiz": [
                {"question": "Transformers use?", "answer": "Self-attention"},
                {"question": "Attention focuses on?", "answer": "Relevant context"},
                {"question": "LLM trained on?", "answer": "Large text data"},
                {"question": "LLM example?", "answer": "ChatGPT"}
            ]
        },
        {
            "title": "Reinforcement Learning (Advanced Intro)",
            "description": "Learn advanced reinforcement learning concepts and algorithms.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=2pWv7GOvuf0",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 32,
            "information": "Master agent-environment interactions, rewards, exploration-exploitation, and policy learning.",
            "steps": ["Agent–environment setup", "States, actions, rewards", "Exploration vs exploitation", "Policy learning", "Real-world RL examples"],
            "quiz": [
                {"question": "RL agent learns by?", "answer": "Trial and error"},
                {"question": "Reward means?", "answer": "Feedback signal"},
                {"question": "Exploration is?", "answer": "Trying new actions"},
                {"question": "RL example?", "answer": "Game AI"}
            ]
        },
        {
            "title": "AI Deployment & MLOps",
            "description": "Learn to deploy AI models and manage ML operations in production.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=1nxzOr6d0_c",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 30,
            "information": "Understand model serving, APIs, versioning, monitoring, and continuous improvement strategies.",
            "steps": ["Model serving basics", "APIs for AI", "Model versioning", "Monitoring models", "Continuous improvement"],
            "quiz": [
                {"question": "MLOps combines?", "answer": "ML + DevOps"},
                {"question": "Model drift means?", "answer": "Performance drop"},
                {"question": "API does?", "answer": "Connect systems"},
                {"question": "Monitoring checks?", "answer": "Accuracy & errors"}
            ]
        },
        {
            "title": "AI Security, Privacy & Ethics (Advanced)",
            "description": "Master security, privacy, and ethical considerations in AI systems.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=V6G5f3XzJkA",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 28,
            "information": "Learn adversarial attacks, data leakage, model explainability, fairness, and compliance.",
            "steps": ["Adversarial attacks", "Data leakage risks", "Model explainability", "Fairness & bias control", "Regulations & compliance"],
            "quiz": [
                {"question": "Adversarial attack is?", "answer": "Fooling AI models"},
                {"question": "Explainability means?", "answer": "Understanding decisions"},
                {"question": "Bias causes?", "answer": "Unfair outcomes"},
                {"question": "Privacy protects?", "answer": "User data"}
            ]
        },
        {
            "title": "Building Advanced AI Projects & Career Path",
            "description": "Learn to build end-to-end AI projects and advance your AI career.",
            "subject": "Artificial Intelligence",
            "difficulty": "Advanced",
            "video_url": "https://www.youtube.com/watch?v=JMUxmLyrhSk",
            "min_age": 15,
            "max_age": 100,
            "duration_minutes": 29,
            "information": "Master end-to-end AI project development, portfolio building, and career advancement strategies.",
            "steps": ["Choose real-world problem", "Design end-to-end AI system", "Train & evaluate model", "Deploy project", "Prepare AI portfolio"],
            "quiz": [
                {"question": "AI project starts with?", "answer": "Problem definition"},
                {"question": "End-to-end means?", "answer": "Data → deployment"},
                {"question": "Portfolio helps?", "answer": "Job readiness"},
                {"question": "AI career example?", "answer": "AI engineer"}
            ]
        }
    ]
    
    with app.app_context():
        try:
            # Check if advanced AI lessons already exist
            existing = db.session.query(Lesson).filter(
                Lesson.subject == "Artificial Intelligence",
                Lesson.difficulty == "Advanced"
            ).first()
            
            if existing:
                print("Advanced Artificial Intelligence lessons already exist in database. Skipping seeding.")
                return
            
            # Add all lessons
            for lesson_data in lessons_data:
                lesson = Lesson(
                    title=lesson_data["title"],
                    description=lesson_data["description"],
                    subject=lesson_data["subject"],
                    difficulty=lesson_data["difficulty"],
                    video_url=lesson_data["video_url"],
                    min_age=lesson_data["min_age"],
                    max_age=lesson_data["max_age"],
                    duration_minutes=lesson_data["duration_minutes"],
                    information=lesson_data["information"],
                    steps=lesson_data["steps"],
                    quiz=lesson_data["quiz"]
                )
                db.session.add(lesson)
            
            db.session.commit()
            print(f"✅ Successfully added {len(lessons_data)} Advanced Artificial Intelligence lessons!")
            for lesson_data in lessons_data:
                print(f"   ✓ {lesson_data['title']}")
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding lessons: {str(e)}")
            raise

if __name__ == "__main__":
    seed_advanced_artificial_intelligence()
