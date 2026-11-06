import requests

# اطلاعات جدید
data = {

    "id": 1,

    "title": "Updated",

    "body": "Updated Body",

    "userId": 1
}

response = requests.put(

    "https://jsonplaceholder.typicode.com/posts/1",

    json=data

)

print(
    response.json()
)