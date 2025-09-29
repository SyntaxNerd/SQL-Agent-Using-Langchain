
# 🤖 SQL AI Agent

***Note: This project is not production-ready. It is a personal project built for learning and experimentation purposes only.***

---
## 🧠 Overview
Ask natural language questions about your database — no SQL required!. This app uses LangChain + LLMs to convert questions into SQL queries and return results, all wrapped in a beautiful Streamlit UI.


## ✨ Features

- 🔎 Ask English questions → Get SQL results
- 🧠 Powered by LangChain Agents and LLMs
- 📊 SQL toolkits for better query results
- 🧾 Agent’s thought process for better understanding (debug-friendly)
## 🚀 Tech Stack

- Python 3.10+
- Streamlit – Interactive UI
- LangChain – LLM + SQL Agent
- LLM - Groq(llama-3.3-70b-versatile)
- SQLite – Sample Database


## ⚡ Run Locally

Clone the project

```bash
  git clone https://github.com/SyntaxNerd/SQL-Agent-Using-Langchain.git
```

Go to the project directory

```bash
  cd SQL-Agent-Using-Langchain
```

Install uv (rust based package manager for python)

```
  curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create a virtual environment

```
uv venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

Install dependencies

```bash
  uv add -r requirements.txt
```

Start the server with streamlit

```bash
  streamlit run app.py
```


## 🎮 Usage

- Start the Streamlit app.
- Type a natural language question (e.g. “List the total sales by month”).
- Click Submit Query.
- See results + agent’s thought process.


## 🌌 Optimizations

- 🔐 User authentication
- 📊 Support for multiple databases (Postgres, MySQL, etc.)
- 🤝 Collaboration mode (share queries with teammates)
- 🎤 Voice-based queries


## 🤝 Lessons Learned

- How to integrate LangChain with SQL databases for natural language querying.
- Handling agent responses & intermediate steps for better debugging.
- The importance of prompt design when working with LLMs for accurate SQL generation.
