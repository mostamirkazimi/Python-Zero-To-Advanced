import requests

try:

    response = requests.get(

        "https://jsonplaceholder.typicode.com/posts",

        timeout=5

    )

    print(
        response.status_code
    )

except requests.Timeout:

    print(
        "زمان پاسخ تمام شد"
    )
