import pandas as pd

from prophet import Prophet

class TrendEngine:

    def __init__(
        self,
        dataframe
    ):

        self.df = dataframe.copy()

    def prepare_data(
        self,
        keyword
    ):

        keyword_df = (
            self.df[
                self.df["Query"] == keyword
            ]
            .groupby("Date")
            ["Clicks"]
            .sum()
            .reset_index()
        )

        keyword_df.columns = [
            "ds",
            "y"
        ]

        return keyword_df

    def forecast_keyword(
        self,
        keyword,
        periods=30
    ):

        data = self.prepare_data(
            keyword
        )

        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )

        model.fit(data)

        future = (
            model.make_future_dataframe(
                periods=periods
            )
        )

        forecast = (
            model.predict(
                future
            )
        )

        return forecast