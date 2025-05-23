from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_config ={"driver": "postgresql",
        'host':"localhost",
        "password":'123456789',
        "port":5432,
        'username':'postgres',
        'dbname':"users"}
USERS_DATABASE_URL = f"{db_config['driver']}://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

users_engine = create_engine(USERS_DATABASE_URL, echo=True)
users_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=users_engine)
user_base = declarative_base()


def get_user_db():
    db = users_SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_config ={"driver": "postgresql",
        'host':"localhost",
        "password":'123456789',
        "port":5432,
        'username':'postgres',
        'dbname':"articals"}


ARTICLAS_DATABASE_URL = f"{db_config['driver']}://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

articals_engine = create_engine(USERS_DATABASE_URL, echo=True)
articals_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=articals_engine)
artical_base = declarative_base()


def get_artical_db():
    db = articals_SessionLocal()
    try:
        yield db
    finally:
        db.close()