from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import database
from src.utils import middleware

app = FastAPI()
origins = middleware.get_origins()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(database.router)
