from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.config import settings
from src.utils.resources import get_database

router = APIRouter(prefix="/database", tags=["documents"])


@router.get("/")
def database(api_key: str | None = None):
    """Retreive database"""

    if api_key != settings.api_key:
        raise HTTPException(
            status_code=403, detail="You are not authorized to get the resource."
        )

    return get_database()
