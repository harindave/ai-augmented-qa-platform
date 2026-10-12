import streamlit as st
from app.backend.qa_engine import analyze_requirement

st.title("Requirement Analyzer")

st.write("Enter a software requirement below to perform a basic requirement analysis.")

requirement = st.text_area(
    "Software Requirement",
    placeholder="Example: Users can reset their password using their registered email.",
)

if st.button("Analyze Requirement"):
    result = analyze_requirement(requirement)

    if result["status"] == "error":
        st.error(result["message"])
    else:
        st.success("Requirement analysis successful!")
        st.write(f"**Requirement:** {result['requirement']}")
        st.write(f"**Character Count:** {result['character_count']}")
