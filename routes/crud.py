from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.todo import TodoItem
from database.engine import DBengine
import database.operations as crud
from pydantic import BaseModel


router = APIRouter()
# Dependency


def get_db():
    db = DBengine.SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True


@router.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    item = crud.get_todo(db, todo_id)
    return item


@router.get("/todos", response_model=list[TodoItem])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_todos(db, skip, limit)


@router.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


@router.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, todo, db: Session = Depends(get_db)):
    return crud.update_todo(db, todo_id, todo)


@router.delete("/todos/{todo_id}", response_model=TodoItem)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db, todo_id)
