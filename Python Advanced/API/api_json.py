import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

# تبدیل پاسخ به دیکشنری
data = response.json()

print(
    data["title"]
)

print(
    data["body"]
)
