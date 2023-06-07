from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

# create connection string
SQLALCHEMY_DATABASE_URL = URL.create(
  "mysql+mysqlconnector",
  username=config.db_user,
  password=config.db_pass,
  host=config.db_host,
  database=config.db_name,
  port=3306
)

# create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session
Session_local = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()