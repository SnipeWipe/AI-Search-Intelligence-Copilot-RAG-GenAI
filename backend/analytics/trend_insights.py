from google import genai

class TrendInsightGenerator:

    def __init__(
        self,
        client
    ):

        self.client = client

    def generate(
        self,
        top_keywords
    ):

        prompt = f"""
You are a Senior Search Strategy Director.

Analyze the following search trends:

{top_keywords}

Provide:

1 Executive Summary

2 Fastest Growing Trends

3 Acquisition Opportunities

4 Budget Recommendations

5 Risks

6 Strategic Actions
"""

        response = (
            self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
        )

        return response.text