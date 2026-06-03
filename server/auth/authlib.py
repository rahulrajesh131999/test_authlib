from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.requests import Request
from fastapi import APIRouter, HTTPException, status
from core.config import get_settings

router = APIRouter()
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
async def auth_via_google(request:Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="error in auth token"
        )
    user = token.get("userinfo")

    if user:
        request.session["user"] = dict(user)

    return {"message": "user logged in successfully"}