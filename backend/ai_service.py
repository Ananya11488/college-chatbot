import os
from dotenv import load_dotenv
import google.generativeai as genai
from database import (
    get_cached_response,
    save_cached_response
)

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_response(user_message):

    try:

        cached_answer = get_cached_response(
            user_message.lower().strip()
        )

        if cached_answer:
            print("CACHE HIT")
            return cached_answer

        print("CACHE MISS")

        prompt = f"""
You are an AI Student Assistant.

Your job is to help students with:
- Academics
- Internships
- Placements
- Career preparation
- College life

Rules:
- Give concise answers.
- Use bullet points whenever possible.
- Keep answers under 150 words unless necessary.
- Be beginner friendly.
- Avoid huge paragraphs.
- Give practical advice.
- End with one useful tip if relevant.

Student Question:
{user_message}
"""

        response = model.generate_content(prompt)

        answer = response.text

        save_cached_response(
            user_message.lower().strip(),
            answer
        )

        return answer

    except Exception:
        return (
            "⚠️ AI service is temporarily busy. "
            "Please try again in a minute."
        )

def is_student_related(user_message):
    student_keywords = [
    "college",
    "student",
    "course",
    "subject",
    "exam",
    "internship",
    "placement",
    "job",
    "career",
    "resume",
    "interview",
    "cgpa",
    "gpa",

    # DBMS
    "dbms",
    "database",
    "sql",
    "normalization",
    "er model",
    "transaction",
    "concurrency",
    "indexing",

    # OS
    "os",
    "operating system",
    "process",
    "thread",
    "deadlock",
    "paging",
    "segmentation",
    "scheduling",
    "memory management",

    # General academics
    "study",
    "study plan",
    "project",
    "assignment",
    "engineering",
    "university",
    "semester",
    "syllabus"
]

    message = user_message.lower()

    return any(
        keyword in message
        for keyword in student_keywords
    )
 
def generate_study_plan(subject, days=7):

    try:
        prompt = f"""
You are an academic tutor.

Create a {days}-day study plan for {subject}.

Rules:
- Day-wise format
- Maximum 3 topics per day
- Exam-oriented
- Beginner-friendly
- Use markdown headings
- Keep it concise
- Include revision on the last day

Example:

## Day 1
- Topic 1
- Topic 2

## Day 2
- Topic 1
- Topic 2
"""

        response = model.generate_content(prompt)

        return f"📚 {subject} Study Plan\n\n" + response.text

    except Exception:
        return (
            "⚠️ Unable to generate study plan right now. "
            "Please try again later."
        )
    
def generate_quiz(subject):

    try:

        prompt = f"""
Generate a quiz on {subject}.

Rules:
- 5 multiple choice questions
- 4 options per question
- Show correct answer after each question
- Exam oriented
- Use markdown formatting
"""

        response = model.generate_content(prompt)

        return f"📝 {subject} Quiz\n\n" + response.text

    except Exception:
        return (
            "⚠️ Unable to generate quiz right now."
        )    