import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import streamlit as st

from backend.rag.rag_engine import (
    RAGEngine
)

st.set_page_config(
    page_title="AI Search Intelligence Copilot",
    layout="wide"
)

st.title(
    "AI Search Intelligence Copilot"
)


@st.cache_resource
def load_rag():

    return RAGEngine()


try:

    rag = load_rag()

    st.success(
        "RAG Engine initialized successfully"
    )

except Exception as e:

    st.error(
        "Failed to initialize RAG Engine"
    )

    st.exception(e)

    st.stop()


question = st.chat_input(
    "Ask anything..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "Analyzing..."
            ):

                answer = (
                    rag.answer(question)
                )

            st.markdown(answer)

        except Exception as e:

            st.exception(e)
