from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def get_documents():
    return {"document": "maco"}
