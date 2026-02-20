from fastapi import APIRouter
from .. import database, schemas, model
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status ,HTTPException
from ..hashing import Hash
from ..repository import user


router = APIRouter(
    prefix="/users",
tags=["Users"]
)
get_db = database.get_db

@router.post("/",response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)


@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)
