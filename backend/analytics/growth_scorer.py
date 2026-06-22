import pandas as pd

class GrowthScorer:

    def calculate_growth(
        self,
        dataframe
    ):

        result = []

        keywords = dataframe["Query"].unique()

        for keyword in keywords:

            temp = (
                dataframe[
                    dataframe["Query"] == keyword
                ]
                .sort_values("Date")
            )

            if len(temp) < 10:
                continue

            first = temp.head(7)["Clicks"].mean()
            last = temp.tail(7)["Clicks"].mean()

            growth = ((last - first) / first) * 100

            result.append(
                {
                    "Query": keyword,
                    "Growth": round(growth, 2),

                    # Temporary placeholders
                    "Theme": "Search Demand",

                    "Priority":
                    "High" if growth > 30
                    else "Medium" if growth > 0
                    else "Low"
                }
            )

        growth_df = pd.DataFrame(result)

        return growth_df.sort_values(
            "Growth",
            ascending=False
        )