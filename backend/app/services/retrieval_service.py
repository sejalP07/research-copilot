from app.core.pinecone_client import index


def get_context(
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

    context = ""

    for hit in results.result.hits:
        context += (
            hit.fields["text"]
            + "\n\n"
        )

    return context