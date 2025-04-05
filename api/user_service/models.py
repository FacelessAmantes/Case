from sqlalchemy import Column, Integer, String
from api.db.database import Base, users_engine




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)


Base.metadata.create_all(bind=users_engine)
