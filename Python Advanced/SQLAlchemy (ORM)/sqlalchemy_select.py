# نمایش همه رکوردها

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
).all()

for student in students:

    print(
        student.id,
        student.name,
        student.age
    )