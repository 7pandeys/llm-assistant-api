# LLM Assistant API

## Overview

LLM Assistant API is a FastAPI-based AI Agent built using LangGraph and Ollama.

The project demonstrates:

* LLM Integration
* Tool Calling
* Memory
* LangGraph Workflows
* Conditional Routing
* FastAPI Deployment
* Docker Containerization
* CI/CD using GitHub Actions

---

## Architecture

User
↓
FastAPI
↓
LangGraph Agent
↓
Memory Node
↓
Router Node

├── Calculator Tool

├── Wikipedia Tool

└── LLM

↓

Response

---

## Tech Stack

### AI

* LangGraph
* LangChain
* Ollama
* Qwen

### Backend

* FastAPI
* Pydantic

### DevOps

* Docker
* GitHub Actions
* Poetry

---

## Features

### Chat API

Users can interact with the assistant using a REST API.

### Conversation Memory

The assistant maintains chat history across interactions.

### Calculator Tool

Handles arithmetic calculations.

Example:

145 * 89

Output:

12905

### Wikipedia Tool

Retrieves information about people and entities.

Example:

Who is Sachin Tendulkar?

### LangGraph Agent

The workflow is implemented using LangGraph nodes and conditional routing.

---

## Project Structure

```text
llm-assistant-api

├── src
│   ├── api.py
│   ├── agent.py
│   ├── llm.py
│   ├── router.py
│   ├── state.py
│   ├── tools.py
│   └── wiki_tool.py
│
├── tests
│   ├── test_router.py
│   ├── test_agent.py
│   ├── test_memory_agent.py
│   └── test_conditional_agent.py
│
├── Dockerfile
├── pyproject.toml
└── README.md
```

---

## LangGraph Workflow

Memory Node
↓
Router Node

├── Calculator Node

├── Wikipedia Node

└── LLM Node

↓

END

---

## API Endpoints

### Chat

POST /chat

Request

```json
{
  "question": "145 * 89"
}
```

Response

```json
{
  "tool": "calculator",
  "answer": "12905"
}
```

---

### History

GET /history

Response

```json
{
  "history": [
    [
      "human",
      "Who is Sachin Tendulkar?"
    ],
    [
      "ai",
      "Sachin Tendulkar is..."
    ]
  ]
}
```

---

## Running Locally

Install dependencies

```bash
poetry install
```

Run API

```bash
poetry run uvicorn src.api:app --reload
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Docker

Build image

```bash
docker build -t llm-assistant-api .
```

Run container

```bash
docker run -p 8000:8000 llm-assistant-api
```

---

## CI/CD

GitHub Actions automatically:

* Installs dependencies
* Runs tests
* Builds Docker image

---

## Future Improvements

* Redis-based Memory
* Multi-Agent Workflows
* RAG Integration
* Vector Database
* Tool Calling using Native LangGraph Tools
* Kubernetes Deployment
* LangSmith Observability

---

## Key Learnings

* LangGraph
* Agent Architecture
* Tool Calling
* Conditional Routing
* Memory Management
* FastAPI
* Docker
* GitHub Actions
* AI Engineering Fundamentals

---

## Author

Sandeep Pandey

Data Engineer | AI Engineer | MLOps Enthusiast
