import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.python.org/downloads/')

release = []
soup = BeautifulSoup(r.text, 'html.parser')

for li in soup.find_all('li'):
    if x := li.find('span', class_='release-number'):
        if y := x.find('a'):
            if z := li.find('span', class_='release-date'):
                release.append((y.text, z.text))

release.sort()
for name, date in release:
    print(f'{name:15}{date}')
