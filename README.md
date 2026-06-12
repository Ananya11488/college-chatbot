# AI Student Assistant

An AI-powered academic assistant that helps students with subject-related queries, study planning, quiz generation, internships, placements, and career preparation.

The project started as a rule-based college chatbot and was later upgraded with Gemini AI, response caching, study planning, quiz generation, and cloud deployment.

---

## Live Demo

**Frontend:**
https://6a2c410656b5424018d97504--profound-dodol-5c1211.netlify.app/

**Backend:**
https://ai-student-assistant-backend-5uc9.onrender.com/

---

## Features

### AI Student Assistant

* Answer academic questions using Gemini AI
* Help with internships, placements, and career preparation
* Provide concise, student-friendly responses

### Study Plan Generator

* Generate structured study plans
* Currently supports:

  * DBMS
  * Operating Systems

### Quiz Generator

* Generate topic-based quizzes
* Supports DBMS and Operating Systems

### Smart Response Caching

* Frequently asked questions are cached in SQLite
* Reduces Gemini API usage
* Improves response time

### Chat History

* Stores previous conversations in SQLite
* View chat history directly from the UI

### Rule-Based Assistant

* Handles greetings and common college-related queries
* Courses
* Clubs
* Placements
* Exams

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* Gemini 2.5 Flash API

### Frontend

* HTML
* CSS
* Vanilla JavaScript

### Deployment

* Render
* Netlify

### Tools

* Git
* GitHub
* REST APIs

---

## Architecture

User
↓
Frontend (Netlify)
↓
FastAPI Backend (Render)
↓
Gemini API
↓
SQLite Cache / Chat History
↓
Response Returned to User

---

## Project Structure


college-chatbot/
├── backend/
│   ├── main.py
│   ├── ai_service.py
│   ├── database.py
│   ├── test_ai_service.py
│   ├── test_gemini.py
│   └── test_scope.py
├── frontend/
│   └── index.html
├── render.yaml
├── .gitignore
└── README.md
```

---

## Running Locally

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd college-chatbot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file inside the `backend` folder:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend will be available at:

```text
http://127.0.0.1:8000
```

### 6. Open the Frontend

Open `frontend/index.html` in your browser.

---

## Key Learnings

* Building REST APIs with FastAPI
* Integrating Generative AI APIs
* SQLite database design
* Response caching techniques
* Frontend-backend communication
* Cloud deployment using Render and Netlify
* Git branching and version control

---

## Future Improvements

* Support additional subjects
* User authentication
* Personalized study plans
* Flashcards and revision notes
* PostgreSQL database migration
* Analytics dashboard
