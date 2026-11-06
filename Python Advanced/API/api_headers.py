import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

# مشاهده Header ها
print(
    response.headers
)