from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware

from core.db import create_db_and_tables
from authlib import authlib


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("connected to db...")
    create_db_and_tables()
    yield
    print("shutting down")


app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware,secret_key = "some-random-string")

app.include_router(authlib.router)


@app.get("/")
def home():
    return {"message":"this is home page"}