from fastapi import FastAPI, Depends
from blog.model import Post
from blog.schemas import PostSchemas

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



