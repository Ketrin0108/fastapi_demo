
from models import Idea
from schemas.inputs import IdeaCreate


class IdeaService:

    def __init__(self, db):
        self.__db = db

    def create_idea(self, idea: IdeaCreate):
        idea_db = Idea(idea=idea)
        self.__db.add(idea_db)
        self.__db.commit()
        self.__db.refresh(idea_db)