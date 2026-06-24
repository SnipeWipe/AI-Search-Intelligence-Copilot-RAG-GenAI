import streamlit as st
import chromadb
from chromadb.config import Settings


@st.cache_resource
def get_client():

    return chromadb.PersistentClient(
        path="chroma_db",
        settings=Settings(
            anonymized_telemetry=False
        )
    )


class VectorStore:

    def __init__(self):

        self.client = get_client()

        self.collection = (
            self.client.get_or_create_collection(
                name="documents"
            )
        )
