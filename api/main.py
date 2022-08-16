from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import address, common, load

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(load.router, prefix="/user", tags=["user"])
app.include_router(load.router, prefix="/load", tags=["load"])
app.include_router(address.router, prefix="/address", tags=["address"])
app.include_router(common.router, prefix="/common", tags=["common"])
