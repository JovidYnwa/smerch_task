import random
from typing import List
from sqlmodel import Session, delete, select
from models.models import Category, Tag, Author, Book
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
    "tag2",
    "tag3",
    "tag4",
    "tag5",
    "tag6",
    "tag7",
    "tag8",
    "tag9",
    "tag10"
]

AUTHOR: List[str] = [
    "Leo Tolstoy",
    "Gustave Flaubert",
    "Mark Twain",
    "George Eliot", 
    "Charles Dickens",
    "Anton Chekhov",
    "William Faulkner", 
    "James Joyce",
    "Jane Austen", 
    "Vladimir Nabokov", 
]

BOOK: List[str] = [
        "War and Peas",
        "Madame Bovary",
        "The Andventures of Finn",
        "Middlemarch",
        "Greate Expectations",
        "Mother",
        "The Sound",
        "The greate",
        "Emma",
        "Pale Fire",
    ]

def create_instance(m, v):
    instance_v = m(name=v)
    return instance_v

def create_tag_instance(v, book_v):
    inctance_ = Tag(v, books=book_v)


def create_book(name_v,author_v, category_v, tag_v: List[int]):
    book = Book(
        name = name_v, 
        author_id = author_v, 
        category_id = category_v,
        tags=tag_v
    )
    return book


def create_db():
    categories = [create_instance(Category, k) for k in CATEGORY]
    authors = [create_instance(Author, k) for k in AUTHOR]
    tags = [create_instance(Tag, k) for k in TAGS]
    books = [
        create_book(BOOK[x],
                    authors[x].id,
                    categories[x].id,
                    tag_v=tags[random.randint(1,10)-1:random.randint(1,10)]
                    )
            for x in range(0,10)
            
    ]

    print(len(categories))
    print(len(authors))
    print(len(tags))
    print(books)
    print()



    with Session(engine) as session:
        session.add_all(categories + authors + tags + books)
        session.commit()

    


#create_db()
