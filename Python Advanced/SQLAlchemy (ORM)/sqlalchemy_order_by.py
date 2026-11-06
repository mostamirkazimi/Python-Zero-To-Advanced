# مرتب سازی

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

students = session.query(
    Student
).order_by(
    Student.age
).all()

for student in students:

    print(
        student.name,
        student.age
    )