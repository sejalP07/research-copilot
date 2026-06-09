from pypdf import PdfReader


def extract_pdf_pages(
    file_path: str
):
    reader = PdfReader(file_path)

    pages = []

    for page_num, page in enumerate(
        reader.pages,
        start=1
    ):
        text = page.extract_text()

        if text:
            pages.append(
                {
                    "page": page_num,
                    "text": text
                }
            )

    return pages