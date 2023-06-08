from datetime import timedelta, datetime
import jwt
from sqlalchemy.orm import Session
from helper.crud import get_user_by_username
from fastapi import HTTPException

from app.config import config

def create_access_token(*, data: dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=60)
  to_encode.update({
    "exp": expire
  })

  encoded_jwt = jwt.encode(payload=to_encode, key=config.secret_key, algorithm=config.algorithm) 

  return encoded_jwt


# decode user password
def decode_user_token(db: Session, token: str):
  try:
    decoded_data = jwt.decode(jwt=token, key=config.secret_key, algorithms=config.algorithm)
  except:
    raise HTTPException(status_code=400, detail="invalid token type")
  #check if username is exist
  check_user = get_user_by_username(db, username=decoded_data["sub"])

  if check_user.username == decoded_data["sub"]:
    return "ok"
  else:
    raise HTTPException(status_code=400, detail="invalid token")