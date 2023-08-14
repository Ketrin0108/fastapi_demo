from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    last_name: str
    first_name: str


class IdeaResponse(BaseModel):
    id: int
    idea: str