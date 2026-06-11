from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.requests import Request
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
from sqlmodel import select

from core.config import get_settings
from core.db import SessionDep
from model import User, UserRead
from crud import create_new_user
from core.security import create_access_token

router = APIRouter(prefix="/auth")
settings = get_settings()

oauth = OAuth()

oauth.register(
    name="google",
    client_id= settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    server_metadata_url = settings.SERVER_METADATA_URL,
    client_kwargs = {
        "scope" : "openid email profile"
    }
)

@router.get("/login/google")
async def login(request:Request):
    redirect_uri = request.url_for("auth_via_google")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/login/auth")
async def auth_via_google(request:Request, session:SessionDep):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="error in auth token"
        )
    user = token.get("userinfo")

    if user:

        request.session["user"] = dict(user) # use this only to store session for auth

        user_exists = session.exec(select(User).where(User.email == user.email)).first()

        if not user_exists:
            new_user = await create_new_user(session= session, email = user.email, google_id=user.sub, name=user.name)

            if not new_user:
                raise HTTPException(
                    status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="failed to create new user via google authentication"
                )
            access_token = create_access_token(data=new_user.id, expires_at=28)

            db_object = UserRead.model_validate(new_user)

            response = RedirectResponse(
                url="http://localhost:3000/dashboard",
                status_code=302
            )

            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly= True,
                #secure= True,
                samesite="lax",
                path="/",
                max_age= 60 * 60 * 24 * 28
            )

            # print("printing response headers",response.headers)
            return response
        else:
            access_token = create_access_token(data=user_exists.id, expires_at=28)

            db_object = UserRead.model_validate(user_exists)

            response = RedirectResponse(
                url="http://localhost:3000/dashboard",
                status_code=302
            )
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly= True,
                #secure= True,
                samesite="lax",
                path="/",
                max_age= 60 * 60 * 24 * 28
            )

            # print("printing response headers",response.headers)
            return response