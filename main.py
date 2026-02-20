from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
def index(limit=10,published: bool =True, sort : Optional[str]= None):
    if published:
        return { "data": f"{limit} items published" }
    else:
        return { "data": f"{limit} items unpublished" }
