# اضافه کردن اطلاعات

from sqlalchemy import (
    create_engine
)

from sqlalchemy.orm import (
    sessionmaker
)

from sqlalchemy_models import (
    Student,
    Base
)


engine = create_engine(
    "sqlite:///students.db"
)

Session = sessionmaker(
    bind=engine
)

session = Session()


student = Student(

    name="Samiullah",

    age=25

)

session.add(
    student
)

session.commit()

print(
    "Student Added"
)