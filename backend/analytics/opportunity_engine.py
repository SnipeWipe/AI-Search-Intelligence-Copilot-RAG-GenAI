import pandas as pd

class OpportunityEngine:

    def score(
        self,
        dataframe
    ):

        df = dataframe.copy()

        df["CTR"] = (
            df["Clicks"]
            /
            df["Impressions"]
        )

        df["CVR"] = (
            df["Conversions"]
            /
            df["Clicks"]
        )

        df["Opportunity_Score"] = (

            df["Growth_Rate"] * 0.40

            +

            df["CTR"] * 100 * 0.30

            +

            df["CVR"] * 100 * 0.30

        )

        return (
            df.sort_values(
                "Opportunity_Score",
                ascending=False
            )
        )