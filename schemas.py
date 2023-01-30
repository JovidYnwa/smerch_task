from pydantic import BaseModel


class BookItem(BaseModel):
    book_name: str
    category_id: int = 1
    author_name: str
    tag_id: int = 1
