from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

API_TOKEN = "somente-permitido-matheus-linhares-123"


def verify_api_token(x_api_token: str = Header(None)):
    if x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "API de jogos funcionando"}


@app.post("/games", response_model=schemas.GameResponse, status_code=201)
def create_game(
    game: schemas.GameCreate,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    db_game = models.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


@app.get("/games", response_model=list[schemas.GameResponse])
def list_games(db: Session = Depends(get_db)):
    return db.query(models.Game).all()


@app.get("/games/{game_id}", response_model=schemas.GameResponse)
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return game


@app.put("/games/{game_id}", response_model=schemas.GameResponse)
def update_game(game_id: int, game_data: schemas.GameCreate, db: Session = Depends(get_db)):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    for key, value in game_data.model_dump().items():
        setattr(game, key, value)

    db.commit()
    db.refresh(game)
    return game


@app.delete("/games/{game_id}")
def delete_game(
    game_id: int,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    db.delete(game)
    db.commit()
    return {"message": "Jogo removido com sucesso"}


@app.post("/players", response_model=schemas.PlayerResponse, status_code=201)
def create_player(
    player: schemas.PlayerCreate,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    db_player = models.Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


@app.get("/players", response_model=list[schemas.PlayerResponse])
def list_players(db: Session = Depends(get_db)):
    return db.query(models.Player).all()


@app.get("/players/{player_id}", response_model=schemas.PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return player


@app.put("/players/{player_id}", response_model=schemas.PlayerResponse)
def update_player(player_id: int, player_data: schemas.PlayerCreate, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")

    for key, value in player_data.model_dump().items():
        setattr(player, key, value)

    db.commit()
    db.refresh(player)
    return player


@app.delete("/players/{player_id}")
def delete_player(
    player_id: int,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")

    db.delete(player)
    db.commit()
    return {"message": "Jogador removido com sucesso"}


@app.post("/library", response_model=schemas.LibraryResponse, status_code=201)
def create_library_entry(
    entry: schemas.LibraryCreate,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    db_entry = models.Library(**entry.model_dump())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@app.get("/library", response_model=list[schemas.LibraryResponse])
def list_library(db: Session = Depends(get_db)):
    return db.query(models.Library).all()


@app.get("/library/{entry_id}", response_model=schemas.LibraryResponse)
def get_library_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Library).filter(models.Library.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Registro da biblioteca não encontrado")
    return entry


@app.put("/library/{entry_id}", response_model=schemas.LibraryResponse)
def update_library_entry(entry_id: int, entry_data: schemas.LibraryCreate, db: Session = Depends(get_db)):
    entry = db.query(models.Library).filter(models.Library.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Registro da biblioteca não encontrado")

    for key, value in entry_data.model_dump().items():
        setattr(entry, key, value)

    db.commit()
    db.refresh(entry)
    return entry


@app.delete("/library/{entry_id}")
def delete_library_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_token)
):
    entry = db.query(models.Library).filter(models.Library.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Registro da biblioteca não encontrado")

    db.delete(entry)
    db.commit()
    return {"message": "Registro da biblioteca removido com sucesso"}