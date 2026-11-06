# خواندن Token

from jose import jwt

SECRET_KEY = "mysecretkey"

token = input("Token: ")

payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print(payload)