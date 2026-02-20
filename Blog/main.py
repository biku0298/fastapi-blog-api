
from . import model
from fastapi import FastAPI
from .database import engine
from .routers import blog,user,authentication

app = FastAPI()



model.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)














