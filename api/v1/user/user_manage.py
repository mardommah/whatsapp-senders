from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta

from sqlalchemy.orm import Session

from helper import crud
from models import db_models
from schemas import message_schemas
from database.db import engine, Session_local

from app.config import config
from dependency.access_token import create_access_token, decode_user_token

db_models.Base.metadata.create_all(bind=engine)


router = APIRouter(prefix="/user", tags=["User Management"])

@router.post("/create", response_model=message_schemas.UserInfo)
def create_user(
  user: message_schemas.UserCreate, 
  db: Session = Depends(crud.get_db)
):
  # check user database
  db_user = crud.get_user_by_username(db, username=user.username)
  if db_user:
    raise HTTPException(status_code=400, detail="Username already registered")
  return crud.create_user(db=db, user=user)



@router.post("/auth", response_model=message_schemas.Token)
def auth_user(
  user: message_schemas.UserAuthenticate, 
  db: Session = Depends(crud.get_db)
):
  db_user = crud.get_user_by_username(db, username=user.username)
  if db_user is None:
    raise HTTPException(status_code=400, detail="Username not existed")
  else:
    is_password_correct = crud.check_user_pass(db, user)
    if is_password_correct is False:
      raise HTTPException(status_code=400, detail="Password is not corect")
    else:
      access_token_expires = timedelta(minutes=config.access_token_expire_time)
      # create access token 
      access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
      )

      return {
        "access_token": access_token,
        "token_type": "Bearer"
      }


@router.post("/decode")
def decode_jwt_token(
  bearer_token: str, 
  db: Session = Depends(crud.get_db)
):
  decode_token = decode_user_token(db, token=bearer_token)
  return decode_token
