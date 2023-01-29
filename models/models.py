from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str

    book: Optional["Book"] = Relationship(back_populates='categories')


class Author(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str

    books: Optional["Book"] = Relationship(back_populates='author')


class BookTagLink(SQLModel, table=True):
    """Many-To-Many model for Book, Tag models
    """
    book_id: Optional[int] = Field(
        default=None, foreign_key='book.id', primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key='tag.id', primary_key=True
    )


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str

    books: List["Book"] = Relationship(back_populates="tags", link_model=BookTagLink) #Many to many


class Book(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id") #makeing a foregin key
    categories: Optional["Category"] = Relationship(back_populates='book')
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    author: Optional["Author"] = Relationship(back_populates='books')

    book: Optional["UserBook"] = Relationship(back_populates="userbooks")
    tags: List["Tag"] = Relationship(back_populates='books', link_model=BookTagLink) #many to many


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str

    userbooks: Optional["UserBook"] = Relationship(back_populates='user')


class UserBook(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates='userbooks')
    
    book_id: Optional[int] = Field(default=None, foreign_key="book.id")
    userbooks: Optional["Book"] = Relationship(back_populates='book')