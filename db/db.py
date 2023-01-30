import os, sys
from sqlmodel import create_engine
from sqlmodel import Session
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Custom
load_dotenv(os.path.join(BASE_DIR, ".env"))  # Custom
engine = create_engine(
    os.getenv("DATABASE_URL"), echo=True
)  # echo=Tru will show all sql queries
session = Session(bind=engine)
