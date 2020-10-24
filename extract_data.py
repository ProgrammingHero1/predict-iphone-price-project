import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IPhone'
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1::1]

d = {}

for row in rows:
    data = row.find_all(['th', 'td'])
    try:
        version_text = data[0].a.text.split('/')[0]
        version_text = ''.join(i for i in version_text if i.isdigit())
        version = int(version_text)
        if version < 3:
            continue

        price_text = data[8]
        price = price_text.text.split('/')[-1].split('*')[-1].replace('$', '').replace('\n', '')
        d[version] = int(price)
    except:
        pass

csv = open('iphone_price.csv', 'a')
csv.write('version,price\n')

for key in d:
    csv.write(f"{key},{d[key]}\n")

csv.close()
