from collections.abc import Generator
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine import URL
from src.infrastructure.db.config import db_settings

url_object = URL.create(
    "postgresql+psycopg2",
    username=db_settings.DATABASE_USERNAME,
    password=db_settings.DATABASE_PASSWORD,
    host=db_settings.DATABASE_HOST,
    database=db_settings.DATABASE_NAME,
)
engine = create_engine(url_object, echo=True)
