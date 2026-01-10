import sqlite3
from datetime import datetime

def get_connection():
    return sqlite3.connect("chatbot.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_chat(user_message: str, bot_reply: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (user_message, bot_reply, timestamp) VALUES (?, ?, ?)",
        (user_message, bot_reply, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

def get_all_chats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_message, bot_reply, timestamp FROM chats ORDER BY id DESC"
    )

    rows = cursor.fetchall()
    conn.close()

    chats = []
    for row in rows:
        chats.append({
            "user_message": row[0],
            "bot_reply": row[1],
            "timestamp": row[2]
        })

    return chats

