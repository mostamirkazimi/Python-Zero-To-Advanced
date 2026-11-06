# استخراج تمام پاراگراف ها

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# پیدا کردن تمامی تگ های p
paragraphs = soup.find_all("p")


for p in paragraphs:

    print(
        p.text
    )