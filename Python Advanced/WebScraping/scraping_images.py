# استخراج تصاویر

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

images = soup.find_all(
    "img"
)

for image in images:

    print(
        image.get("src")
    )