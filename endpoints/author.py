from typing import Optional

from fastapi import APIRouter
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)
from fastapi.encoders import jsonable_encoder
from db.db import session
from models.models import Author

author_router = APIRouter()


@author_router.get("/author", tags=["Author"])
def authors(author_name: Optional[str] = None):
    """List of all authors"""

    authors = select(Author)
    if author_name is not None:
        authors = authors.where(Author.name == author_name)
    else:
        authors = authors

    authors = session.exec(authors).all()
    return {"authors": authors}


@author_router.get("/author/{id}", response_model=Author, tags=["Author"])
def author(id: int):
    """Author by given id"""
    author_found = session.get(Author, id)
    if not author_found:
        return JSONResponse("Author does not exist", status_code=HTTP_404_NOT_FOUND)
    return author_found


@author_router.post("/author", tags=["Author"])
def create_author(author_pr: Author):
    """Author create"""

    new_author = Author(name=author_pr.name)
    session.add(new_author)
    session.commit()
    return {"name": new_author.name}


@author_router.put("/author/{id}", response_model=Author, tags=["Author"])
def update_author(id: int, author: Author):
    """Author update"""
    author_found = session.get(Author, id)

    if author_found is None:
        return JSONResponse("Object not found", status_code=HTTP_404_NOT_FOUND)

    update_item_encoded = jsonable_encoder(author)
    update_item_encoded.pop("id", None)
    for key, val in update_item_encoded.items():
        author_found.__setattr__(key, val)
    session.commit()
    return author_found


@author_router.delete("/author/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Author"])
def delete_author(id: int):
    """Author delete by id"""
    author_found = session.get(Author, id)
    if author_found is None:
        return JSONResponse("Object not found", status_code=HTTP_404_NOT_FOUND)
    session.delete(author_found)
    session.commit()
