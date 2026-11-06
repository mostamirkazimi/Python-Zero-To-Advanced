from fastapi import FastAPI

app = FastAPI()


# دریافت اطلاعات
@app.get("/students")
def get_students():

    return [

        {
            "id": 1,
            "name": "Ali"
        },

        {
            "id": 2,
            "name": "Samiullah"
        }

    ]