import streamlit as st

st.set_page_config(page_title="RAG + MCP AI", layout="centered")

st.title("🤖 RAG + MCP AI")
st.write("Your Streamlit app is working successfully 🎉")

with st.form("ask_form"):
    question = st.text_input("Ask something:", placeholder="Type a question...")
    submitted = st.form_submit_button("Submit")

if submitted:
    if question and question.strip():
        st.success(f"You asked: {question.strip()}")
    else:
        st.warning("Please enter a question")
