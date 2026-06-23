from src.llm import get_llm

llm = get_llm()


from src.llm import get_llm

llm = get_llm()


def choose_tool(question):

    question_lower = question.lower()

    # Rule-based routing

    if (
            "*" in question
            or "+" in question
            or "-" in question
            or "/" in question
    ):
        return "calculator"

    if question_lower.startswith(
            "who is"
    ):
        return "wikipedia"

    if question_lower.startswith(
            "what is"
    ):
        return "llm"

    # LLM routing

    prompt = f"""
Available tools:

calculator
wikipedia
llm

Question:
{question}

Return ONLY:

calculator
wikipedia
llm
"""

    response = llm.invoke(
        prompt
    )

    tool = (
        response.content
        .strip()
        .lower()
    )

    if "calculator" in tool:
        return "calculator"

    if "wikipedia" in tool:
        return "wikipedia"

    return "llm"

def route_tool(state):

    return state["tool"]