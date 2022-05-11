from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user_cources = relationship('UserCources', back_populates='user')


class UserCources(Base):
    __tablename__ = 'user_cources'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    cource_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    cource_filds = Column(JSON, nullable=False)
    cource_info = Column(JSON, nullable=True)

    user = relationship('User', back_populates='user_cources')