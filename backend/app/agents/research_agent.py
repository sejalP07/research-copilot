from app.tools.web_search_tool import search_web
from app.services.vectorstore import retrieve_documents

def gather_context(question: str):

    web_results = search_web(question)

    pdf_results = retrieve_documents(question)

    return {
        "web": web_results,
        "pdf": pdf_results
    }