import streamlit as st
import pandas as pd
from backend.analytics.growth_scorer import (GrowthScorer)
from backend.analytics.topic_discovery import (TopicDiscovery)
from backend.analytics.opportunity_scoring import (OpportunityScorer)
from backend.agents.trend_agent import (TrendAgent)

df = pd.read_csv("datasets/search_queries.csv")

st.title("Trend Intelligence Dashboard")

if "growth" not in st.session_state:
    st.session_state["growth"] = (
        GrowthScorer()
        .calculate_growth(df)
    )
growth = st.session_state["growth"]

st.subheader(
    "Top Growing Queries"
)

st.dataframe(
    growth.head(20),
    use_container_width=True
)

topic_engine = (
    TopicDiscovery()
)

topic_engine.discover_topics(
    df
)

topic_summary = (
    topic_engine.topic_summary()
)

st.subheader(
    "Emerging Topics"
)

st.dataframe(
    topic_summary,
    use_container_width=True
)

opp = (
    OpportunityScorer()
)

opportunity_df = (
    opp.score(
        growth
    )
)

st.subheader(
    "Top Opportunities"
)

st.dataframe(
    opportunity_df.head(10),
    use_container_width=True
)

agent = TrendAgent()

top_data = (
    opportunity_df
    .head(10)
    .to_string()
)

analysis = (
    agent.analyze(
        top_data
    )
)

st.subheader(
    "Executive Recommendations"
)

st.markdown(
    analysis
)
