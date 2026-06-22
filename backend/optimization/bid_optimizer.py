import pandas as pd


class BidOptimizer:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

        self.df["ROAS"] = (
            self.df["Revenue"]
            /
            self.df["Spend"]
        )

    def optimize(self):

        total_budget = self.df["Spend"].sum()

        # Allocate budget proportional to ROAS
        roas_sum = self.df["ROAS"].sum()

        self.df["Recommended_Budget"] = (
            self.df["ROAS"] / roas_sum
        ) * total_budget

        self.df["Recommended_Budget"] = (
            self.df["Recommended_Budget"]
            .round(2)
        )

        self.df["Budget_Change"] = (
            self.df["Recommended_Budget"]
            - self.df["Spend"]
        ).round(2)

        return self.df