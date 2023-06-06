# simple key checker
from fastapi import Security, HTTPException
from app.config import config
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="API key token", auto_error=False)


def check_key(key:str):
  if key != config.api_key:
    return "Wrong Key"
  else:
    pass


async def get_api_key(api_key_header: str = Security(api_key_header)):
  if api_key_header == config.api_key:
      return api_key_header   
  else:
      raise HTTPException(
          status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
      )