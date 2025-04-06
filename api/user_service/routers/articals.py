from fastapi import APIRouter, Depends, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api.user_service.models import Artical, ArticalOut
from api.db.database import get_user_db, get_artical_db
from sqlalchemy.orm import Session
from psycopg2.errors import UniqueViolation

artical_router = APIRouter()


@artical_router.get('/get_articals', response_model=list[ArticalOut])
def get_articals(limit: int = 20,  offset:int = 0, db: Session = Depends(get_artical_db)):
    response = db.query(Artical).offset(offset=offset).limit(limit=limit).all()
    