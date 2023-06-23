from pypdf import PdfReader

pdf = PdfReader('resources/docs-pytest-org-en-latest.pdf')
num_pages = len(pdf.pages)
print(num_pages)
page_0 = pdf.pages[0]
page_0_text = page_0.extract_text()
print(page_0_text)
assert '2022' in page_0_text
