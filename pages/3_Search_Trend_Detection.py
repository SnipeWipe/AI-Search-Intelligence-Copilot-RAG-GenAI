import streamlit as st
import pandas as pd
import plotly.express as px

from backend.analytics.growth_scorer import (
    GrowthScorer
)

df = pd.read_csv(
    "datasets/search_queries.csv"
)

st.title(
    "Search Trend Detection"
)

growth = (
    GrowthScorer()
    .calculate_growth(df)
)

st.session_state["growth"] = growth

st.subheader(
    "Fastest Growing Keywords"
)

st.dataframe(
    growth,
    use_container_width=True
)

fig = px.bar(
    growth.head(20),
    x="Growth",
    y="Query",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
