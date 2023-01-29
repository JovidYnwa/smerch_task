from typing import Optional
from db.db import engine
from models.models import Category
from sqlmodel import Session, select, or_


def select_all_categories(cat_name: Optional[str]=None):


    with Session(engine) as session:
        statement = select(Category)
        result = session.exec(statement)
    return result

