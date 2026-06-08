import google.generativeai as genai

from app.core.config import GEMINI_API_KEY

from app.agents.research_agent import (
    gather_context
)

from app.services.history_service import (
    save_research
)

from app.services.retrieval_service import (
    get_context
)

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(
    question: str
):

    retrieval = get_context(
        question
    )

    pdf_context = retrieval[
        "context"
    ]

    context = gather_context(
        question
    )

    print(
        "\nDOCUMENTS USED:\n",
        retrieval["documents"]
    )

    print(
        "\nPDF CONTEXT:\n",
        pdf_context
    )

    web_context = ""

    for result in context["web"]["results"]:

        web_context += f"""
Title: {result["title"]}

Content:
{result["content"]}

URL:
{result["url"]}

"""

    prompt = f"""
You are a professional research assistant.

Use both the uploaded documents and
web search results.

====================
DOCUMENT CONTEXT
====================

{pdf_context}

====================
WEB CONTEXT
====================

{web_context}

====================
QUESTION
====================

{question}

Instructions:

1. Prefer DOCUMENT CONTEXT first.
2. If information is missing,
   use WEB CONTEXT.
3. Give a clear and detailed answer.
4. Mention important points.
5. At the end include a short
   Sources section.
"""

    response = model.generate_content(
        prompt
    )

    save_research(
        question,
        response.text
    )

    return {
        "answer": response.text,
        "documents": retrieval[
            "documents"
        ],
        "sources": context["web"][
            "results"
        ]
    }