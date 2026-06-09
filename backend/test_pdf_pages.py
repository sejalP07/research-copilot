from app.services.pdf_processor import (
    extract_pdf_pages
)

pages = extract_pdf_pages(
    "sample.pdf"
)

print(pages)