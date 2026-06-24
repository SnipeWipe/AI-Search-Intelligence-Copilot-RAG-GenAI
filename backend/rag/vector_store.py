# backend/rag/vector_store.py

import streamlit as st
import chromadb


@st.cache_resource
def get_client():

    return chromadb.PersistentClient(
        path="chroma_db"
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

        if self.collection.count() > 0:
            print("Collection already populated.")
            return

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def search(
            self,
            query_embedding,
            n_results=5
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

    def count_documents(self):

        return self.collection.count()
