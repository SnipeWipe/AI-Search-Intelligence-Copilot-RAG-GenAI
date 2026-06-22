import streamlit as st
import pandas as pd

from backend.agents.router_agent import (
    RouterAgent
)

st.title(
    "Multi-Agent Search Copilot"
)

question = st.text_area(
    "Ask your question",
    placeholder="""
Examples:
• Which campaigns need budget increases?
• Analyze AI search visibility risks.
• Give me an executive summary.
• What are the emerging search trends?
"""
)

trend_df = pd.read_csv(
    "datasets/search_queries.csv"
)

budget_df = pd.read_csv(
    "datasets/campaigns.csv"
)

visibility_df = pd.read_csv(
    "datasets/ai_visibility.csv"
)

if st.button(
        "Analyze"
):

    with st.spinner(
            "Consulting agents..."
    ):

        response = (

            RouterAgent()

            .route(

                question,

                trend_df.head(20),

                budget_df.head(20),

                visibility_df.head(20)

            )

        )

    st.markdown(response)