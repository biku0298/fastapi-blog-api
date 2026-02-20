from sqlalchemy.orm import Session
from .. import model, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs

def create(request:schemas.Blog,db: Session):
    new_blog = model.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} Not Found")
    return blog

def destroy(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} Not Found")
    blog.delete(synchronize_session=False)
    db.commit()
    return("Blog deleted")

def update(id,request:schemas.Blog,db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} Not Found")
    blog.update(request)
    db.commit()
    return("Blog updated")