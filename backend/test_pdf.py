from app.services.pdf_processor import (
    extract_text
)

text = extract_text(
    "sample.pdf"
)

print(
    text[:1000]
)