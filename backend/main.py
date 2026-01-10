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


