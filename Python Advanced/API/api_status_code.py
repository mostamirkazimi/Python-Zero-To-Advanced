import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

# نمایش کد وضعیت
print(
    "Status Code:",
    response.status_code
)

# نمایش نتیجه بررسی
print(
    response.ok
)