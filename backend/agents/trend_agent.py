from backend.llm.gemini_client import (
    GeminiClient
)


class TrendAgent:

    def __init__(self):

        self.llm = GeminiClient()

    def analyze(
        self,
        trend_data
    ):

        prompt = f"""
You are a Director of Search Analytics.

Analyze:

{trend_data}

Provide:

1 Executive Summary

2 Emerging Search Themes

3 Acquisition Opportunities

4 Budget Reallocation

5 Risks

6 Recommended Actions

7 Expected Business Impact
"""

        return (
            self.llm.generate(
                prompt
            )
        )