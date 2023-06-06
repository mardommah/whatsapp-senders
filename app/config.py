import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
  root_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  api_prefix: str = ("/api/v1" if not os.getenv("API_GATEWAY") else "/api/v1")

  api_key_kirim_wa: str = os.getenv("API_KEY_KIRIMWA")
  api_key: str = os.getenv("KEY")


  class Config():
    env_file = ".env"

  
config = Config()