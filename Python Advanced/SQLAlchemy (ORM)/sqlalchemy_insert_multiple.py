# افزودن چند دانشجو

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

students = [

    Student(
        name="Ali",
        age=20
    ),

    Student(
        name="Sara",
        age=22
    ),

    Student(
        name="Omar",
        age=24
    )

]

session.add_all(
    students
)

session.commit()