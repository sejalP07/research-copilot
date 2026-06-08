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
    documents = set()

    for hit in results.result.hits:

        documents.add(
            hit.fields["document"]
        )

        context += (
            hit.fields["text"]
            + "\n\n"
        )

    return {
        "context": context,
        "documents": list(
            documents
        )
    }