from fastapi import APIRouter
from src.utils.resources import get_database

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/")
def get_documents():
    path = get_database()
    return {"document": path}
