import os

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from services.idea import IdeaService
from dotenv import load_dotenv

load_dotenv()
SQL_URL = os.environ.get("SQL_URL")

engine = create_engine(SQL_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_idea_service(db: Session = Depends(get_db)) -> IdeaService:
    return IdeaService(db=db)