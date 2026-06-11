from fastapi.middleware.cors import CORSMiddleware

from database import create_table, save_chat, get_all_chats
from ai_service import (
    get_ai_response,
    is_student_related,
    generate_study_plan,
    generate_quiz

)
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_table()


@app.get("/")
def read_root():
    return {"message": "Hello Ananya, welcome to your chatbot backend!"}

@app.get("/info")
def get_info():
    return {
        "name": "College Assistant Chatbot",
        "version": "1.0",
        "description": "Helps students with college-related queries"
    }

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
INTENTS = {
    
    "courses": ["course", "degree", "program", "subject"],
    "exams": ["exam", "test", "midsem", "endsem"],
    "clubs": ["club", "society", "activity"],
    "placements": ["placement", "job", "internship"]
}
def detect_intent(message: str):
    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in message:
                return intent
    return None

def generate_reply(user_message: str) -> str:
    # Greeting should be short messages only
    if user_message.strip() in ["hi", "hello", "hey"]:
        return "Hi! 😊 How can I help you today?"

    intent = detect_intent(user_message)

    if intent == "courses":
        return "We offer CS, IT, and AI programs with a strong practical focus."

    elif intent == "exams":
        return "Exams usually start from mid-March. The detailed schedule will be shared soon."

    elif intent == "clubs":
        return "We have music, dance, fashion, coding, and drama clubs."

    elif intent == "placements":
        return "Our placement cell supports internships and full-time roles with top companies."

    else:
        return "I'm not sure about that yet 🤔 Try asking about courses, exams, clubs, or placements."



@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    message_lower = user_message.lower()
    
    if "quiz" in message_lower:

        if "dbms" in message_lower:
            reply = generate_quiz("DBMS")

        elif "os" in message_lower or "operating system" in message_lower:
            reply = generate_quiz("Operating Systems")

        else:
            reply = (
               "Currently I can generate quizzes for "
               "DBMS and Operating Systems."
            )

    elif "study plan" in message_lower:

        if "dbms" in message_lower:
            reply = generate_study_plan("DBMS")

        elif "os" in message_lower or "operating system" in message_lower:
            reply = generate_study_plan("Operating Systems")

        else:
            reply = (
                "Currently I can create study plans for "
                "DBMS and Operating Systems."
            )
    

    else:

        basic_reply = generate_reply(message_lower)

        if "I'm not sure about that yet" not in basic_reply:
            reply = basic_reply

        elif is_student_related(user_message):
            reply = get_ai_response(user_message)

        else:
            reply = (
                "I'm designed to help with academics, internships, "
                "placements, college life, career preparation, "
                "DBMS, and Operating Systems. 🎓"
            )

    save_chat(user_message, reply)

    return {"reply": reply}
@app.get("/history")
def get_chat_history():
    return get_all_chats()




