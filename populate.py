from typing import List
from sqlmodel import Session, delete, select
from models.models import Category, Tag, Author ,Book
from db.db import engine,session



CATEGORY: List[str] = [
    "Fiction",
    "Novel",
    "Narratice",
    "Science fiction",
    "Mystery",
    "Horror",
    "Thriller",
    "Memoir",
    "History",
    "Poetry" 
]

TAGS: List[str] = [
    "tag1",
    "tag2"
    "tag3",
    "tag4",
    "tag5",
    "tag6"
    "tag7",
    "tag8",
    "tag9",
    "tag10"
]

AUTHOR_BOOK: dict = {
    "Leo Tolstoy": "War and Peas",
    "Gustave Flaubert": "Madame Bovary",
    "Mark Twain": "The Andventures of Finn",
    "George Eliot": "Middlemarch",
    "Charles Dickens": "Greate Expectations",
    "Anton Chekhov": "Mother",
    "William Faulkner": "The Sound",
    "James Joyce":"The greate",
    "Jane Austen": "Emma",
    "Vladimir Nabokov": "Pale Fire",
}

def create_category(j):
    category_v = Category(name=CATEGORY[j])
    return category_v

def create_tag(j):
    tag_v = Tag(name=TAGS[j])
    return tag_v

def create_author(j):
    author_n = Author(name=j)
    return author_n

def create_book(name_v, category_v, author_v):
    book = Book(name = name_v, category_id = category_v, author_id = author_v)
    return book


def create_db():
    categories = [create_category(x) for x in range(0,10)]
    authors = [create_author(k) for k in AUTHOR_BOOK.keys()]
    print("====> ",categories)
    with Session(engine) as session:
        session.add_all(categories + authors)
        session.commit()
        book = [create_book(AUTHOR_BOOK[authors[x].name],categories[x].id,authors[x].id) for x in range(0,10)]
        session.add_all(book)
        session.commit()
    


#create_db()
