from src.agent import app

history = []

response1 = app.invoke(
    {
        "question":
        "Who is Sachin Tendulkar?",

        "chat_history":
        history
    }
)

history = response1[
    "chat_history"
]

response2 = app.invoke(
    {
        "question":
        "How many centuries did he score?",

        "chat_history":
        history
    }
)

print(
    response2["answer"]
)