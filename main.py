from fastapi import FastAPI
import uvicorn
from endpoints.category import category_router
from endpoints.author import author_router
from endpoints.tag import tag_router
from endpoints.book import book_router




app = FastAPI()

app.include_router(category_router)
app.include_router(author_router)
app.include_router(tag_router)
app.include_router(book_router)



if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
