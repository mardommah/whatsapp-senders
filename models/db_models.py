from sqlalchemy import Column, Integer, String, DateTime, VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import VARCHAR

Base = declarative_base()

class User(Base):
  __tablename__ = "user_info"

  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String(200), nullable=False)
  full_name = Column(String, nullable=False)
  date_created = Column(DateTime(timezone=True), server_default=func.now())