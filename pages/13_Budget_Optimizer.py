import streamlit as st
import pandas as pd
import plotly.express as px

from backend.optimization.bid_optimizer import (
    BidOptimizer
)

st.set_page_config(
    page_title="Budget Optimizer",
    layout="wide"
)

st.title(
    "Budget Optimization Engine"
)

df = pd.read_csv(
    "datasets/campaigns.csv"
)

optimized = (

    BidOptimizer(df )

    .optimize()

)

st.dataframe(
    optimized,
    use_container_width=True
)

fig = px.bar(

    optimized.head(20),

    x="Campaign_Name",

    y="Recommended_Budget",

    title="Recommended Budget Allocation"

)

st.plotly_chart(
    fig,
    use_container_width=True
)