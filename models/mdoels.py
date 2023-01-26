from typing import Optional
from sqlalchemy import Table, MetaData, Column,Integer, String, ForeignKey

metadata = MetaData()


category = Table(
    "category",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
) 

tag = Table(
    "tag",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),    
) 

book = Table(
    "book",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('category_id', Integer, ForeignKey("category.id")),
    Column('tag_id', Integer, ForeignKey("tag.id"))
    #User Should be adedde
)

