from fastapi import FastAPI
from faststream import FastStream
from app.routers import users, photos

app = FastAPI()
stream = FastStream()

