from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.testing import db

Base = declarative_base()


class Idea(Base):
    __tablename__ = 'idea'

    id = Column(Integer, primary_key=True)
    idea = Column(String(100), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey('user.id'))    #связь один ко многим

    def __repr__(self):
        return f"<User {self.idea}>"


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    ideas = relationship('Idea', backref='user', lazy=True)


    def __repr__(self):
        return f"<User {self.username}>"