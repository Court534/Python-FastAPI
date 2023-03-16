# Import necessary modules and classes
from fastapi import FastAPI
from typing import List 
from models import User, Gender, Role
from uuid import uuid4

# Create a FastAPI instance
app = FastAPI()

# Define a list of User objects with pre-defined attributes
db: List[User] = [
    User(id=UUID("8bafbadf-7564-44c6-a93d-6f44a70b3c26"), 
         first_name= "John",
         last_name= "Doe",
         gender= Gender.male,
         roles=[Role.student]
        ),
    User(id=UUID("6708f9ad-064a-4c7d-8ad1-4986bfddb338"), 
         first_name= "Jannet",
         last_name= "Doe",
         gender= Gender.female,
         roles=[Role.admin, Role.user]
        )
]

# Define a GET endpoint at root URL path that returns "Hello World"
@app.get("/")
async def root ():
    return {"Hello": "World"}

# Define a GET endpoint at "/users" path that returns the db list of User objects
@app.get("/users")
async def fetch_users():
    return db

# Define a POST endpoint at "/users" path that adds a new User object to db list
@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
