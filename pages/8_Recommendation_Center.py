import streamlit as st
import pandas as pd

from backend.analytics.growth_scorer import (
    GrowthScorer
)

from backend.recommendations.recommendation_engine import (
    RecommendationEngine
)

st.set_page_config(
    page_title="Recommendation Center",
    layout="wide"
)

st.title(
    "Recommendation Center"
)

df = pd.read_csv(
    "datasets/search_queries.csv"
)

if "growth" not in st.session_state:
    st.session_state["growth"] = (
        GrowthScorer()
        .calculate_growth(df)
    )
else:
growth = st.session_state["growth"]

recommendations = (

    RecommendationEngine(
        growth_df
    )

    .generate_recommendations()
)

st.subheader("Growth Data")

st.dataframe(
    growth_df,
    use_container_width=True
)

st.subheader(
    "Strategic Recommendations"
)

st.dataframe(

    recommendations,

    use_container_width=True

)

high_priority = (

    recommendations[
        recommendations[
            "Priority"
        ] == "High"
    ]

)

st.metric(

    "High Priority Actions",

    len(high_priority)

)
