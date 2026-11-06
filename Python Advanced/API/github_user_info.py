import requests

username = "octocat"

response = requests.get(
    f"https://api.github.com/users/{username}"
)

data = response.json()

print(
    "Name:",
    data["name"]
)

print(
    "Public Repos:",
    data["public_repos"]
)

print(
    "Followers:",
    data["followers"]
)