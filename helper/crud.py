from sqlalchemy.orm import Session
from models import db_models
from schemas import message_schemas
from database.db import Session_local
import bcrypt

# query username
def get_user_by_username(db: Session, username:str):
  return db.query(db_models.User).filter(db_models.User.username == username).first()

# create user
def create_user(db: Session, user: message_schemas.UserCreate):
  hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
  db_user = db_models.User(username=user.username, password=hashed_password, full_name=user.full_name)

  # add to data base
  db.add(db_user)

  # commit to accept data save
  db.commit()

  # refresh database
  db.refresh(db_user)

  # return result
  return db_user


# decrypt user pasword
def check_user_pass(db:Session, user: message_schemas.UserAuthenticate):
  db_user_info: db_models.User = get_user_by_username(db, username=user.username)
  return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))



def get_db():
  db = None
  try:
    db = Session_local()
    yield db
  finally:
    db.close()