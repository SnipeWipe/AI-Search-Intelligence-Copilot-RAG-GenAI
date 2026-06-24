# backend/rag/vector_store.py

import chromadb

from chromadb.config import Settings


class VectorStore:

    def __init__(
            self,
            persist_directory="chroma_db"
    ):

        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="documents"
            )
        )

    def add_documents(
            self,
            chunks,
            embeddings
    ):

        ids = [
            f"doc_{i}"
            for i in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
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

        return (
            results["documents"][0]
            if results["documents"]
            else []
        )

    def count_documents(self):

        return self.collection.count()
