from fastapi import APIRouter, UploadFile, File

from app.services.storage_service import upload_pdf
from app.services.document_service import (
    save_document_metadata
)

router = APIRouter()


@router.post("/documents")
async def upload_document(
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    file_url = upload_pdf(
        file.filename,
        file_bytes
    )

    save_document_metadata(
        file.filename,
        file_url
    )

    return {
        "filename": file.filename,
        "file_url": file_url
    }