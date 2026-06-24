import streamlit as st
from sentence_transformers import (
    SentenceTransformer
)


@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


class EmbeddingModel:

    def __init__(self):

        self.model = (
            load_embedding_model()
        )

    def generate_embeddings(
            self,
            texts
    ):

        return self.model.encode(
            texts,
            show_progress_bar=True
        )
