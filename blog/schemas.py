from pydantic import BaseModel, Field


class PostSchemas(BaseModel):
    title: str
    content: str


class PostCreate(PostSchemas):
    pass
