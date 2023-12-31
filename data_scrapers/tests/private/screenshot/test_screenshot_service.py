from sqlalchemy import select
from sqlalchemy.orm import Session

from private.game.model import Game
from private.screenshot.model import GameScreenshot
from private.screenshot.service import get_screenshots_in_steam_file_ids, save_screenshots


def test_save_screenshots은_입력한_스크린샷을_저장해야_한다(session: Session, saved_games: list[Game]):
    screenshots = [
        {"steam_file_id": 1, "url": "https://fake.url/1", "game_id": saved_games[0].id},
        {"steam_file_id": 2, "url": "https://fake.url/2", "game_id": saved_games[0].id},
        {"steam_file_id": 3, "url": "https://fake.url/3", "game_id": saved_games[1].id},
        {"steam_file_id": 4, "url": "https://fake.url/4", "game_id": saved_games[1].id},
    ]
    save_screenshots(session, screenshots)

    saved = session.scalars(select(GameScreenshot)).all()
    assert len(saved) == 4


def test_get_screenshots_in_steam_file_ids는_스크린샷을_반환해야_한다(session: Session, saved_screenshots: list[GameScreenshot]):
    file_ids = [s.steam_file_id for s in saved_screenshots[:2]]

    given = get_screenshots_in_steam_file_ids(session, file_ids)
    assert len(given) == 2
