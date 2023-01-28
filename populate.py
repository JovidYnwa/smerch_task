import random
from typing import List
from sqlmodel import Session, delete, select
from models.models import Category, Tag, Author, Book, User, UserBook
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

BOOKS: List[str] = [
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

USERS: List[str] = [
    "User1",
    "User2",
    "User3",
    "User4",
    "User5",
    "User6",
    "User7",
    "User8",
    "User9",
    "User10",
]


def create_instance(m, v):
    instance_v = m(name=v)
    return instance_v


def create_book(name_v,author_v, category_v, tag_v: List[Tag]):
    book = Book(
        name = name_v, 
        author_id = author_v, 
        category_id = category_v,
        tags=tag_v
    )
    return book

def create_user_book(user_v, book_v):
    book = UserBook(
        user_id=user_v,
        book_id=book_v,
    )
    return book

def create_db():
    categories = [create_instance(Category, k) for k in CATEGORY]
    authors = [create_instance(Author, k) for k in AUTHOR]
    tags = [create_instance(Tag, k) for k in TAGS]
    users = [create_instance(User, k) for k in USERS]

    with Session(engine) as session:
        session.add_all(categories + authors + tags + users)
        session.commit()
        books = [
            create_book(BOOKS[x],
                        authors[x].id,
                        categories[x].id,
                        tag_v=tags[random.randint(1,10)-1:random.randint(1,10)]
                        )
                for x in range(0,10)
                
        ]
        session.add_all(books)
        session.commit()
        users_books = [create_user_book(k.id, books[random.randint(1,9)].id) for k in users]
        session.add_all(users_books)
        session.commit()

 
create_db()
