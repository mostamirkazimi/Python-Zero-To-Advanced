from fastapi import FastAPI

app = FastAPI()


students = []


@app.post("/students")
def create_student(
    name: str
):

    students.append(name)

    return students


@app.get("/students")
def get_students():

    return students


@app.delete("/students/{index}")
def delete_student(
    index: int
):

    students.pop(index)

    return students