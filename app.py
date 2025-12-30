import streamlit as st
from openai import OpenAI

st.title("RAG + MCP AI")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Ask something")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please type a question")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": question}
                ]
            )

        st.write("### Answer")
        st.write(response.choices[0].message.content)
