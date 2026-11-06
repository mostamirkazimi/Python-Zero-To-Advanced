import requests

# دریافت تمام پست‌ها
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

posts = response.json()

# نمایش 5 پست اول
for post in posts[:5]:

    print(post)