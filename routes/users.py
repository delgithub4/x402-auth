from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def users():

    return {
        "message": "List of users"
    }


@router.get("/{user_id}")
def user(user_id: int):

    return {
        "user": user_id
    }
