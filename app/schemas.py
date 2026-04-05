from pydantic import BaseModel
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


class GameBase(BaseModel):
    title: str
    platform: str
    genre: str
    price: Decimal
    developer: str
    release_date: date
    rating: str
    file_size_gb: Decimal
    multiplayer_support: bool


class GameCreate(GameBase):
    pass


class GameResponse(GameBase):
    id: int

    class Config:
        from_attributes = True


class PlayerBase(BaseModel):
    gamertag: str
    email: str
    region: str
    level: int
    avatar_url: Optional[str] = None
    achievements_unlocked: int = 0
    online_status: str
    friends_count: int = 0
    last_login: Optional[datetime] = None


class PlayerCreate(PlayerBase):
    pass


class PlayerResponse(PlayerBase):
    id: int

    class Config:
        from_attributes = True


class LibraryBase(BaseModel):
    game_id: int
    player_id: int
    activation_key: str
    purchase_date: date
    playtime_hours: Decimal = 0
    last_played: Optional[datetime] = None
    is_installed: bool
    download_progress: int = 0
    is_gift: bool


class LibraryCreate(LibraryBase):
    pass


class LibraryResponse(LibraryBase):
    id: int

    class Config:
        from_attributes = True