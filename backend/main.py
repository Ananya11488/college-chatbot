from fastapi.middleware.cors import CORSMiddleware

from database import create_table, save_chat, get_all_chats

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

    save_chat(user_message, reply)

    return {"reply": reply}
@app.get("/history")
def get_chat_history():
    return get_all_chats()





