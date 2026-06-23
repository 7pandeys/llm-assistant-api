from dotenv import load_dotenv

# from langchain_google_genai import (
#     ChatGoogleGenerativeAI
# )

load_dotenv()

# def get_llm():
#
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         temperature=0
#     )

from langchain_ollama import ChatOllama

def get_llm():
    return ChatOllama(
        model="qwen"
    )