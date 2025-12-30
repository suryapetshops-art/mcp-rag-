import streamlit as st

st.set_page_config(page_title="RAG + MCP AI", layout="centered")

st.title("🤖 RAG + MCP AI")
st.write("Your Streamlit app is working successfully 🎉")

question = st.text_input("Ask something:")

if st.button("Submit"):
    if question:
        st.success(f"You asked: {question}")
    else:
        st.warning("Please enter a question"0
