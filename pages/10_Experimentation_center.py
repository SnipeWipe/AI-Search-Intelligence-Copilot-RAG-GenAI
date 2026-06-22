import streamlit as st
import matplotlib.pyplot as plt

from backend.experimentation.bayesian_ab_test import (
    BayesianABTest
)

st.title(
    "Experimentation Center"
)

col1, col2 = st.columns(2)

with col1:

    visitors_a = st.number_input(
        "Visitors A",
        1000
    )

    conversions_a = st.number_input(
        "Conversions A",
        100
    )

with col2:

    visitors_b = st.number_input(
        "Visitors B",
        1000
    )

    conversions_b = st.number_input(
        "Conversions B",
        120
    )

if st.button(
    "Run Experiment"
):

    result = (

        BayesianABTest()

        .analyze(

            visitors_a,
            conversions_a,

            visitors_b,
            conversions_b

        )
    )

    st.metric(

        "Probability B Wins",

        f"{result['probability']:.2%}"

    )

    st.metric(

        "Expected Lift",

        f"{result['lift']:.2f}%"

    )

    fig, ax = plt.subplots()

    ax.hist(

        result["posterior_a"],
        bins=50,
        alpha=0.5,
        label="A"

    )

    ax.hist(

        result["posterior_b"],
        bins=50,
        alpha=0.5,
        label="B"

    )

    ax.legend()

    st.pyplot(fig)