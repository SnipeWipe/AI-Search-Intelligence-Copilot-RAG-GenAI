class OpportunityScorer:

    def score(
        self,
        df
    ):

        df = df.copy()

        df["Opportunity_Score"] = (
            df["Growth"] * 0.4
        )

        return df.sort_values(
            "Opportunity_Score",
            ascending=False
        )