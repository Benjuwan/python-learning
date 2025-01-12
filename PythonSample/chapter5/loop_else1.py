catalog = []
while len(catalog) < 3:
    item = input('item: ')
    if item in catalog:
        print(item, 'is on the catalog.')
        break
    catalog.append(item)
else:
    print('catalog:', catalog)
