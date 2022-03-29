from django.template import engines
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings

SQLALCHEMY_DATABASE_URL =   settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#use dependency injection
#allow use test and prod db
#during test override this and change db client
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()