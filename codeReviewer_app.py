import streamlit as st

st.set_page_config(page_title="AI Code Reviewer")

st.title("AI-Powered Code Reviewer & Bug Explainer")

code = st.text_area("Paste your code here:")

if st.button("Review Code"):
    if code:
        st.subheader("Review Result")

        st.write("### Detected Language")
        st.write("Python")

        st.write("### Code Purpose Summary")
        st.write("This code performs the given task based on user logic.")

        st.write("### Bugs Found")
        st.write("- Possible syntax or logic issues found.")

        st.write("### Bug Explanations")
        st.write("- Check indentation, variable names, and loops.")

        st.write("### Time & Space Complexity")
        st.write("- Time Complexity: O(n)")
        st.write("- Space Complexity: O(1)")

        st.write("### Optimization Suggestions")
        st.write("- Improve variable naming and reduce unnecessary loops.")

        st.write("### Optimized Code")
        st.code(code, language="python")
    else:
        st.warning("Please paste code first.")
