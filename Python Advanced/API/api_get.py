# ارسال درخواست GET

import requests

# دریافت داده از API
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

# تبدیل پاسخ به JSON
data = response.json()

# نمایش نتیجه
print(data)