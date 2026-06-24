# backend/rag/vector_store.py

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

    def add_documents(
            self,
            ids,
            documents,
            embeddings
    ):

        # Avoid duplicate inserts
        existing_count = self.collection.count()

        if existing_count > 0:
            print(
                f"Collection already contains "
                f"{existing_count} documents."
            )
            return

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

        print(
            f"{len(documents)} documents added successfully."
        )

    def search(
            self,
            query_embedding,
            n_results=5
    ):

        results = self.collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=n_results
        )

        return results

    def count_documents(self):

        return self.collection.count()
