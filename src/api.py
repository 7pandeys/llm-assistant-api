from fastapi import FastAPI
from pydantic import BaseModel
from src.llm import get_llm
from src.agent import app as agent_app


app = FastAPI()

llm = get_llm()

chat_history = []
class ChatRequest(BaseModel):

    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    global chat_history

    result = agent_app.invoke(
        {
            "question": request.question,
            "chat_history": chat_history
        }
    )

    chat_history = result.get(
        "chat_history",
        chat_history
    )

    return {
        "tool": result["tool"],
        "answer": result["answer"]
    }

@app.get("/history")
def history():

    return {
        "history": chat_history
    }