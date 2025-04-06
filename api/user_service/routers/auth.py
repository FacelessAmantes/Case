from fastapi import APIRouter, Depends, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api.user_service.models import User
from api.db.database import get_user_db 
import bcrypt
from sqlalchemy.orm import Session
from psycopg2.errors import UniqueViolation

router = APIRouter()


@router.post("/registration")
async def register(username: str,email:str, password: str, db: Session = Depends(get_user_db)):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, hashed_password=hashed_password.decode('utf-8'), email=email)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return JSONResponse(content={'message':'Пользователь зарегестрировался'}, status_code=200)
    except UniqueViolation:
        return JSONResponse(content={'message':"Пользователь с таким email уже существует"},status_code=401)

@router.post("/authorisation")
async def authorize(username: str, password: str, db: Session = Depends(get_user_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=402, detail="User not found")

    if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return JSONResponse(content={"message": "Авторизация прошла успешно"},status_code=200)


@router.get("/get_users")
async def register(db: Session = Depends(get_user_db)):
    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # new_user = User(username=username, hashed_password=hashed_password.decode('utf-8'), email=email)
    # print(new_user)
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    
    return db.query(User).all() 
    
