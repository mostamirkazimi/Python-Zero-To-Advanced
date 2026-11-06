from sqlalchemy import *

from sqlalchemy.orm import *

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    age = Column(
        Integer
    )


engine = create_engine(
    "sqlite:///school.db"
)

Base.metadata.create_all(
    engine
)

Session = sessionmaker(
    bind=engine
)

session = Session()

student = Student(
    name="Samiullah",
    age=25
)

session.add(student)

session.commit()

print(
    "Student Saved"
)