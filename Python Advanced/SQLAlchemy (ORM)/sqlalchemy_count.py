# شمارش رکوردها

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy_models import Student


engine = create_engine(
    "sqlite:///students.db"
)

Session = sessionmaker(
    bind=engine
)

session = Session()

count = session.query(
    Student
).count()

print(
    count
)