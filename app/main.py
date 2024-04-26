from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
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
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"success": True, "message": "all posts", "data": posts}


@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    return {"success": True, "message": "single post", "data": {}}
