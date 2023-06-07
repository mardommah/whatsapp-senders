from sqlalchemy import Column, Integer, String
from database.db import Base

class User(Base):
  __table__name = "user_info"

  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  username = Column(String, unique=True)
  password = Column(String)
  full_name = Column(String)

