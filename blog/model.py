from sqlalchemy import Column, Integer, String
from database import Base


class Post(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    content = Column(String(256))

    class Config:
        schema_extra = {
            "example": {
                "title": "exampl title",
                "content": "this is the example content"
            }
        }
