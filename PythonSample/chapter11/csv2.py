import csv
with open('catalog.csv', encoding='utf-8') as file:
    for row in csv.reader(file):
        print(row)
