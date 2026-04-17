import streamlit as st
from groq import Groq

# Groq API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
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
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("💻 AI Code Reviewer Pro")
st.sidebar.info("""
### Features
✅ Real Bug Detection  
✅ Multi-language Support  
✅ Complexity Analysis  
✅ Optimization Suggestions  
""")

# Header
st.markdown("<h1 class='title'>AI-Powered Code Reviewer & Bug Explainer</h1>", unsafe_allow_html=True)

language = st.selectbox(
    "Select Language",
    ["Python", "Java", "C++", "JavaScript", "C#", "PHP"]
)

code = st.text_area("Paste your code here:", height=300)

if st.button("Analyze Code"):
    if code.strip():
        prompt = f"""
You are an AI-powered code reviewer.

Analyze this {language} code and provide:

1. Detected Language
2. Code Purpose Summary
3. Bugs Found
4. Bug Explanations
5. Time & Space Complexity
6. Optimization Suggestions
7. Optimized Code

Code:
{code}

Explain in student-friendly language.
"""

        with st.spinner("Analyzing code..."):
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

        st.success("Analysis Complete!")
        st.markdown(result)

    else:
        st.warning("Please paste some code.")
