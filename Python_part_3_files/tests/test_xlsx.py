import os
from openpyxl import load_workbook


def test_xlsx():
    workbook = load_workbook(os.path.abspath('../resources/file_example_XLSX_50.xlsx'))
    sheet = workbook.active
    value = sheet.cell(row=3, column=2).value
    print(value)

    assert 'Mara' in value
