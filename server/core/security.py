from datetime import datetime, timezone, timedelta
from pwdlib import PasswordHash
import jwt

from core.config import SettingsDep

password_hash = PasswordHash.recommended()


def create_access_token(*,data:str, expires_at:datetime | None = None, settings:SettingsDep):

    if expires_at:
        expire = datetime.now(timezone.utc) + expires_at
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode = {"exp":expire, "sub":str(data)}

    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM,)

    return encoded_jwt

def decode_token(*,access_token, settings:SettingsDep):
    return jwt.decode(access_token, settings.JWT_SECRET, settings.JWT_ALGORITHM)

def get_password_hash(plain_password:str):
    return password_hash.hash(plain_password)

def verify_password_hash(plain_password:str, hash_password:str):
    return password_hash.verify(hash_password=hash, password=plain_password)