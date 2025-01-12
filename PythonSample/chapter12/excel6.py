import openpyxl
book = openpyxl.load_workbook('catalog.xlsx')
sheet = book.active
total = 0
for i, (name, price) in enumerate(
        sheet.iter_rows(values_only=True), 1):
    if not price:
        continue
    if name == 'Total':
        break
    total += price
else:
    i += 2
sheet[f'A{i}'] = 'Total'
sheet[f'B{i}'] = total
book.save('catalog.xlsx')
