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


@app.get("/")
def home():
    return {"success": True, "message": "home", "data": {}}


@app.post("/posts")
def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()  # saved to db
    db.refresh(new_post)  # get saved post to new_post variable
    return {"success": True, "message": "post created", "data": new_post}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"success": True, "message": "all posts", "data": posts}


@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    return {"success": True, "message": "single post", "data": post}


@app.delete("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        return {"success": True, "message": "post does not exist", "data": None}
    post.delete()
    db.commit()
    return {"success": True, "message": "single post", "data": None}


@app.put("/posts/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if post_query.first() == None:
        return {"success": True, "message": "post does not exist", "data": None}
    post_query.update(post.dict())
    db.commit()
    return {"success": True, "message": "single post", "data": post_query.first()}


@app.delete("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        return {"success": True, "message": "post does not exist", "data": None}
    post.delete()
    db.commit()
    return {"success": True, "message": "single post", "data": None}
