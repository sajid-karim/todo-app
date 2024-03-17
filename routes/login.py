from fastapi import APIRouter
from auth.jwt import create_access_token
router = APIRouter()

@router.post("/login")
def login(username: str):
  # Check if username and password are valid
  access_token = create_access_token(data={"sub": username})    
  return {"message": "Login successful", "token": access_token}
