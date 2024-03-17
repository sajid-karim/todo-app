from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from database.engine import DBengine
import models
from routes import crud, login, token, user
import sys

sys.path.append("..")

app = FastAPI()

models.user.metadata.create_all(bind=DBengine.get_engine())

app.include_router(crud.router)
app.include_router(login.router)
app.include_router(token.router)
app.include_router(user.router)





  
