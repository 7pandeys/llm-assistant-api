from src.agent import app

response = app.invoke(
    {
        "question":
        "145 * 89"
    }
)

print(response)