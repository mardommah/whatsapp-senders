from fastapi import APIRouter
from api.v1.send_wa.app import router as send_wa_router

v1api = APIRouter()

v1api.include_router(send_wa_router)