from bertopic import BERTopic
from umap import UMAP

class TopicDiscovery:

    def __init__(self):

        umap_model = UMAP(
            n_neighbors=15,
            n_components=5,
            min_dist=0.0,
            metric="cosine",
            random_state=42
        )

        self.topic_model = BERTopic(
            umap_model=umap_model,
            verbose=True,
            low_memory=True,
            calculate_probabilities=False
        )

    def discover_topics(self,dataframe):

        docs = (dataframe["Query"].sort_values().tolist())

        topics, probs = (
            self.topic_model.fit_transform(
                docs
            )
        )

        dataframe["Topic"] = topics

        return dataframe

    def topic_summary(self):

        return (
            self.topic_model
            .get_topic_info()
        )

    def get_topic_words(
        self,
        topic_id
    ):

        return (
            self.topic_model
            .get_topic(
                topic_id
            )
        )