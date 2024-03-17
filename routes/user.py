from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database.engine import DBengine
import database.operations as crud 

def get_db():
  db = DBengine.SessionLocal()
  try:
    yield db
  finally:
    db.close()

router = APIRouter()

class User(BaseModel):
  id: int
  username: str
  email: str
  password: str

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db=Depends(get_db)):
  return crud.find_user(db, user_id)


  