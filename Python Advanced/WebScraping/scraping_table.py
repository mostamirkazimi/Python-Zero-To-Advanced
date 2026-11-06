# استخراج جدول

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

rows = soup.find_all(
    "tr"
)

for row in rows:

    columns = row.find_all(
        "td"
    )

    for col in columns:

        print(
            col.text
        )