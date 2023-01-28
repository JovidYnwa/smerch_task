from typing import Optional

from fastapi import APIRouter
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from fastapi.encoders import jsonable_encoder
from db.db import session
from models.models import Category

category_router = APIRouter()


@category_router.get('/category', tags=['Category'])
def categories(cat_name: Optional[str]=None):
    """List of all categories
    """
    categories = select(Category)
    if cat_name is not None:
        categories = categories.where(Category.name==cat_name)
    else:
        categories = categories

    categories = session.exec(categories).all()
    return {'categories': categories}


@category_router.get('/category/{id}', response_model=Category, tags=['Category'])
def category(id: int):
    """Category by given id
    """
    category_found = session.get(Category, id)
    if not category_found:
        return JSONResponse("Category does not exist",status_code=HTTP_404_NOT_FOUND)
    return category_found


@category_router.post('/category', tags=['Category'])
def create_category(category_pr: Category):
    """Category create
    """

    new_category = Category(name=category_pr.name)
    session.add(new_category)
    session.commit()
    return new_category.name


@category_router.put('/category/{id}', response_model=Category, tags=['Category'])
def update_category(id: int, category: Category):
    """Category update
    """
    category_found = session.get(Category, id)

    if category_found is None:
        return JSONResponse('object not found',status_code=HTTP_401_UNAUTHORIZED)

    update_item_encoded = jsonable_encoder(category)
    update_item_encoded.pop('id', None)
    for key, val in update_item_encoded.items():
        category_found.__setattr__(key, val)
    session.commit()
    return category_found


@category_router.delete('/category/{id}', status_code=HTTP_204_NO_CONTENT, tags=['Category'])
def delete_category(id: int):
    """Category delete by id
    """
    category_found = session.get(Category, id)
    if category_found is None:
        return JSONResponse("Object not found",status_code=HTTP_401_UNAUTHORIZED)
    session.delete(category_found)
    session.commit()