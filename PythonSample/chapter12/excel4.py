import openpyxl
book = openpyxl.load_workbook('catalog.xlsx')
sheet = book.active
catalog = [('hat', 2000), ('shirt', 1000), 
           ('socks', 500)]
for i, (name, price) in enumerate(catalog, 1):
    sheet[f'A{i}'] = name
    sheet[f'B{i}'] = price
book.save('catalog.xlsx')
