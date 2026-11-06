from fastapi import FastAPI

app = FastAPI()


@app.post("/students")
def create_student():

    return {
        "message": "Student Created"
    }