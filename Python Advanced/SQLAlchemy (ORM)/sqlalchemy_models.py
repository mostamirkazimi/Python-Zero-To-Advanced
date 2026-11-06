# ساخت مدل دیتابیس

from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine
)

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
    "sqlite:///students.db"
)

Base.metadata.create_all(
    engine
)

print(
    "Table Created"
)