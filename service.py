from sqlmodel import select
from models.models import Book, Category, Author, Tag, BookTagLink, User, UserBook
from db.db import session, engine
from typing import Optional

from schemas import BookItem


def get_book_info(
    book_id_v: Optional[int] = None,
    book_name_v: Optional[str] = None,
    category_name_v: Optional[str] = None,
    tag_name_v: Optional[str] = None,
):
    """ """

    books = (
        select(Book.id, Book.name, Category, Author)
        .join(Category, Category.id == Book.category_id)
        .join(Author, Author.id == Book.author_id)
        .join(BookTagLink, isouter=True)
        .join(Tag, isouter=True)
    )

    if book_name_v is not None:
        books = books.where(Book.name == book_name_v)
    elif category_name_v is not None:
        books = books.where(Category.name == category_name_v)
    elif tag_name_v is not None:
        books = books.where(Tag.name == tag_name_v)
    elif book_id_v is not None:
        books = books.where(Book.id == book_id_v)

    books = session.exec(books).all()
    return books


def update_book_info(book_id_v: Optional[int] = None, tag_id_v: Optional[id] = None):
    """ """

    books = (
        select(Book.id, Book.name, Category, Author, Tag)
        .join(Category, Category.id == Book.category_id)
        .join(Author, Author.id == Book.author_id)
        .join(BookTagLink, BookTagLink.book_id == Book.id)
        .join(Tag, BookTagLink.tag_id == Tag.id)
    )

    if tag_id_v is not None:
        books = books.where(Tag.id == tag_id_v)
    elif book_id_v is not None:
        books = books.where(Book.id == book_id_v)

    books = session.exec(books).all()
    return books


def cerate_new_book(instance: BookItem):
    """Method for creating new Book and Author if needed"""

    book_name = instance.book_name
    author_name = instance.author_name
    # Atomic transaction
    with session:
        author_exist = select(Author.id).where(Author.name == author_name)
        author_exist = session.exec(author_exist).all()

        if len(author_exist) == 0:
            new_author = Author(name=author_name)
            session.add(new_author)

        author_id = select(Author.id).where(Author.name == author_name)
        author_id_v = session.exec(author_id).all()[0]
        new_book = Book(
            name=book_name, category_id=instance.category_id, author_id=author_id_v
        )
        session.add(new_book)
        session.commit()
    return new_book


def get_user_books(user_id_v: Optional[int] = None):
    """Method for getting all usersbooks"""

    user_books = (
        select(UserBook.id, User, Book)
        .join(User, UserBook.user_id == User.id)
        .join(Book, UserBook.book_id == Book.id)
    )

    if user_id_v is not None:
        user_books = user_books.where(UserBook.user_id == user_id_v)
    else:
        user_books = user_books

    user_books = session.exec(user_books).all()
    return user_books
