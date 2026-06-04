from app.services.pdf_service import extract_pdf_text
from app.services.chunk_service import chunk_text
from app.services.vectorstore import create_vectorstore

text = extract_pdf_text(
    "uploads/research_test.pdf"
)

chunks = chunk_text(text)

vectorstore = create_vectorstore(chunks)

print(
    f"Stored {len(chunks)} chunks"
)