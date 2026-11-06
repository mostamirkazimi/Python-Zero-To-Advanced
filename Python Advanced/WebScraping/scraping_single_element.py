# پیدا کردن اولین عنصر

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

title = soup.find("h1")

print(
    title.text
)