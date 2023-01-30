from sqlmodel import create_engine
from sqlmodel import Session
eng = 'database.db'
#uuu = 'postgresql+psycopg2://postgres:password@db:5432/book_db'
#sqlite_url = f'sqlite:///{eng}'
uuu = 'postgresql+psycopg2://postgres:password@db:5432/book_db'
sqlite_url = uuu
engine = create_engine(sqlite_url, echo=True)
session = Session(bind=engine)