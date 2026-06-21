from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, PlainTextResponse, Response
from fastapi.requests import Request

from model import UserPass, User, UserRead, UserLogin
from crud import create_new_user, authenticate
from core.security import create_access_token
from core.depends import Current_User
from core.db import SessionDep

router = APIRouter(prefix="/auth", tags=["/auth"])


@router.post("/register")
async def register(user:UserPass, session:SessionDep):
    try:
        created_user = await create_new_user(session=session,
                                             name=user.full_name,
                                             email=user.email,
                                             password=user.password, 
                                             confirm_password=user.confirm_password)

        if not created_user:
            raise HTTPException(
                status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Failed to create user"
            )
        
        db_object = UserRead.model_validate(created_user)

        access_token = create_access_token(data=db_object.id, expires_at=28)
        
        response = JSONResponse(
            content={"user":db_object.model_dump(mode="json")}
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            samesite="none",
            secure=True,
            max_age=60* 60 * 24 * 28
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/login")
async def login( user:UserLogin, session:SessionDep):

    email = user.email
    password = user.password

    if not email or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="both email and password required of login"
        )
    

    user = await authenticate(email=email, password=password, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="user authentication failed"
        )
    
    db_object = User.model_validate(user)

    access_token = create_access_token(data=db_object.id, expires_at=28)

    response = JSONResponse(
        content={"user" : db_object.model_dump(mode="json")}
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="none",
        expires= 60 * 60 * 24 * 28
    )

    return response


@router.get("/me")
async def current_user(current_user:Current_User):

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authorized"
        )

    user = UserRead.model_validate(current_user)

    return JSONResponse(
        content={"user":user.model_dump(mode="json")}
    )

@router.get("/logout")
def logout(response:Response, request:Request):

    request.session.clear()

    #request.session.pop("user",None)

    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=True,
        samesite="none",
    )

    return {"message":"logged out"}
