
# 🤖 SQL AI Agent

***Note: This project is not production-ready. It is a personal project built for learning and experimentation purposes only.***

---
<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/LangChain-00A3E0?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABGklEQVQ4T+3TP0oDQRTH8c9M4AvsA7jA3sAb/AUbhwC3sBTsALyAmXvXhK6u3E4CE5HcDAS2uSJpygRz7w7mzMzLyKnxAM6dxvQ0M1z1gJ0GnaKcJtDkO7c6XW7v3IXR6BhPjtmxdES0Td12mgMZZDDx0GcYYM1eb8Sgxeq9lPVNdNhbph/5K8uSD0mXxkR8gz9DhXzS3cXjC8XJk4gY0fIvsDgE5X9HGWTWZlsnPr1gGqukQbmH8xHJ9yWfQJK6v5YzNHCpFbJ0Oe8nWrs8gW8/0m4NYuQZL4ns5IP0wCX3b9KOHYfGpXd+u3Jr7+EyHQv3bPUDn6UK1aq4OThX3/1AaXUg5XqgEsAAAAASUVORK5CYII=" alt="LangChain" />
</p>

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


## 🎮 Demo URL
- Link : https://sql-agent-using-langchain-by-akash.streamlit.app/

## 🤝 Lessons Learned

- How to integrate LangChain with SQL databases for natural language querying.
- Handling agent responses & intermediate steps for better debugging.
- The importance of prompt design when working with LLMs for accurate SQL generation.
