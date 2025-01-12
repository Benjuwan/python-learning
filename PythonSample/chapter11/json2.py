import json
with open('catalog.json', encoding='utf-8') as file:
    print(json.load(file))
