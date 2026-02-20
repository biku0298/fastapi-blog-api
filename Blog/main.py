
from . import model
from fastapi import FastAPI
from .database import engine
from .routers import blog,user,authentication
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>FastAPI Blog API</h1>
    <p>API is running successfully 🚀</p>
    <a href="/docs">Go to API Docs</a>
    """

model.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)














