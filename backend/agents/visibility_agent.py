from backend.llm.gemini_client import GeminiClient


class VisibilityAgent:

    def __init__(self):

        self.llm = GeminiClient()

    def analyze(self, data):

        prompt = f"""
You are an AI Search Visibility Expert.

Analyze:

{data}

Provide:

1 Visibility gaps

2 Competitor risks

3 Share of Voice insights

4 Recommendations
"""

        return self.llm.generate(
            prompt
        )