import requests

# اطلاعات ارسالی
data = {

    "title": "Python",

    "body": "Advanced Python",

    "userId": 1
}

# ارسال POST
response = requests.post(

    "https://jsonplaceholder.typicode.com/posts",

    json=data

)

print(
    response.json()
)