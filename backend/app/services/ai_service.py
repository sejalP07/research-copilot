import google.generativeai as genai

from app.core.config import GEMINI_API_KEY
from app.tools.web_search_tool import search_web
from app.services.vectorstore import retrieve_documents

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question: str):

    docs = retrieve_documents(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question using the provided context.

Context:
{context}

Question:
{question}

If the answer is not in the context,
say you don't know.
"""

    response = model.generate_content(
        prompt
    )

    return {
        "answer": response.text,
        "sources": []
    }