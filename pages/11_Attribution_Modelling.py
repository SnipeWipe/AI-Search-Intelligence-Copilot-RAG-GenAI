import streamlit as st
import pandas as pd
import plotly.express as px

from backend.attribution.attribution_engine import (
    AttributionEngine
)

st.title(
    "Attribution Modeling"
)

df = pd.read_csv(
    "datasets/channel_paths.csv"
)

engine = AttributionEngine()

model = st.selectbox(

    "Model",

    [

        "First Touch",

        "Last Touch",

        "Linear"

    ]

)

if model == "First Touch":

    result = engine.first_touch(df)

elif model == "Last Touch":

    result = engine.last_touch(df)

else:

    result = engine.linear(df)

st.dataframe(
    result
)

fig = px.bar(

    result,

    x="Channel",

    y="Revenue"

)

st.plotly_chart(
    fig,
    use_container_width=True
)