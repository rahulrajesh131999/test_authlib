from pydantic import BaseModel, EmailStr
from datetime import datetime, timezone, timedelta
from sqlalchemy import DateTime
from sqlmodel import SQLModel, Field
import uuid



def get_date_utc()->datetime :
    return datetime.now(timezone.utc)

class UserBase(SQLModel):
    full_name : str = Field(min_length=3)
    email : EmailStr = Field(unique=True)
    
class UserPass(UserBase):
    password : str | None = Field(default=None,min_length=8, max_length=24)
    confirm_password : str | None = Field(default=None,min_length=8, max_length=24)
   

class User(UserBase, table=True):
    id : uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password : str | None = None
    google_login_id : str | None = None
    created_at : datetime | None = Field(
        default_factory=get_date_utc,
        sa_type= DateTime(timezone=True)  # tells SQLAlchemy what database column type to create.
    )

class UserRead(UserBase):
    id : uuid.UUID
    google_login_id : str | None = None
    created_at : datetime

class UserLogin(BaseModel):
    email : EmailStr
    password : str