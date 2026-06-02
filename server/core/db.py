from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from typing import Annotated

from core.config import SettingsDep


engine = create_engine(SettingsDep.DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]