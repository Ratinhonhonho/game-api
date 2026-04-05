# API REST de Jogos de Videogame

## Integrantes
- Renato
- Sara

## Descrição do projeto

Esta API REST foi desenvolvida para simular uma plataforma de jogos de videogame.
O sistema permite cadastrar jogos, jogadores e registros da biblioteca de jogos adquiridos pelos jogadores.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn

## Recursos da API

A aplicação possui 3 recursos principais:

### 1. Games

Responsável pelo catálogo de jogos disponíveis.

Campos:
- id
- title
- platform
- genre
- price
- developer
- release_date
- rating
- file_size_gb
- multiplayer_support

### 2. Players

Responsável pelo cadastro dos jogadores.

Campos:
- id
- gamertag
- email
- region
- level
- avatar_url
- achievements_unlocked
- online_status
- friends_count
- last_login

### 3. Library

Responsável pelos registros da biblioteca de jogos dos jogadores.

Campos:
- id
- game_id
- player_id
- activation_key
- purchase_date
- playtime_hours
- last_played
- is_installed
- download_progress
- is_gift

## Como executar o projeto

### 1. Clonar o repositório
```bash
git clone URL_DO_REPOSITORIO
cd game_api
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados no MySQL

No MySQL Workbench, executar:
```sql
CREATE DATABASE game_api;
USE game_api;
```

### 5. Criar as tabelas

Após criar o banco, criar as tabelas `games`, `players` e `library` conforme a estrutura do projeto.

### 6. Configurar a conexão com o banco

No arquivo `app/database.py`, ajustar usuário e senha do MySQL:
```python
DATABASE_URL = "mysql+pymysql://root:SUA_SENHA@localhost/game_api"
```

### 7. Rodar a aplicação
```bash
uvicorn app.main:app --reload
```

## Como acessar

- API local: http://127.0.0.1:8000
- Documentação Swagger: http://127.0.0.1:8000/docs

## Endpoints principais

### Games
- `POST /games`
- `GET /games`
- `GET /games/{game_id}`
- `PUT /games/{game_id}`
- `DELETE /games/{game_id}`

### Players
- `POST /players`
- `GET /players`
- `GET /players/{player_id}`
- `PUT /players/{player_id}`
- `DELETE /players/{player_id}`

### Library
- `POST /library`
- `GET /library`
- `GET /library/{entry_id}`
- `PUT /library/{entry_id}`
- `DELETE /library/{entry_id}`

## Exemplos de uso

### Criar um jogo
```json
{
  "title": "Elden Ring",
  "platform": "PC",
  "genre": "RPG",
  "price": 299.90,
  "developer": "FromSoftware",
  "release_date": "2022-02-25",
  "rating": "18+",
  "file_size_gb": 60.5,
  "multiplayer_support": true
}
```

### Criar um jogador
```json
{
  "gamertag": "PlayerOne_99",
  "email": "playerone@email.com",
  "region": "SA",
  "level": 10,
  "avatar_url": "https://example.com/avatar.png",
  "achievements_unlocked": 5,
  "online_status": "Online",
  "friends_count": 12,
  "last_login": "2026-04-05T20:30:00"
}
```

### Criar um registro na biblioteca
```json
{
  "game_id": 5,
  "player_id": 1,
  "activation_key": "AAAA-BBBB-CCCC",
  "purchase_date": "2026-04-05",
  "playtime_hours": 12.5,
  "last_played": "2026-04-05T21:00:00",
  "is_installed": true,
  "download_progress": 100,
  "is_gift": false
}
```

## Observações

- O projeto utiliza MySQL como banco de dados.
- A documentação interativa pode ser acessada pela rota `/docs`.
- Os testes dos endpoints podem ser feitos diretamente no Swagger.

## URL de deploy

> DATABASE_URL = "mysql+pymysql://root:SUA_SENHA_AQUI@localhost/game_api"