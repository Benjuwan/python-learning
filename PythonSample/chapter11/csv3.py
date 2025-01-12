import csv
with open('catalog.csv', encoding='utf-8') as file:
    print([tuple(x) for x in csv.reader(file)])
