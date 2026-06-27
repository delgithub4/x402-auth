from fastapi import APIRouter

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.get("/")
def roles():

    return {
        "roles": [
            "Admin",
            "User",
            "Moderator"
        ]
    }
