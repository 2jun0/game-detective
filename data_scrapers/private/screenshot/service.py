from collections import OrderedDict
from typing import Any, Iterable

from sqlalchemy.orm import Session

from . import repository
from .model import GameScreenshot


def save_screenshots(session: Session, screenshots: Iterable[dict[str, Any]]):
    screenshots_ = [GameScreenshot(**s) for s in screenshots]
    session.add_all(screenshots_)


def get_screenshots_in_steam_file_ids(session: Session, file_ids: Iterable[int]) -> list[OrderedDict[str, Any]]:
    screenshots = repository.get_game_screenshots_in_steam_file_ids(session, file_ids)

    return [s.to_json() for s in screenshots]