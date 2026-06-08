from app.services.pdf_processor import (
    extract_text
)

from app.services.chunk_service import (
    create_chunks
)

text = extract_text(
    "sample.pdf"
)

chunks = create_chunks(
    text
)

print(
    "Chunks:",
    len(chunks)
)

print(
    chunks[0]
)