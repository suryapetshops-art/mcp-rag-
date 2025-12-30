import os
import streamlit as st

st.set_page_config(page_title="RAG + MCP AI", layout="centered")

# --- API key handling ---
# Prefer environment variable `API_KEY`. Also allow entering it in the sidebar (password field).
env_api_key = os.getenv("API_KEY", "")
if "api_key" not in st.session_state:
    st.session_state["api_key"] = env_api_key

sidebar_key = st.sidebar.text_input("API Key", value=st.session_state.get("api_key", ""), type="password", help="Set your API key (not saved to disk).")
if sidebar_key and sidebar_key != st.session_state.get("api_key", ""):
    st.session_state["api_key"] = sidebar_key

if st.session_state.get("api_key"):
    st.sidebar.success("API key configured")
else:
    st.sidebar.warning("No API key configured. Set via sidebar or env var `API_KEY`.")

st.title("🤖 RAG + MCP AI")
st.write("✅ Streamlit deployment successful!")
st.write("This is a test app. Your setup is working.")

question = st.text_input("Ask something:")

if question:
    st.success(f"You asked: {question}")
    st.info("Next step: AI response will be added here.")

# Example: show whether API key is available (do not print the key itself)
if st.session_state.get("api_key"):
    st.write("API key: set (hidden)")
else:
    st.write("API key: not set")
