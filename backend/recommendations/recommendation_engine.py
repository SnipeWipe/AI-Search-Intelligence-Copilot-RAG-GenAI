import pandas as pd


class RecommendationEngine:

    def __init__(self, dataframe):

        self.df = dataframe

    def generate_recommendations(self):

        recommendations = []

        for _, row in self.df.iterrows():

            growth = row["Growth"]

            if growth > 40:

                recommendation = (
                    "Increase budget allocation and expand keyword coverage"
                )

                priority = "High"

                impact = (
                    "Capture emerging demand and improve acquisition"
                )

            elif growth > 10:

                recommendation = (
                    "Test new ad creatives and monitor performance"
                )

                priority = "Medium"

                impact = (
                    "Improve engagement and conversion rates"
                )

            else:

                recommendation = (
                    "Maintain current strategy and monitor trends"
                )

                priority = "Low"

                impact = "Stable performance"

            recommendations.append(
                {
                    "Query": row["Query"],
                    "Growth": round(
                        row["Growth"], 2
                    ),
                    "Recommendation": recommendation,
                    "Priority": priority,
                    "Expected_Impact": impact
                }
            )

        return pd.DataFrame(
            recommendations
        )