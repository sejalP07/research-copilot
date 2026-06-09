from app.services.pdf_processor import (
    extract_pdf_pages
)

from app.services.page_chunk_service import (
    create_page_chunks
)

from app.services.pinecone_service import (
    store_page_chunks
)

pages = extract_pdf_pages(
    "sample.pdf"
)

chunks = create_page_chunks(
    pages
)

result = store_page_chunks(
    chunks,
    "sample.pdf"
)

print(result)