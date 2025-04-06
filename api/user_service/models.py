from sqlalchemy import Column, Integer, String
from api.db.database import user_base, users_engine, artical_base, articals_engine
from pydantic import BaseModel
from datetime import date


class User(user_base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

class Artical(artical_base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)

class ArticalIn(BaseModel):
    title: str
    description: str
    url: str
    datetime:date

class ArticalOut(Artical):
    datetime:date
    
user_base.metadata.create_all(bind=users_engine)
artical_base.metadata.create_all(bind=articals_engine)

