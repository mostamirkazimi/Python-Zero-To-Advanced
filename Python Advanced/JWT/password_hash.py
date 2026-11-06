# هش کردن رمز عبور

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"]
)

password = "123456"

hashed = pwd_context.hash(
    password
)

print(hashed)