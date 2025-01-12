from urllib.request import urlopen
with urlopen('https://higpen.jellybean.jp/') as file:
    for line in file:
        print(str(line, encoding='utf-8'), end='')
