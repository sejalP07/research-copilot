from app.services.retrieval_service import (
    get_context
)

from app.services.ai_service import model


def generate_report(
    question: str
):
    retrieval = get_context(
        question
    )

    context = retrieval[
        "context"
    ]

    prompt = f"""
Create a professional research report.

QUESTION:
{question}

CONTEXT:
{context}

Generate:

1. Executive Summary

2. Key Findings

3. Important Concepts

4. References

5. Conclusion
"""

    response = model.generate_content(
        prompt
    )

    return response.text