from fastapi import FastAPI

app = FastAPI()


# Query Parameter
@app.get("/search")
def search(
    name: str
):

    return {
        "name": name
    }