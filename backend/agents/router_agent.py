from backend.agents.trend_agent import TrendAgent
from backend.agents.budget_agent import BudgetAgent
from backend.agents.visibility_agent import VisibilityAgent
from backend.agents.executive_agent import ExecutiveAgent


class RouterAgent:

    def route(
            self,
            question,
            trend_data,
            budget_data,
            visibility_data
    ):

        question = question.lower()

        if "budget" in question:

            return (
                BudgetAgent()
                .analyze(budget_data)
            )

        elif "visibility" in question:

            return (
                VisibilityAgent()
                .analyze(
                    visibility_data
                )
            )

        elif "executive" in question:

            trend_output = (
                TrendAgent()
                .analyze(trend_data)
            )

            budget_output = (
                BudgetAgent()
                .analyze(budget_data)
            )

            visibility_output = (
                VisibilityAgent()
                .analyze(visibility_data)
            )

            return (
                ExecutiveAgent()
                .analyze(
                    trend_insights=trend_output,
                    budget_insights=budget_output,
                    visibility_insights=visibility_output,
                    experimentation_insights="No experimentation data available."
                )
            )

        else:

            return (
                TrendAgent()
                .analyze(
                    trend_data
                )
            )