import streamlit as st
import pandas as pd
import plotly.express as px

from backend.analytics.audience_segmentation import (
    AudienceSegmentation
)

st.set_page_config(
    page_title="Audience Targeting",
    layout="wide"
)

st.title(
    "Audience Targeting Engine"
)

df = pd.read_csv(
    "datasets/campaigns.csv"
)

segmented = (

    AudienceSegmentation(df)

    .create_segments()

)

st.dataframe(
    segmented.head(50),
    use_container_width=True
)

summary = (

    segmented
    .groupby("Audience_Type")
    ["Revenue"]
    .sum()
    .reset_index()

)

fig = px.bar(

    summary,

    x="Audience_Type",

    y="Revenue",

    title="Revenue Contribution by Audience"

)

st.plotly_chart(
    fig,
    use_container_width=True
)