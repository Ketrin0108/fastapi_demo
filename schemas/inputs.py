from pydantic import BaseModel


class IdeaBase(BaseModel):
    idea: str

class IdeaCreate(IdeaBase):
    pass


