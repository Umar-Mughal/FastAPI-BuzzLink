from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def home():
    return {"success": True, "message": "home", "data": {}}


@app.get("/posts")
def get_posts():
    return {"success": True, "message": "all posts", "data": {}}


@app.post("/posts")
def create_post(payload: dict = Body):
    print(payload)
    return {"success": True, "message": "post created", "data": {}}
