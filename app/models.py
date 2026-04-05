from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime, Boolean, ForeignKey
from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False)
    genre = Column(String(50), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    developer = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    rating = Column(String(20), nullable=False)
    file_size_gb = Column(DECIMAL(5, 2), nullable=False)
    multiplayer_support = Column(Boolean, nullable=False)


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    gamertag = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    region = Column(String(20), nullable=False)
    level = Column(Integer, nullable=False)
    avatar_url = Column(String(250))
    achievements_unlocked = Column(Integer, default=0)
    online_status = Column(String(20), nullable=False)
    friends_count = Column(Integer, default=0)
    last_login = Column(DateTime)


class Library(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    activation_key = Column(String(50), nullable=False)
    purchase_date = Column(Date, nullable=False)
    playtime_hours = Column(DECIMAL(8, 2), default=0)
    last_played = Column(DateTime)
    is_installed = Column(Boolean, nullable=False)
    download_progress = Column(Integer, default=0)
    is_gift = Column(Boolean, nullable=False)