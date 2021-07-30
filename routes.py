from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class UrlModel(BaseModel):
   url : str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/url")
def url(url  : UrlModel):
   return {"message" : "url", "original_url": url}
