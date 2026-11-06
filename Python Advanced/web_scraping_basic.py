# ارسال درخواست به وب‌سایت
import requests

# تجزیه HTML
from bs4 import BeautifulSoup


# دریافت صفحه
response = requests.get(
    "https://example.com"
)

# ساخت شیء BeautifulSoup
soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# نمایش عنوان صفحه
print(
    soup.title.text
)