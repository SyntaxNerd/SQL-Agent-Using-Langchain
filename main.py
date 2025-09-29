# libraries
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_groq.chat_models import ChatGroq
from langchain.agents import AgentExecutor
from langchain import hub
from dotenv import load_dotenv
import os

# load api key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# agent function
def agent(query):

    # database connections and prompts
    database = SQLDatabase.from_uri("sqlite:///sample.db")
    prompt = hub.pull("rlm/text-to-sql") # not using

    # LLM model initialization
    llm = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature = 0.5,
        max_tokens = None
    )

    # agent initialization
    sql_agent = create_sql_agent(
        llm = llm,
        db = database,
        verbose = True
    )

    response = sql_agent.invoke({
        "input": query
    })
    return response