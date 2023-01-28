from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# таблица `category`:
#   - **id** int
#   - **name** str

# таблица `tag`:
#   - **id** int
#   - **name** str

# таблица `book`:
#   - **id** int
#   - **name** str
#   - **category_id** категория книги
#   - **author_id** автор
#   - **tags** список тегов (many to many)


class Category(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str


class Author(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str


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

    books: List["Book"] = Relationship(back_populates="tags", link_model=BookTagLink)

class Book(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id") #makeing a foregin key
    #category: Optional[Category] = Relationship(back_populates='book')
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    #author: Optional[Author] = Relationship(back_populates='book')

    tags: List["Tag"] = Relationship(back_populates='books', link_model=BookTagLink)






