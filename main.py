from fastapi import FastAPI
from src.routes import documents

app = FastAPI()
app.include_router(documents.router)
