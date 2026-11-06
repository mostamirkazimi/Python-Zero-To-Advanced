from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {
        "page": "Home"
    }


@app.get("/about")
def about():

    return {
        "page": "About"
    }


@app.get("/contact")
def contact():

    return {
        "page": "Contact"
    }