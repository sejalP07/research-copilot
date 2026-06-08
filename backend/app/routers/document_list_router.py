from fastapi import APIRouter

from app.services.document_service import (
    get_documents,
    delete_document
)

router = APIRouter()


@router.get("/documents/list")
def list_documents():

    return get_documents()


@router.delete("/documents/{doc_id}")
def remove_document(
    doc_id: str
):

    return delete_document(
        doc_id
    )