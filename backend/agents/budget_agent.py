from backend.llm.gemini_client import GeminiClient


class BudgetAgent:

    def __init__(self):

        self.llm = GeminiClient()

    def analyze(self, data):

        prompt = f"""
You are a Budget Optimization Expert.

Analyze:

{data}

Provide:

1 Budget reallocations

2 Underinvested campaigns

3 Overinvested campaigns

4 Recommendations
"""

        return self.llm.generate(
            prompt
        )