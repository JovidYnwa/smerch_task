from fastapi import FastAPI
import uvicorn
from endpoints.category import category_router


app = FastAPI()

app.include_router(category_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
