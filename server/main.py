from fastapi import FastAPI
from fastapi.responses import Response
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from core.db import create_db_and_tables
from authlib_setup import authlib
from routes import credential_auth


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("connected to db...")
    create_db_and_tables()
    yield
    print("shutting down")


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="some-random-string",
)

routers = [
    authlib.router,
    credential_auth.router
]

for router in routers:
    app.include_router(router, prefix="/api/v1")

@app.head("/")
def root_head():
    return Response(status_code=200)


@app.get("/")
def home():
    return {"message":"this is home page"}