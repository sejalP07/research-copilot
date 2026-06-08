from app.core.supabase_client import supabase


def save_document_metadata(
    filename: str,
    file_url: str
):
    response = (
        supabase
        .table("documents")
        .insert({
            "filename": filename,
            "file_url": file_url
        })
        .execute()
    )

    return response.data


def get_documents():
    response = (
        supabase
        .table("documents")
        .select("*")
        .execute()
    )

    return response.data


def delete_document(doc_id):
    response = (
        supabase
        .table("documents")
        .delete()
        .eq("id", doc_id)
        .execute()
    )

    return response.data