from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from src.config import settings
import os


def get_database():
    """Retreive `database` file"""

    path = settings.pwd_database_path

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Database file not found")

    return FileResponse(
        path,
        media_type="application/octet-stream",
        filename="database.kdbx",
    )
