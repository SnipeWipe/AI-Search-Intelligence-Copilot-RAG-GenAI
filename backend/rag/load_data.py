import pandas as pd

from backend.rag.embedder import (
    EmbeddingModel
)

from backend.rag.vector_store import (
    VectorStore
)

embedder = EmbeddingModel()

store = VectorStore()

files = [

    "datasets/campaigns.csv",

    "datasets/search_queries.csv",

    "datasets/keywords.csv",

    "datasets/ab_test_data.csv",

    "datasets/ai_visibility.csv"

]

documents = []

for file in files:

    df = pd.read_csv(file)

    documents.extend(
        df.astype(str)
        .apply(
            lambda x:
            " | ".join(x),
            axis=1
        )
        .tolist()
    )

embeddings = (
    embedder
    .generate_embeddings(
        documents
    )
)

ids = [
    str(i)
    for i
    in range(
        len(documents)
    )
]

store.add_documents(
    ids,
    documents,
    embeddings
)

print(
    "Knowledge Base Loaded"
)