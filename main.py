from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import chatbot_reply
from chatbot import databaseServices


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.get("/")
def home():
    return {"status": "chatbot backend is running"}

@app.get("/debug/bookings")
def show_bookings():
    return databaseServices

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chatbot_reply(request.session_id,request.message)
    return {"reply": reply}