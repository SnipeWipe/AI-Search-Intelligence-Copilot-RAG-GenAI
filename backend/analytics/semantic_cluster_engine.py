import pandas as pd

from sentence_transformers import (
    SentenceTransformer
)

from sklearn.cluster import KMeans


class SemanticClusterEngine:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_clusters(
        self,
        dataframe,
        n_clusters=10
    ):

        queries = (
            dataframe["Query"]
            .unique()
            .tolist()
        )

        embeddings = (
            self.model.encode(
                queries,
                show_progress_bar=True
            )
        )

        kmeans = KMeans(
            n_clusters=n_clusters,
            random_state=42
        )

        labels = (
            kmeans.fit_predict(
                embeddings
            )
        )

        result = pd.DataFrame({

            "Query": queries,

            "Cluster": labels

        })

        return result