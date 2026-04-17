import streamlit as st
from reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI-Powered Code Reviewer & Bug Explainer")
st.write("Upload or paste your code below and get bug analysis, complexity insights, and optimized suggestions.")

# Code Input
code_input = st.text_area("Paste Your Code Here", height=300)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            result = review_code(code_input)

        st.subheader("📌 Review Result")
        st.markdown(result)
    else:
        st.warning("Please paste some code first.")
