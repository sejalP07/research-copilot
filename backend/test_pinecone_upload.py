from app.services.pdf_processor import (
    extract_text
)

from app.services.chunk_service import (
    create_chunks
)

from app.services.pinecone_service import (
    store_chunks
)

text = extract_text(
    "sample.pdf"
)

chunks = create_chunks(
    text
)

result = store_chunks(
    chunks,
    "sample.pdf"
)

print(result)