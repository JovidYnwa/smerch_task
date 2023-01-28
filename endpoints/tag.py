from typing import Optional

from fastapi import APIRouter
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from fastapi.encoders import jsonable_encoder
from db.db import session
from models.models import Tag

tag_router = APIRouter()


@tag_router.get('/tag', tags=['Tag'])
def tags(tag_name: Optional[str]=None):
    """List of all tags
    """

    tags = select(Tag)
    if tag_name is not None:
        tags = tags.where(Tag.name==tag_name)
    else:
        tags = tags

    tags = session.exec(tags).all()
    return {'tags': tags}


@tag_router.get('/tag/{id}', response_model=Tag, tags=['Tag'])
def tag(id: int):
    """Tag by given id
    """
    tag_found = session.get(Tag, id)
    if not tag_found:
        return JSONResponse("Author does not exist",status_code=HTTP_404_NOT_FOUND)
    return tag_found


@tag_router.post('/tag', tags=['Tag'])
def create_tag(category_pr: Tag):
    """Tag create
    """

    new_author = Tag(name=category_pr.name)
    session.add(new_author)
    session.commit()
    return {"name": new_author.name}


@tag_router.put('/tag/{id}', response_model=Tag, tags=['Tag'])
def update_tag(id: int, category: Tag):
    """Author update
    """
    tag_found = session.get(Tag, id)

    if tag_found is None:
        return JSONResponse('object not found',status_code=HTTP_401_UNAUTHORIZED)

    update_item_encoded = jsonable_encoder(category)
    update_item_encoded.pop('id', None)
    for key, val in update_item_encoded.items():
        tag_found.__setattr__(key, val)
    session.commit()
    return tag_found


@tag_router.delete('/tag/{id}', status_code=HTTP_204_NO_CONTENT, tags=['Tag'])
def delete_tag(id: int):
    """Author delete by id
    """

    tag_found = session.get(Tag, id)
    if tag_found is None:
        return JSONResponse("Object not found",status_code=HTTP_401_UNAUTHORIZED)
    session.delete(tag_found)
    session.commit()