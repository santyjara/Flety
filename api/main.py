from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import load, vehicle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(load.router)
# app.include_router(vehicle.router)
