import chromadb

class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                "marketing_knowledge"
            )
        )

    def add_documents(
        self,
        ids,
        docs,
        embeddings
    ):

        self.collection.add(
            ids=ids,
            documents=docs,
            embeddings=embeddings.tolist()
        )

    def retrieve(
        self,
        query_embedding,
        k=5
    ):

        return self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=k
        )