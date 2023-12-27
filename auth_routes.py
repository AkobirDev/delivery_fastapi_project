from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get("/")
async def auth():
    return {"message": "Authentication successful"}
