from sqlalchemy import create_engine
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
db_path= BASE_DIR/"data"/"app.db"
db_url=f"sqlite:///{db_path}"

engine=create_engine(url=db_url, connect_args={"check_same_thread": False})

