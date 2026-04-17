import streamlit as st
from groq import Groq

# -------------------------
# STREAMLIT UI CONFIG
# -------------------------
st.set_page_config(page_title="AI Code Reviewer", layout="centered")

st.title("💻 AI Code Reviewer")
st.write("Paste your code below and get AI review + improvements")

# -------------------------
# GROQ CLIENT
# -------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -------------------------
# INPUT BOX
# -------------------------
code_input = st.text_area("Enter your code here", height=300)

# -------------------------
# BUTTON
# -------------------------
if st.button("Review Code"):

    if code_input.strip() == "":
        st.warning("Please enter some code first!")
    else:

        with st.spinner("Analyzing your code..."):

            prompt = f"""
You are an expert senior software engineer and code reviewer.

Review the following code and provide:
1. Errors (if any)
2. Improvements
3. Best practices
4. Optimized version (if needed)

Code:
{code_input}
"""

            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

        st.subheader("🧠 AI Review")
        st.write(result)

