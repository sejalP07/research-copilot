from app.core.pinecone_client import index


def store_page_chunks(
    chunks,
    document_name
):
    records = []

    for i, chunk in enumerate(
        chunks
    ):

        records.append(
            {
                "_id":
                    f"{document_name}-{i}",

                "text":
                    chunk["text"],

                "document":
                    document_name,

                "page":
                    chunk["page"]
            }
        )

    result = index.upsert_records(
        namespace="__default__",
        records=records
    )

    return result