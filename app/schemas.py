from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int
    faculty: str
    bio: str
    dormitory_info: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True