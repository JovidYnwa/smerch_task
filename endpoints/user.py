from typing import Optional

from fastapi import APIRouter
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from fastapi.encoders import jsonable_encoder
from db.db import session
from models.models import User

user_router = APIRouter()


@user_router.get('/user/{id}', response_model=User, tags=['User'])
def user(id: int):
    """User by given id
    """

    category_found = session.get(User, id)
    if not category_found:
        return JSONResponse("User does not exist",status_code=HTTP_404_NOT_FOUND)
    return category_found


@user_router.post('/user', tags=['User'])
def create_user(user_pr: User):
    """User create
    """

    new_user= User(name=user_pr.name)
    session.add(new_user)
    session.commit()
    return new_user.name
