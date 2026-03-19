import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.port)
