import numpy as np

class AnomalyDetector:

    def detect(
        self,
        series
    ):

        mean = np.mean(
            series
        )

        std = np.std(
            series
        )

        upper = (
            mean
            +
            3 * std
        )

        lower = (
            mean
            -
            3 * std
        )

        anomalies = (
            (series > upper)
            |
            (series < lower)
        )

        return anomalies