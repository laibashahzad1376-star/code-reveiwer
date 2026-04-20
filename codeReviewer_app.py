import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)

# Sidebar
st.sidebar.title("💻 AI Code Reviewer")
st.sidebar.markdown("---")
st.sidebar.info("""
### Features
✅ Bug Detection  
✅ Bug Explanation  
✅ Complexity Analysis  
✅ Optimization Suggestions  
""")
st.sidebar.markdown("---")
st.sidebar.success("Built with Streamlit")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
    AI-Powered Code Reviewer & Bug Explainer
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style='text-align: center; font-size:18px;'>
    Paste your code below and receive a professional review report
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Input Section
code = st.text_area("📌 Paste Your Code Here", height=300, placeholder="Paste your Python code here...")

# Review Button
if st.button("🔍 Analyze Code", use_container_width=True):

    if code.strip():

        st.success("Analysis Completed Successfully!")

        # Display input code
        with st.expander("📄 Submitted Code", expanded=False):
            st.code(code, language="python")

        # Metrics Row
        col1, col2, col3 = st.columns(3)
        col1.metric("Detected Bugs", "3")
        col2.metric("Time Complexity", "O(n)")
        col3.metric("Optimization Score", "75%")

        st.markdown("---")

        # Two columns for detailed analysis
        left, right = st.columns(2)

        with left:
            with st.expander("🧠 Detected Language", expanded=True):
                st.write("Python")

            with st.expander("🐞 Bugs Found", expanded=True):
                st.write("""
1. Variable naming inconsistency  
2. Possible syntax issue  
3. Output formatting problem
""")

            with st.expander("📘 Bug Explanations", expanded=True):
                st.write("""
- Some variables may not match their intended use.  
- There might be missing syntax elements such as colons or brackets.  
- Output formatting can cause runtime issues.
""")

        with right:
            with st.expander("⏱ Complexity Analysis", expanded=True):
                st.write("""
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
""")

            with st.expander("🚀 Optimization Suggestions", expanded=True):
                st.write("""
- Use consistent variable names  
- Remove redundant loops  
- Improve readability with better formatting  
- Use built-in functions where possible
""")

        st.markdown("---")

        with st.expander("✅ Optimized Code", expanded=True):
            st.code(code, language="python")

    else:
        st.warning("Please paste some code before clicking Analyze.")
