import streamlit as st
import pandas as pd

from backend.pipeline.search_intelligence_pipeline import (
    SearchIntelligencePipeline
)

st.set_page_config(
    page_title="Search Intelligence Center",
    layout="wide"
)

st.title(
    "AI Search Intelligence Center"
)

df = pd.read_csv(
    "datasets/search_queries.csv"
)

pipeline = (
    SearchIntelligencePipeline()
)

results = (
    pipeline.run(
        df
    )
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Clusters",
        "Topics",
        "Growth",
        "Opportunities",
        "Executive AI"
    ]
)

with tab1:
    st.dataframe(
        results["clusters"],
        use_container_width=True
    )

with tab2:
    st.dataframe(
        results["topics"],
        use_container_width=True
    )

with tab3:
    st.dataframe(
        results["growth"],
        use_container_width=True
    )

with tab4:
    st.dataframe(
        results["opportunities"],
        use_container_width=True
    )

with tab5:
    st.markdown(
        results["insights"]
    )