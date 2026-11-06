# ذخیره اطلاعات در فایل

import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

with open(
    "output.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        soup.get_text()
    )

print(
    "اطلاعات ذخیره شد"
)
