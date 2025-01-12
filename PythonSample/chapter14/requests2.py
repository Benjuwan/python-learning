import requests
r = requests.get('https://higpen.jellybean.jp/')
with open('download2.html', 'wb') as file:
    file.write(r.content)
