from fastapi import FastAPI

app = FastAPI()

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

def generate_reply(user_message: str) -> str:
    if "exam" in user_message:
        return "Exams start from 15th March."
    elif "course" in user_message:
        return "We offer CS, IT, and AI courses."
    elif "club" in user_message:
        return "We have music, dance, fashion, and coding clubs."
    else:
        return "Sorry, I didn’t understand that. Try asking about exams, courses, or clubs."


@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()
    reply = generate_reply(user_message)
    return {"reply": reply}




