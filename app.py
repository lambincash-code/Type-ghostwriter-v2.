import streamlit as st
import google.generativeai as genai
from docx import Document
import io

st.set_page_config(page_title="Ghostwriter Pro", layout="wide")
st.title("📚 Ghostwriter Pro: 80k Word Architect")

with st.sidebar:
    st.header("Project Setup")
    api_key = st.text_input("Gemini API Key", type="password")
    st.divider()
    step = st.radio("Workflow", ["1. Setup", "2. Source Context", "3. Draft", "4. Export"])

if "1." in step:
    st.header("Step 1: Topic")
    topic = st.text_input("What is the book's title?")
    if st.button("Save"): st.session_state.topic = topic

elif "3." in step:
    st.header("Step 3: Drafting")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        if st.button("Write Chapter 1"):
            res = model.generate_content(f"Write Chapter 1 for {st.session_state.get('topic', 'a book')}", stream=True)
            txt, p = "", st.empty()
            for chunk in res:
                txt += chunk.text
                p.markdown(txt + "▌")
            st.session_state.ch1 = txt
