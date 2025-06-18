
# 🤖 Study Buddy Matching with AI

An AI-powered backend system that intelligently pairs students with suitable study partners based on their study goals, preferred time, learning type, and personality traits. Built with **FastAPI**, this project enables seamless and customizable matching through a RESTful API.

---

## 🚀 Features

- ✅ Matches students based on:
  - Study goal
  - Preferred study time
  - Study type (reading, video, group, etc.)
  - Personality traits (collaborative, adaptive, etc.)
- ⚡ FastAPI-powered backend
- 📦 JSON-based student data and config
- 📩 Simple and extendable matching logic
- 🐳 Docker support for deployment

---
## 📁 Folder Structure
study-buddy/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI endpoints
│ ├── matcher.py # Matching logic
│ └── pycache/
├── data/
│ └── students.json # Sample student data
├── tests/ # (Optional) For unit tests
├── config.json # Configuration file
├── Dockerfile # For containerization
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── schema.json # JSON schema for validation
## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the server with:

```bash
uvicorn app.main:app --reload
```

Then open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Sample API Request

**Endpoint:** `POST /match`

**Request Body:**

```json
{
  "student_id": "stu_1001",
  "goal": "Master Data Science",
  "preferred_study_time": "early_morning",
  "study_type": "reading",
  "personality": ["collaborative", "adaptive"]
}
```

**Sample Response:**

```json
{
  "matched_with": "stu_1004",
  "compatibility_score": 87
}
```

---

## 🐳 Docker Support

To build and run the Docker container:

```bash
docker build -t study-buddy .
docker run -p 8000:8000 study-buddy
```

---

## 🔮 Future Improvements

- Frontend integration
- ML-based intelligent matching
- Match history and feedback loop
- Authentication system

---

## 📄 License

MIT License

---

## 👩‍💻 Author

**Ashritha Penke**  
[LinkedIn](https://www.linkedin.com/in/ashritha-penke-385560259)  
[GitHub](https://github.com)
