from fastapi import APIRouter
from api.v1 import v1api
from app.config import config

v1_router = APIRouter(prefix=config.api_prefix)

v1_router.include_router(v1api)