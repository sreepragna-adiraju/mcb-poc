import streamlit as st

st.title("🏫 MCB SmartAI Assistant")

st.metric("Notices", 15)
st.metric("Exams", 3)
st.metric("Holidays", 2)

question = st.text_input("Ask a question")

if question:
    st.success("AI Answer appears here")