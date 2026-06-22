import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class AudienceSegmentation:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    def create_segments(self, n_clusters=4):

        self.df["CTR"] = (
            self.df["Clicks"] /
            self.df["Impressions"]
        )

        self.df["CVR"] = (
            self.df["Conversions"] /
            self.df["Clicks"]
        )

        self.df["ROAS"] = (
            self.df["Revenue"] /
            self.df["Spend"]
        )

        features = self.df[
            [
                "CTR",
                "CVR",
                "ROAS",
                "Revenue",
                "Spend"
            ]
        ]

        scaler = StandardScaler()

        scaled = scaler.fit_transform(
            features
        )

        model = KMeans(
            n_clusters=n_clusters,
            random_state=42
        )

        self.df["Segment"] = (
            model.fit_predict(scaled)
        )

        segment_map = {

            0: "High Value Audience",
            1: "Growth Audience",
            2: "Premium Audience",
            3: "Low Value Audience"

        }

        self.df["Audience_Type"] = (

            self.df["Segment"]
            .map(segment_map)

        )

        return self.df