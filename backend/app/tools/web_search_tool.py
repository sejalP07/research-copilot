from tavily import TavilyClient
from app.core.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query: str):
    response = client.search(
        query=query,
        max_results=5
    )

    return response