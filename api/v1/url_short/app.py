from fastapi import APIRouter, HTTPException, Depends
from schemas import short_url
import validators
import secrets

from sqlalchemy.orm import Session

from app.config import config
from helper import crud
from models import db_models


router = APIRouter(prefix="/short", tags=["Short URL"])


@router.post("/url")
def create_url(url: short_url.URLBase, db: Session = Depends(crud.get_db)):
  if not validators.url(url.target_url):
    raise HTTPException(status_code=400, detail="invalid url")

  
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  key = "".join(secrets.choice(chars) for _ in range(5))
  secret_key = "".join(secrets.choice(chars) for _ in range(8))
  db_url = db_models.URL(
    target_url = url.target_url, key=key, secret_key=secret_key
  )

  # add to database
  db.add(db_url)
  db.commit()
  db.refresh(db_url)
  db_url.url = key
  db_url.admin_url = secret_key

  return db_url