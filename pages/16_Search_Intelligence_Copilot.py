import streamlit as st

from backend.rag.rag_engine import (
    RAGEngine
)

st.set_page_config(
    page_title="Search Intelligence Copilot",
    layout="wide"
)

st.title(
    "Search Intelligence Copilot"
)

question = st.text_input(
    "Ask a strategic question"
)

if st.button(
        "Ask Copilot"
):

    with st.spinner(
            "Analyzing enterprise knowledge..."
    ):

        answer = (

            RAGEngine()

            .answer(
                question
            )
        )

    st.markdown(
        answer
    )