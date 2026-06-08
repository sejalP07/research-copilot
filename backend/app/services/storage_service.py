from app.core.supabase_client import supabase


def upload_pdf(
    file_name: str,
    file_bytes: bytes
):
    path = f"documents/{file_name}"

    supabase.storage.from_(
        "documents"
    ).upload(
        path,
        file_bytes
    )

    file_url = (
        supabase.storage
        .from_("documents")
        .get_public_url(path)
    )

    return file_url