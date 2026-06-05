import google.generativeai as genai

from app.core.config import GEMINI_API_KEY
from app.agents.research_agent import gather_context

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question: str):

    context = gather_context(question)

    pdf_context = "\n\n".join(
        [doc.page_content for doc in context["pdf"]]
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

Use both the uploaded documents and web search results.

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

Provide a detailed answer.
"""

    response = model.generate_content(prompt)

    return {
        "answer": response.text,
        "sources": context["web"]["results"]
    }