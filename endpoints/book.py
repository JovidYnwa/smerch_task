from typing import Optional

from fastapi import APIRouter
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from fastapi.encoders import jsonable_encoder
from db.db import session
from models.models import Book, Author
from schemas import BookItem
from service import cerate_new_book, get_book_info

book_router = APIRouter()


@book_router.get('/book', tags=['Book'])
def books(book_name: Optional[str]=None, category_name: Optional[str]=None, tag_name: Optional[str]=None):
    """List of all books
    """

    books = get_book_info(book_name_v=book_name, category_name_v=category_name, tag_name_v=tag_name)
    return {'books': books}


@book_router.get('/book/{id}', tags=['Book'])
def book(id: int):
    """Book by given id
    """

    book = get_book_info(book_id_v=id)
    if not book:
        return JSONResponse("Book does not exist",status_code=HTTP_404_NOT_FOUND)
    return {'book': book}

#оздание книги с её автором одной транзакцией.

@book_router.post('/book', tags=['Book'])
def create_book(item: BookItem):
    """Tag create
    """
    book_exist = select(Book).where(Book.name==item.book_name)
    book_exist = session.exec(book_exist).all()

    if len(book_exist) > 0:
        return JSONResponse('object already exsits',status_code=HTTP_409_CONFLICT)

    try:
        cerate_new_book(item)
    except:
        return JSONResponse('Object creation failed',status_code=HTTP_409_CONFLICT)

    return "Object successfully created"


@book_router.put('/book/{id}', response_model=Author, tags=['Book'])
def update_book(id: int, book: Book):
    """Book update
    """
    book_found = session.get(Book, id)

    if book_found is None:
        return JSONResponse('object not found',status_code=HTTP_401_UNAUTHORIZED)

    update_item_encoded = jsonable_encoder(book)
    update_item_encoded.pop('id', None)
    for key, val in update_item_encoded.items():
        book_found.__setattr__(key, val)
    session.commit()
    return book_found


@book_router.delete('/book/{id}', status_code=HTTP_204_NO_CONTENT, tags=['Book'])
def delete_book(id: int):
    """Book delete by id
    """

    book_found = session.get(Book, id)
    if book_found is None:
        return JSONResponse("Object not found",status_code=HTTP_401_UNAUTHORIZED)
    session.delete(book_found)
    session.commit()