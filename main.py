from fastapi import FastAPI, Depends
from blog.model import Post
from blog.schemas import PostCreate

from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()


@app.get("/post")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@app.get("/post/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    return db.query(Post).get(post_id)


@app.post("/post")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    post_model = Post(**post.dict())
    db.add(post_model)
    db.commit()
    return post_model


@app.put("/post/{post_id}")
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    post_object = db.query(Post).get(post_id)
    post_object.title = post.title
    post_object.content = post.content
    db.commit()
    return post_object


@app.delete("/post/{post_id}")
def delete_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    post_object = db.query(Post).get(post_id)
    db.delete(post_object)
    db.commit()
    db.close()
    return "Post is deleted"
