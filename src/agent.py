from src.router import choose_tool
from src.tools import calculator
from src.wiki_tool import search_wikipedia
from src.llm import get_llm
from src.router import route_tool
from src.state import AgentState
def router_node(state):

    tool = choose_tool(
        state["question"]
    )

    print(
        f"Question: {state['question']}"
    )

    print(
        f"Chosen Tool: {tool}"
    )

    return {
        **state,
        "tool": tool
    }

llm = get_llm()


# def tool_node(state):
#
#     question = state["question"]
#
#     if state["tool"] == "calculator":
#
#         answer = calculator(
#             question
#         )
#
#     elif state["tool"] == "wikipedia":
#
#         answer = search_wikipedia(
#             question
#         )
#
#     else:
#
#         # answer = llm.invoke(
#         #     question
#         # ).content
#         messages = (
#             state["chat_history"]
#         )
#
#         response = llm.invoke(
#             messages
#         )
#
#         answer = response.content
#
#     return {
#         **state,
#         "answer": answer
#     }

from langgraph.graph import (
    StateGraph,
    END
)


def memory_node(state):

    history = state.get(
        "chat_history",
        []
    )

    history.append(
        (
            "human",
            state["question"]
        )
    )

    return {
        **state,
        "chat_history": history
    }

def calculator_node(state):

    answer = calculator(
        state["question"]
    )

    return {
        **state,
        "answer": answer
    }

def wikipedia_node(state):

    answer = search_wikipedia(
        state["question"]
    )

    return {
        **state,
        "answer": answer
    }

def llm_node(state):

    response = llm.invoke(
        state["question"]
    )

    return {
        **state,
        "answer":
        response.content
    }


graph = StateGraph(
    AgentState
)

# add nodes
graph.add_node("router", router_node)
graph.add_node("calculator", calculator_node)
graph.add_node("wikipedia", wikipedia_node)
graph.add_node("llm", llm_node)

# entry point
graph.add_node(
    "memory",
    memory_node
)

graph.set_entry_point(
    "memory"
)

graph.add_edge(
    "memory",
    "router"
)

# conditional routing
graph.add_conditional_edges(
    "router",
    route_tool,
    {
        "calculator": "calculator",
        "wikipedia": "wikipedia",
        "llm": "llm"
    }
)

# terminal edges
graph.add_edge("calculator", END)
graph.add_edge("wikipedia", END)
graph.add_edge("llm", END)

# COMPILE LAST
app = graph.compile()

