import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from pypdf import PdfReader
import tempfile

st.set_page_config(page_title="Telugu RAG AI")
st.title("🤖 Telugu PDF AI Assistant")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(docs, embeddings)

    llm = HuggingFacePipeline.from_model_id(
        model_id="google/flan-t5-small",
        task="text2text-generation"
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    question = st.text_input("మీ ప్రశ్న ఇక్కడ టైప్ చేయండి (Telugu / English)")

    if question:
        answer = qa.run(question)
        st.success(answer)
