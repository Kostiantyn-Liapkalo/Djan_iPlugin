from fastapi import HTTPException
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DatabaseError

from src.conf.config import settings

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Hello Andrii sdfdzddebhdhdh


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except HTTPException:  # noqa
        db.rollback()
    finally:
        db.close()
