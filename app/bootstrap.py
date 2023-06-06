from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import v1_router


Bootstrap = FastAPI()


Bootstrap.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

Bootstrap.include_router(v1_router)