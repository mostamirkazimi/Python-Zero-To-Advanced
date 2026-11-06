# نمونه ساختار جمع آوری اخبار

import requests

from bs4 import BeautifulSoup


url = "https://example.com"

response = requests.get(
    url
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headlines = soup.find_all(
    "h2"
)

for headline in headlines:

    print(
        headline.text
    )