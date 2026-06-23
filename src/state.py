from typing import TypedDict


class AgentState(TypedDict):

    question: str

    chat_history: list

    tool: str

    answer: str