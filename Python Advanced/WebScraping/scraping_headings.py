# استخراج تیترها

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headings = soup.find_all(
    ["h1", "h2", "h3"]
)

for heading in headings:

    print(
        heading.text
    )