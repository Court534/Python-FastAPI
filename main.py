from fastapi import FastAPI
from typing import List 
from models import User, Gender
from uuid import uuid4

app = FastAPI()

db: List [User] = [
    User(id-uuid4(), 
         first_name="John",
         last_name="Doe",
         gender="Gender.male",
        )
]

@app.get("/")
async def root ():
    return {"Hello": "World"}
