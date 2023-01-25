from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "exampl title",
                "content": "this is the example content"
            }
        }


class User(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Shakib",
                "email": "shakib@gmail.com",
                "password": "12345678"
            }
        }


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "shakib@gmail.com",
                "password": "12345678"
            }
        }
