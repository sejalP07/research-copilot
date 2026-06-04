import google.generativeai as genai

from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(question: str) -> str:
    response = model.generate_content(question)

    return response.text