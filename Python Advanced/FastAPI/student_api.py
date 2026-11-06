from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class Student(
    BaseModel
):

    name: str

    age: int


students = []


@app.post("/students")
def create_student(
    student: Student
):

    students.append(
        student
    )

    return {
        "message": "Student Added"
    }


@app.get("/students")
def get_students():

    return students