# ایجاد اتصال به دیتابیس SQLite

from sqlalchemy import create_engine


# ایجاد دیتابیس
engine = create_engine(

    "sqlite:///students.db",

    echo=True

)

print(
    "Database Connected Successfully"
)