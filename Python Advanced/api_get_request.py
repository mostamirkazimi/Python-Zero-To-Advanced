# برای ارسال درخواست‌های HTTP
import requests


# ارسال درخواست GET
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

# تبدیل پاسخ به JSON
data = response.json()

# نمایش داده دریافتی
print(data)