import streamlit as st
from utils.reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")
st.markdown("Paste your code below and get instant AI feedback.")

language = st.selectbox(
    "Select Programming Language",
    ["Python", "Java", "C++", "JavaScript", "C", "Other"]
)

code_input = st.text_area("Paste your code here:", height=300)

if st.button("Review My Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            result = review_code(code_input, language)
        st.markdown(result)
