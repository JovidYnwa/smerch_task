from typing import Optional

from fastapi import APIRouter

from service import get_user_books

userbooks_router = APIRouter()


@userbooks_router.get("/user-books", tags=["UserBooks"])
def categories(user_id: Optional[int] = None):
    """UserBooks of all categories"""

    book = get_user_books(user_id_v=user_id)
    return {"user_books": book}
