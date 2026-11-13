from .. import model, schemas, utils, oauth2
from sqlalchemy.orm import Session
from fastapi import Response,status,HTTPException,Depends,FastAPI, APIRouter
from typing import List
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    posts = db.query(model.Post).all()
    return posts



@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title, post.content,post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    new_post=model.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int,response: Response,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id= %s""",(str(id),))
    # post=cursor.fetchone()
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    return post


@router.delete("/{id}")
def delete_post(id: int,response: Response,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post: schemas.PostCreate,db: Session = Depends(get_db)):

    # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(model.Post).filter(model.Post.id==id)
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()
