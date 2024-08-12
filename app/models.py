from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    faculty = Column(String, nullable=False)
    bio = Column(Text)
    dormitory_info = Column(String)
    photos = relationship('UserPhoto', back_populates='user')

class UserPhoto(Base):
    __tablename__ = 'user_photos'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    photo_url = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship('User', back_populates='photos')