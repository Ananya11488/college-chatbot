import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_response(user_message):
    try:
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
        return response.text

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
        "dbms",
        "os",
        "operating system",
        "study",
        "study plan",
        "project",
        "assignment",
        "engineering",
        "university"
    ]

    message = user_message.lower()

    return any(
        keyword in message
        for keyword in student_keywords
    )
    
    
def generate_study_plan(subject, days=7):

    if subject.lower() == "dbms":
        return """
📚 DBMS Study Plan (7 Days)

Day 1
• Introduction to DBMS
• Database Architecture

Day 2
• ER Model
• Entities, Attributes, Relationships

Day 3
• Relational Model
• Keys and Constraints

Day 4
• SQL Basics
• SELECT, INSERT, UPDATE, DELETE

Day 5
• Joins and Subqueries
• Aggregate Functions

Day 6
• Normalization
• 1NF, 2NF, 3NF, BCNF

Day 7
• Transactions
• Concurrency Control
• Revision + Practice Questions
"""

    elif subject.lower() in ["operating systems", "os"]:
        return """
💻 Operating Systems Study Plan (7 Days)

Day 1
• Introduction to OS
• Types of Operating Systems

Day 2
• Processes and Threads

Day 3
• CPU Scheduling Algorithms

Day 4
• Synchronization
• Deadlocks

Day 5
• Memory Management
• Paging and Segmentation

Day 6
• File Systems
• Disk Scheduling

Day 7
• Security Concepts
• Revision + Practice Questions
"""

    else:
        return "Study plans are currently available only for DBMS and Operating Systems."