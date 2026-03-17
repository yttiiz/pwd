from src.config import settings
from typing import TypedDict, cast
import json


class Origins(TypedDict):
    origins: list[str]


def get_origins():
    """Retreive a list of 'origin' allowed to communicate with this API"""

    with open(settings.origins_path, "r") as file:
        content = cast(Origins, json.load(file))

    return content.get("origins", [])
