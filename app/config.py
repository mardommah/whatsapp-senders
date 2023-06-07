import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
  root_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  api_prefix: str = ("/api/v1" if not os.getenv("API_GATEWAY") else "/api/v1")

  api_key_kirim_wa: str = os.getenv("API_KEY_KIRIMWA")
  api_key: str = os.getenv("KEY")
  algorithm: str = os.getenv("ALGORITHM")
  secret_key: str = os.getenv("SECRET_KEY")

  # DATABASE
  db_host: str = os.getenv("DB_HOST")
  db_user: str = os.getenv("DB_USER")
  db_pass: str = os.getenv("DB_PASS")
  db_name: str = os.getenv("DB_NAME")


  class Config():
    env_file = ".env"

  
config = Config()