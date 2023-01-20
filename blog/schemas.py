from pydantic import BaseModel, Field


class PostSchemas(BaseModel):
    title: str = Field(...)
    content: str = Field(...)


