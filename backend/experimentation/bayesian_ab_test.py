import numpy as np

from scipy.stats import beta


class BayesianABTest:

    def analyze(

            self,

            visitors_a,
            conversions_a,

            visitors_b,
            conversions_b

    ):

        samples = 100000

        posterior_a = beta.rvs(

            conversions_a + 1,

            visitors_a - conversions_a + 1,

            size=samples

        )

        posterior_b = beta.rvs(

            conversions_b + 1,

            visitors_b - conversions_b + 1,

            size=samples

        )

        probability = np.mean(

            posterior_b > posterior_a

        )

        lift = (

            posterior_b.mean()

            -

            posterior_a.mean()

        ) * 100

        return {

            "probability": probability,

            "lift": lift,

            "posterior_a": posterior_a,

            "posterior_b": posterior_b

        }