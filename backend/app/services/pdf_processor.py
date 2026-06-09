from pypdf import PdfReader


def extract_pdf_text(
    file_path: str
) -> str:

    reader = PdfReader(
        file_path
    )

    text = ""

    for page in reader.pages:

        page_text = (
            page.extract_text()
        )

        if page_text:
            text += (
                page_text + "\n"
            )

    return text


def extract_pdf_pages(
    file_path: str
):

    reader = PdfReader(
        file_path
    )

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