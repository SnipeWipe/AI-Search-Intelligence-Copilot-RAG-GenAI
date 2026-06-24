import chromadb
from chromadb.config import Settings


class VectorStore:

    _client = None
    _collection = None

    def __init__(
            self,
            persist_directory="chroma_db"
    ):

        if VectorStore._client is None:

            VectorStore._client = (
                chromadb.PersistentClient(
                    path=persist_directory,
                    settings=Settings(
                        anonymized_telemetry=False
                    )
                )
            )

        self.client = VectorStore._client

        if VectorStore._collection is None:

            VectorStore._collection = (
                self.client.get_or_create_collection(
                    name="documents"
                )
            )

        self.collection = (
            VectorStore._collection
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

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

    def count_documents(self):

        return self.collection.count()
