from fastapi import FastAPI
import uvicorn



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Merch"}


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
