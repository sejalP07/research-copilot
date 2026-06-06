from app.core.supabase_client import supabase

def save_document_metadata(
    filename: str,
    file_url: str
):

    data = {
        "filename": filename,
        "file_url": file_url
    }

    supabase.table(
        "documents"
    ).insert(data).execute()