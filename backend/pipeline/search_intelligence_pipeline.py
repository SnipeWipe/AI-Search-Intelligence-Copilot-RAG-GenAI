import pandas as pd

from backend.analytics.semantic_cluster_engine import (
    SemanticClusterEngine
)

from backend.analytics.topic_discovery import (
    TopicDiscovery
)

from backend.analytics.growth_scorer import (
    GrowthScorer
)

from backend.analytics.opportunity_scoring import (
    OpportunityScorer
)

from backend.agents.trend_agent import (
    TrendAgent
)


class SearchIntelligencePipeline:

    def __init__(self):

        self.cluster_engine = (
            SemanticClusterEngine()
        )

        self.topic_engine = (
            TopicDiscovery()
        )

        self.growth_engine = (
            GrowthScorer()
        )

        self.opp_engine = (
            OpportunityScorer()
        )

        self.agent = (
            TrendAgent()
        )

    def run(
        self,
        dataframe
    ):

        clusters = (
            self.cluster_engine
            .create_clusters(
                dataframe
            )
        )

        topic_df = (
            self.topic_engine
            .discover_topics(
                dataframe
            )
        )

        topics = (
            self.topic_engine
            .topic_summary()
        )

        growth = (
        self.growth_engine
        .calculate_growth(dataframe)
        )

        opportunities = (
            self.opp_engine
            .score(
                growth
            )
        )

        insights = (
            self.agent
            .analyze(
                opportunities
                .head(10)
                .to_string()
            )
        )

        return {

            "clusters":
            clusters,

            "topics":
            topics,

            "growth":
            growth,

            "opportunities":
            opportunities,

            "insights":
            insights

        }