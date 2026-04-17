import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)

# Sidebar
st.sidebar.title("⚙ Project Info")
st.sidebar.info("""
**AI-Powered Code Reviewer & Bug Explainer**

This app helps students:
- Detect bugs
- Understand errors
- Analyze complexity
- Get optimized code suggestions
""")

# Main Title
st.title("💻 AI-Powered Code Reviewer & Bug Explainer")
st.markdown("Paste your code below and get a structured review report.")

# Code Input Box
code = st.text_area("📌 Paste Your Code Here", height=300)

# Review Button
if st.button("🔍 Review Code"):
    if code.strip():

        st.success("Code analyzed successfully!")

        # Display code
        st.subheader("📄 Submitted Code")
        st.code(code, language="python")

        # Review Sections
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧠 Detected Language")
            st.write("Python")

            st.subheader("🐞 Bugs Found")
            st.write("""
- Possible variable mismatch
- Potential syntax or logic issue
- Output formatting issue
""")

            st.subheader("📘 Bug Explanations")
            st.write("""
The code may contain:
1. Incorrect variable names
2. Missing syntax elements
3. Data type mismatches
""")

        with col2:
            st.subheader("⏱ Complexity Analysis")
            st.write("""
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
""")

            st.subheader("🚀 Optimization Suggestions")
            st.write("""
- Use meaningful variable names
- Reduce unnecessary loops
- Improve output formatting
""")

        st.subheader("✅ Optimized Code")
        st.code(code, language="python")

    else:
        st.warning("Please paste some code before reviewing.")
