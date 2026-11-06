from fastapi import FastAPI

app = FastAPI()


# دریافت شناسه از URL
@app.get("/student/{student_id}")
def get_student(
    student_id: int
):

    return {
        "id": student_id
    }