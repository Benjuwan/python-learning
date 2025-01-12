catalog = []
while len(catalog) < 3:
    item = input('item: ')
    if item in catalog:
        print(item, 'is on the catalog.')
        continue
    catalog.append(item)
print('catalog:', catalog)
