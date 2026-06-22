import streamlit as st
import pandas as pd
import plotly.express as px
from backend.analytics.topic_discovery import (TopicDiscovery)

@st.cache_resource
def load_topic_model(dataframe):

    topic_engine = TopicDiscovery()

    result = (
        topic_engine.discover_topics(
            dataframe
        )
    )

    summary = (
        topic_engine.topic_summary()
    )

    return (
        topic_engine,
        result,
        summary
    )

st.title(
    "Emerging Topic Discovery"
)

df = pd.read_csv(
    "datasets/search_queries.csv"
)

topic_engine, result, summary = (
    load_topic_model(df)
)

st.subheader(
    "Topic Summary"
)

st.dataframe(
    summary,
    use_container_width=True
)

topic_id = st.selectbox(
    "Select Topic",
    summary["Topic"]
)

words = (
    topic_engine.get_topic_words(
        topic_id
    )
)

if words:

    topic_df = pd.DataFrame(
        words,
        columns=[
            "Word",
            "Importance"
        ]
    )

    st.subheader(
        f"Top Keywords for Topic {topic_id}"
    )

    st.dataframe(
        topic_df,
        use_container_width=True
    )

    fig = px.bar(
        topic_df,
        x="Importance",
        y="Word",
        orientation="h",
        title=f"Topic {topic_id} Keywords"
    )

    fig.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Queries in Selected Topic"
    )

    topic_queries = (
        result[
            result["Topic"] == topic_id
        ][["Query"]]
    )

    st.dataframe(
        topic_queries,
        use_container_width=True
    )

else:

    st.warning(
        "No keywords available for this topic."
    )