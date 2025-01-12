import openpyxl
book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = 'hat'
sheet['B1'] = 2000
book.save('catalog.xlsx')
