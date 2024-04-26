from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field
    rating: Optional[int] = None


@app.get("/")
def home():
    return {"success": True, "message": "home", "data": {}}


@app.post("/posts")
def create_post(post: Post):
    print(post.dict())
    return {"success": True, "message": "post created", "data": {}}


@app.get("/posts")
def get_posts():
    return {"success": True, "message": "all posts", "data": {}}


@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    return {"success": True, "message": "single post", "data": {}}
