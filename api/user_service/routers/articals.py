from fastapi import APIRouter, Depends, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api.user_service.models import Artical
from api.db.database import get_user_db, get_artical_db
from sqlalchemy.orm import Session
from psycopg2.errors import UniqueViolation
import time
from datetime import datetime


artical_router = APIRouter()


@artical_router.get('/get_articals')
def get_articals(limit: int = 20,  offset:int = 0, db: Session = Depends(get_artical_db)):
    articals = db.query(Artical).offset(offset=offset).limit(limit=limit).all()
    response = [artical.to_dict() for artical in articals] 
    return response


@artical_router.post('/add_articals')
def add_articals(articals:dict, db: Session = Depends(get_artical_db)):
    for url, artical in articals.items():
        db_row = Artical(url = url, title=artical["title"], description = artical['desc'])

        db.add(db_row)
        db.commit()
        db.refresh(db_row)

    else:
        return JSONResponse(content={'message':'Статьи добавлены'}, status_code=200)
