from app.core.pinecone_client import index


def search_documents(
    query: str
):
    results = index.search_records(
        namespace="__default__",
        query={
            "top_k": 5,
            "inputs": {
                "text": query
            }
        }
    )

    return results