from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
  __tablename__ = "user_info"

  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  full_name = Column(String, nullable=False)
  date_created = Column(DateTime(timezone=True), server_default=func.now())