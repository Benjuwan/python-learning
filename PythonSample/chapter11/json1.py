import json
catalog = [{'name': 'hat', 'price': 2000},
           {'name': 'shirt', 'price': 1000}, 
           {'name': 'socks', 'price': 500}]
with open('catalog.json', 'w', encoding='utf-8') as file:
    json.dump(catalog, file, indent=4)
