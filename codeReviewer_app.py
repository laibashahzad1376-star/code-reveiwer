import streamlit as st
from groq import Groq
import os

# API Setup
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    st.error("⚠️ API key not found! Please set GROQ_API_KEY as an environment variable.")
    st.stop()

client = Groq(api_key=API_KEY)

# Page Config
st.set_page_config(page_title="AI Code Reviewer Pro", page_icon="💻", layout="wide")

# Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    width: 100%;
    background-color: #2E8B57;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 3em;
}
.title {
    text-align: center;
    color: #2E8B57;
}
textarea {
    font-family: monospace !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("💻 AI Code Reviewer Pro")
st.sidebar.markdown("""
### 🚀 Features
- ✅ Bug Detection  
- ✅ Multi-language Support  
- ✅ Complexity Analysis  
- ✅ Optimization Suggestions  
""")

# Header
st.markdown("<h1 class='title'>AI-Powered Code Reviewer & Bug Explainer</h1>", unsafe_allow_html=True)

# Inputs
language = st.selectbox("Select Language", ["Python", "Java", "C++", "JavaScript", "C#", "PHP"])
code = st.text_area("Paste your code here:", height=300)

if code:
    st.code(code, language=language.lower())

# Analyze Button
if st.button("🚀 Analyze Code"):
    if not code.strip():
        st.warning("⚠️ Please paste some code.")
    else:
        prompt = f"""
You are an expert AI code reviewer.

Analyze the following {language} code and respond in a clean structured format:

1. Detected Language
2. Code Purpose
3. Bugs Found
4. Bug Explanation
5. Time & Space Complexity
6. Optimization Suggestions
7. Improved Code

Code:
{code}
"""

        with st.spinner("🔍 Analyzing code..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )

                result = response.choices[0].message.content

                st.success("✅ Analysis Complete!")
                st.markdown(result)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Groq")
