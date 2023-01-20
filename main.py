from fastapi import FastAPI, Body, Depends
from accounts.authentication.auth_bearer import JWTBearer
from accounts.authentication.auth_handler import signJWT
from accounts.model import Post, User, UserLogin
from accounts.schemas import PostSchemas, UserSchemas, UserLoginSchemas

from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_db():
    session = SessionLocal
    try:
        yield session
    finally:
        session.close()


"""
    Post: This is the Dummy data for testing 
"""
posts = [
    {
        "id": 1,
        "title": "my first blog",
        "text": "this is my first blog"
    },
    {
        "id": 2,
        "title": "my 2nd blog",
        "text": "this is my 2nd blog"
    },
    {
        "id": 3,
        "title": "my 3rd blog",
        "text": "this is my 3rd blog"
    },
]

users = []
app = FastAPI()

"""
    home: Just Checking , that api Works 
"""


@app.get("/", tags=["test"])
def home():
    return {"hello": "world!."}


"""
    check_user: validation of User, matching email and password for sign in
"""


def validate_user(data: UserLogin):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


"""
    route handlers
    testing
"""

"""
    get_posts: get all posts from DB
"""


@app.get("/posts", tags=["posts"])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


"""
    get_post: Get single Post From Database
"""


@app.get("/posts/{post_id}", tags=["posts"])
def get_post(post_id: int, db: Session = Depends(get_db)):
    queryset = db.query(Post).get(post_id)
    return queryset


"""
    create_post: Create single post
"""


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def create_post(post: PostSchemas, db: Session = Depends(get_db)):
    post_model = Post
    post_model.title = post.title
    post_model.content = post.content
    db.add(post_model)
    db.commit()
    return post
    # post.id = len(posts) + 1
    # posts.append(post.dict())
    # return {
    #     "data": "Successfully Post Created "
    # }


"""
    User Signup endpoint
"""


@app.post("/user/signup", tags=["user"])
def create_user(user: User = Body(...), db: Session = Depends(get_db)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)


"""
    User Signin endpoint
"""


@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin = Body(...), db: Session = Depends(get_db)):
    if validate_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong Credentials!"
    }
