from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class Student(
    BaseModel
):

    name: str

    age: int


@app.get(
    "/student",
    response_model=Student
)
def get_student():

    return Student(

        name="Samiullah",

        age=25

    )