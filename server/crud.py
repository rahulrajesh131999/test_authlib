from sqlmodel import Session, select
from fastapi import HTTPException, status
from pydantic import EmailStr

from model import User, UserPass
from core.security import get_password_hash, verify_password_hash
from core.config import settings
from core.db import SessionDep


async def create_new_user(session:SessionDep, email:EmailStr, name:str, google_id:str | None = None, password:str | None = None, confirm_password:str | None = None):
    
    if google_id:
        new_user = User(
            full_name=name,
            email=email,
            google_login_id=google_id
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user
    
    else:
        name = name
        email = email

        if password != confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="password does not match confirm password"
            )
        
        result = session.exec(select(User).where(User.email == email))
        user_exists = result.first()

        if user_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )
        
        hashed_password = get_password_hash(plain_password=password)

        new_user = User(
            full_name=name,
            email=email,
            hashed_password = hashed_password
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user
    


async def authenticate(session:SessionDep, email:EmailStr, password:str):
    if not email or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="email and password required"
        )
    
    result = session.exec(select(User).where(User.email == email))

    user = result.first()

    if not user:
        verify_password_hash(plain_password=password, hash_password=settings.DUMMY_HASH)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    
    if not verify_password_hash(plain_password=password, hash_password=user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    
    return user
    
