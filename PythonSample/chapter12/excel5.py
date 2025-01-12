import openpyxl
book = openpyxl.load_workbook('catalog.xlsx')
sheet = book.active
for name, price in sheet.iter_rows(values_only=True):
    print(name, price)
