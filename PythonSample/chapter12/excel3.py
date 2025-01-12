import openpyxl
book = openpyxl.load_workbook('catalog.xlsx')
sheet = book.active
print(sheet['A1'].value, sheet['B1'].value)
