# استخراج تمامی لینک ها

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# پیدا کردن تمام لینک ها
links = soup.find_all("a")


for link in links:

    print(
        link.get("href")
    )