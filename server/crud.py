from sqlmodel import Session, select
from fastapi import HTTPException, status
from pydantic import EmailStr

from model import User, UserPass
from core.security import get_password_hash, verify_password_hash
from core.config import SettingsDep


async def create_new_user(session:Session, google_id:str | None, password:str, confirm_password:str, email:EmailStr, name:str):
    
    if google_id:
        new_user = await User(
            full_name=name,
            email=email,
            google_login_id=google_id
        )

        await session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
    
    else:
        name = name
        email = name

        if password != confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="password does not match confirm password"
            )
        
        user_exists = await session.exec(select(User).where(User.email == email))

        if user_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )
        
        hashed_password = await get_password_hash(plain_password=password)

        new_user = await User(
            full_name=name,
            email=email,
            hashed_password = hashed_password
        )

        await session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
    


async def authenticate(session:Session, user:UserPass, settings:SettingsDep):

    email = user.email
    password = user.password

    if not email or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="email and password required"
        )
    
    user = await session.exec(select(User).where(User.email == email))

    if not user:
        verify_password_hash(plain_password=password, hash_password=settings.DUMMY_HASH)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    
    if not verify_password_hash(plain_password=password, hash_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    
    return user
    
