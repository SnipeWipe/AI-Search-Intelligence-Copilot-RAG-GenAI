import streamlit as st
import pandas as pd

from backend.optimization.bid_optimizer import (
    BidOptimizer
)

st.title(
    "Bid Optimization Engine"
)

df = pd.read_csv(
    "datasets/campaigns.csv"
)

optimized = (
    BidOptimizer(df)
    .optimize()
)

st.dataframe(
    optimized,
    use_container_width=True
)