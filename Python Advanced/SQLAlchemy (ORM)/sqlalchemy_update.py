# ویرایش اطلاعات

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

student = session.query(
    Student
).filter_by(
    id=1
).first()

student.age = 30

session.commit()

print(
    "Updated"
)