import os
from pypdf import PdfReader
from .conftest import path_res


def test_pdf():
    reader = PdfReader(os.path.join(path_res, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert 'consultant' in text
    assert 412 == number_of_pages
