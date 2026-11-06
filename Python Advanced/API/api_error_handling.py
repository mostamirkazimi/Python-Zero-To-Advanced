import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    print(
        response.json()
    )

except requests.exceptions.HTTPError:

    print(
        "خطای HTTP"
    )

except requests.exceptions.ConnectionError:

    print(
        "خطای اتصال"
    )

except requests.exceptions.Timeout:

    print(
        "اتمام زمان انتظار"
    )

except requests.exceptions.RequestException as error:

    print(error)