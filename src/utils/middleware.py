import json
from typing import TypedDict, cast

from src.config import settings


class Origins(TypedDict):
    origins: list[str]


def get_origins() -> list[str]:
    """Retreive a list of 'origin' allowed to communicate with this API"""
    try:
        with open(settings.origins_path, "r") as file:
            content = cast(Origins, json.load(file))
        return content.get("origins", [])
    except FileNotFoundError:
        return []
