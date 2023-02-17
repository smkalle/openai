

import requests
from bs4 import BeautifulSoup

url = 'https://www.shopify.com/login'

payload = {
    'login': '',
    'password': ''
}

with requests.Session() as s:
    p = s.post(url, data=payload)
    r = s.get('https://www.shopify.com/admin/products/8180873726')
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', {'class': 'product-form__item'})
    for item in data:
        print(item.text)