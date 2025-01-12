import csv
catalog = [('hat', 2000), ('shirt', 1000), ('socks', 500)]
with open('catalog.csv', 'w', encoding='utf-8', 
          newline='') as file:
    csv.writer(file).writerows(catalog)
