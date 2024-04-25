from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "success": True,
        "message": "home",
        "data": {}
    }


@app.get("/posts")
def all_posts():
    return {
        "success": True,
        "message": "all_posts",
        "data": {}
    }
