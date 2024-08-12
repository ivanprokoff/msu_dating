from sqlalchemy.orm import Session
from app import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, age=user.age, faculty=user.faculty, bio=user.bio, dormitory_info=user.dormitory_info)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user