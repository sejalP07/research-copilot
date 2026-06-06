from app.core.supabase_client import supabase

def upload_pdf(
    file_name: str,
    file_bytes: bytes
):
    path = file_name

    supabase.storage.from_(
        "documents"
    ).upload(
        path,
        file_bytes
    )

    return path