import glob
total = 0
for x in glob.glob('catalog.*'):
    with open(x, encoding='utf-8') as file:
        s = file.read()
        n = s.count('\n')+1 if len(s) else 0
        print(f'{x:15}{n:5}')
        total += n
print('-'*20)
print(f'{"Total":15}{total:5}')
