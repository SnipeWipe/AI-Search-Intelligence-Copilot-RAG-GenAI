import pandas as pd

from xgboost import XGBRegressor

from sklearn.model_selection import (
    train_test_split
)


class ConversionForecaster:

    def train(
        self,
        dataframe
    ):

        features = [

            "Impressions",

            "Clicks",

            "Spend",

            "CTR",

            "CPC"

        ]

        X = dataframe[
            features
        ]

        y = dataframe[
            "Conversions"
        ]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        model = XGBRegressor(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            random_state=42

        )

        model.fit(
            X_train,
            y_train
        )

        return model