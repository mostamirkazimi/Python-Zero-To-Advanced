import requests

# پارامترهای URL
params = {

    "userId": 1
}

response = requests.get(

    "https://jsonplaceholder.typicode.com/posts",

    params=params

)

print(
    response.url
)

print(
    response.json()
)