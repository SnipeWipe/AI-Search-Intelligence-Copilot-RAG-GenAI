import streamlit as st
import pandas as pd

from backend.analytics.semantic_cluster_engine import (
    SemanticClusterEngine
)

df = pd.read_csv(
    "datasets/search_queries.csv"
)

engine = (
    SemanticClusterEngine()
)

clusters = (
    engine.create_clusters(df)
)

st.title(
    "Semantic Search Themes"
)

st.dataframe(
    clusters,
    use_container_width=True
)