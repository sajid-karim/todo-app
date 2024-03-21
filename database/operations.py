from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.todo import TodoItem
from database.engine import DBengine
from models.user import User

db = DBengine.session()()


def get_todo(db: Session, todo_id: int):
    todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if todo_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo_item


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TodoItem).offset(skip).limit(limit).all()


def create_todo(db: Session, todo):
    db_todo = TodoItem(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, todo):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        for key, value in todo.dict().items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo


def find_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def find_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
