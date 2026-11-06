# جستجو بر اساس کلاس

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

results = soup.find_all(
    class_="example"
)

for item in results:

    print(
        item.text
    )