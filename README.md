# LangGraph Learning Repository

A hands-on collection of **LangGraph** notebooks and projects exploring stateful, multi-agent workflows built on top of LangChain. This repo covers everything from basic graph workflows to advanced chatbots, RAG pipelines, and MCP (Model Context Protocol) integration.

## Overview

LangGraph extends LangChain by enabling cyclical, stateful computation graphs — making it ideal for building agentic AI systems, multi-step reasoning pipelines, and conversational agents with memory.

## Contents

| File / Folder | Description |
|---|---|
| `0_test_installation.ipynb` | Environment setup and installation verification |
| `1_bmi_workflow.ipynb` | Simple BMI calculator workflow |
| `2_simple_llm_workflow.ipynb` | Basic LLM node in a LangGraph |
| `3_prompt_chaining.ipynb` | Prompt chaining with multiple nodes |
| `4_batsman_workflow.ipynb` | Sports stats agentic workflow |
| `5_UPSC_essay_workflow.ipynb` | Essay generation pipeline |
| `6_quadratic_equation_workflow.ipynb` | Math problem-solving workflow |
| `7_review_reply_workflow.ipynb` | Review analysis and reply generation |
| `8_X_post_generator.ipynb` | Social media post generator |
| `9_basic_chartbot.ipynb` | Basic chatbot using LangGraph |
| `10_persistence.ipynb` | State persistence and memory in graphs |
| `11_tools_.ipynb` | Tool-calling agents with LangGraph |
| `12_mcp.py` | Model Context Protocol (MCP) integration |
| `13_rag.ipynb` | RAG (Retrieval-Augmented Generation) pipeline |
| `Langgraph_Chatbot/` | Full chatbot application |
| `Langgraph_Chatbot_with_databse/` | Chatbot with database memory |
| `langsmith-masterclass/` | LangSmith observability and tracing masterclass |

## Tech Stack

- **Python 3.11+**
- **LangGraph** — stateful agent orchestration
- **LangChain** — LLM primitives and tool integrations
- **LangSmith** — tracing and observability
- **OpenAI / Groq** — LLM providers
- **Jupyter Notebooks** — interactive exploration

## Getting Started

### Prerequisites

- Python 3.11+
- Jupyter Notebook or JupyterLab

### Installation

```bash
git clone https://github.com/VishalWaghmare03/LangGraph.git
cd LangGraph
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Set Up API Keys

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
LANGCHAIN_API_KEY=your_key_here
```

### Run Notebooks

```bash
jupyter notebook
```

Open any `.ipynb` file to get started.

## Key Concepts Covered

- StateGraph and node definitions
- Conditional edges and routing logic
- Checkpointers and state persistence
- Tool-calling agents
- Multi-agent collaboration
- RAG with LangGraph
- LangSmith tracing and evaluation
- MCP (Model Context Protocol)

## License

MIT
