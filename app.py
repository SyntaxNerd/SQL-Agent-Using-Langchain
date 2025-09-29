import streamlit as st
from main import agent

# --- Streamlit page config ---
st.set_page_config(page_title="SQL AI Agent", page_icon="🤖", layout="wide")

# --- Custom CSS for dark theme + AI background ---
page_bg = """
<style>
/* Background image - AI themed */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1661961112951-fb4b9da3e51b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Overlay for readability */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.75);
    z-index: 0;
}

/* Ensure content appears above overlay */
[data-testid="stAppViewContainer"] > div {
    position: relative;
    z-index: 1;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: rgba(20,20,20,0.95);
    color: #eee;
}

/* Headings */
.main-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #00FFB3;
    text-align: center;
    text-shadow: 0px 0px 8px rgba(0,255,179,0.7);
}
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #bbb;
    margin-bottom: 25px;
    font-style: italic;
}

/* Input box */
.stTextInput > div > div > input {
    border-radius: 10px;
    border: 1px solid #00FFB3;
    padding: 10px;
    font-size: 1rem;
    background-color: #111;
    color: #eee;
}

/* Answer box */
.answer-box {
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(25,25,25,0.9);
    border: 1px solid #00FFB340;
    margin-top: 15px;
    box-shadow: 0px 0px 15px rgba(0,255,179,0.2);
    color: #eee;
    font-size: 1.05rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">🤖 SQL AI Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask natural language questions about your database — no SQL required!</div>', unsafe_allow_html=True)

# --- Input field ---
query = st.text_input("💬 Enter your question:")

if st.button("🚀 Submit Query"):
    if query:
        with st.spinner("🔍 Thinking... querying the database..."):
            response = agent(query)

        # --- Final Answer ---
        st.subheader("✅ Agent Answer", divider = "gray")
        st.markdown(f"<div class='answer-box'>{response['output']}</div>", unsafe_allow_html = True)

        # --- Thought Process ---
        with st.expander("🧠 Show Agent Thoughts"):
            st.code(str(response), language="text")

        # --- animation ---
        st.success("Query completed successfully!")
        st.snow()

    else:
        st.warning("⚠️ Please enter a question before submitting")
