# استخراج عنوان سایت

import requests

from bs4 import BeautifulSoup


# دریافت صفحه
response = requests.get(
    "https://example.com"
)

# پردازش HTML
soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# نمایش عنوان
print(
    soup.title.text
)