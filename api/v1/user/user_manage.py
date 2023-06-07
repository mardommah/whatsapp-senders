from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from helper import crud
from models import db_models
from schemas import message_schemas
from database.db import engine, Session_local

db_models.Base.metadata.create_all(bind=engine)


router = APIRouter(prefix="user", tags=["User Management"])

@router.post("/user", response_model=message_schemas.UserInfo)
def create_user(
  user: message_schemas.UserInfo, 
  db: Session = Depends(crud.get_db)
):
  # check user database
  db_user = crud.get_user_by_username(db, username=user.username)
  if db_user:
    raise HTTPException(status_code=400, detail="Username already registered")
  return crud.create_user(db=db, user=user)
