from pydantic import BaseModel, Field


class PostSchemas(BaseModel):
    title: str = Field(...)
    content: str = Field(...)


class UserSchemas(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)


class UserLoginSchemas(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
