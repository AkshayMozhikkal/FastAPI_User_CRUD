from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from routers import auth_routes
import os



app = FastAPI()

class Data(BaseModel):
    name : str

app.include_router(auth_routes.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}

