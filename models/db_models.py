from sqlalchemy import Column, Integer, String, DateTime, VARCHAR, Boolean
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



class URL(Base):
  __tablename__ = "short_link"

  id = Column(Integer, primary_key=True, autoincrement=True)
  key = Column(String, unique=True, index=True)
  secret_key = Column(String, unique=True, index=True)
  target_url = Column(String, index=True)
  is_active = Column(Boolean, default=True)
  clicks = Column(Integer, default=0)


class DataPembeli(Base):
  __tablename__ = "data_pembelian"

  id = Column(Integer, primary_key=True, autoincrement=True)
  order_id = Column(Integer)
  product_name = Column(String(200))
  order_total = Column(Integer)
  payment_method = Column(String(50))
  first_name = Column(String(50))
  last_name = Column(String(50))
  address = Column(String(250))
  city = Column(String(50))
  post_code = Column(String(50))
  email = Column(String(100))
  phone = Column(String(30))
  date_created = Column(String(30))

  

  