import pandas as pd


class AttributionEngine:

    def first_touch(self, df):

        result = (

            df.groupby("Channel")
            ["Revenue"]
            .sum()

            * 0.4

        )

        return result.reset_index()

    def last_touch(self, df):

        result = (

            df.groupby("Channel")
            ["Revenue"]
            .sum()

            * 0.6

        )

        return result.reset_index()

    def linear(self, df):

        result = (

            df.groupby("Channel")
            ["Revenue"]
            .mean()

        )

        return result.reset_index()