from datetime import timedelta, datetime
import jwt

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