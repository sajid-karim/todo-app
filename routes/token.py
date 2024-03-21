from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from models.todo import TodoItem
from auth.jwt import get_current_user, create_access_token, verify_password, get_password_hash
import database.operations as db
from models.token import Token
from pydantic import BaseModel


router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True

# Define route for all token operations


@router.post("/token", response_model=Token)
# Define function to create a new token
async def create_token(username: str, password: str):
    # Check if username and password are valid
    user = db.find_user(username=username)
    if not user:
        return {"message": "Invalid username or password"}
    if not verify_password(password, user.password):
        return {"message": "Invalid username or password"}
    # If username and password are valid, create a new token
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
