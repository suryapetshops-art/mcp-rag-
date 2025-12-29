import streamlit as st

st.set_page_config(page_title="RAG + MCP AI", layout="centered")

st.title("🤖 RAG + MCP AI")
st.write("✅ Streamlit deployment successful!")
st.write("This is a test app. Your setup is working.")

question = st.text_input("Ask something:")

if question:
    st.success(f"You asked: {question}")
    st.info("Next step: AI response will be added here.")
