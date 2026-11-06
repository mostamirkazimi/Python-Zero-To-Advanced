# وارد کردن FastAPI

from fastapi import FastAPI


# ساخت برنامه
app = FastAPI()


# اولین Route
@app.get("/")
def home():

    return {
        "message": "Hello FastAPI"
    }