from sentence_transformers import (
    SentenceTransformer
)

from backend.llm.gemini_client import (
    GeminiClient
)

from backend.rag.vector_store import (
    VectorStore
)


class RAGEngine:

    def __init__(self):

        self.llm = GeminiClient()

        self.vector_store = (
            VectorStore()
        )

        self.embedder = (
            SentenceTransformer(
                "all-MiniLM-L6-v2"
            )
        )

    def answer(self, query):

    query_embedding = (
        self.embedder.encode(query)
    )

    results = (
        self.vector_store.search(
            query_embedding
        )
    )

    if len(results["documents"][0]) == 0:

        return (
            "No relevant documents found "
            "in the knowledge base."
        )

    docs = (
        results["documents"][0]
    )

    context = "\n".join(docs)

    prompt = f"""
You are an Executive Search Intelligence Copilot.

Use the following enterprise knowledge to answer.

==================================================

{context}

==================================================

Question:
{query}

Provide:

1. Executive Summary

2. Key Insights

3. Business Recommendations

4. Risks

5. Next Actions
"""

    response = (
        self.llm.generate(prompt)
    )

    return response
