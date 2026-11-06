# ساخت JWT Token

from jose import jwt

SECRET_KEY = "mysecretkey"

data = {
    "username": "Samiullah"
}

token = jwt.encode(
    data,
    SECRET_KEY,
    algorithm="HS256"
)

print(token)