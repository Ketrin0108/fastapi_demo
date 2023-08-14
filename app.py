import os
from typing import List

import uvicorn

from fastapi import FastAPI, Depends, HTTPException, requests
from pydantic import BaseModel, json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import requests
import json
import random

from dependencies import get_db, get_idea_service
from models import User, Idea
from schemas.inputs import IdeaCreate
from schemas.response import UserResponse, IdeaResponse
from services import idea
from services.idea import IdeaService

app = FastAPI()


# эндпоинт для отображения всех пользователей
@app.get('/user/',response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


#  # эндпоинт для отображения всех пользователей с пагинацией
# @app.get("/users/", response_model=List[UserResponse])
# def get_groups(offset: int = 0, limit: int = 5, db: Session = Depends(get_db)):
#     return db.query(User).offset(offset).limit(limit).all()


# эндпоинт для отображения идей пользователя
@app.get("/user/{user_id}/ideas",response_model=List[IdeaResponse])
def get_user_ideas(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    ideas = db.query(Idea).filter_by(user_id=user_id).all()
    return ideas



# эндпоинт для создания идеи
@app.post("/idea/", response_model=IdeaResponse)
def create_idea(idea: IdeaCreate, idea_service: IdeaService = Depends(get_idea_service)):
     return idea_service.create_idea(idea)



# @app.post("/idea/")
# def create_idea():
#     # Запрос к API для получения случайной активности
#     response = requests.get("https://www.boredapi.com/api/activity")
#     if response.status_code == 200:
#         activity = response.json()["activity"]
#         new_idea = Idea(activity=activity)
#         return new_idea
#     else:
#         return {"error": "Не удалось получить активность"}
#

# @app.post("/idea/",response_model=IdeaResponse)
# def create_idea(idea: IdeaCreate, db: Session = Depends(get_db)):
#     response = requests.get("https://www.boredapi.com/api/activity")
#     data = json.loads(response.text)
#     return Idea(activity=data["activity"])

if __name__ == '__main__':
    uvicorn.run(app, host= "localhost", port=8001)
