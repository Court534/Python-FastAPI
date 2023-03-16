# Import necessary modules and classes
from fastapi import FastAPI, HTTPException
from typing import List 
from models import User, Gender, Role, UserUpdateDetails
from uuid import UUID 

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

# Define a DELETE endpoint at /users/{user_id}
@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    # Loop through each user in the database
    for user in db:
        # Check if the user's ID matches the given user_id
        if user.id == user_id:
            # If there's a match, remove the user from the database
            db.remove(user)
            # Return a success message
            return {"message": "User deleted successfully"}
    # If no user is found with the given user_id, raise an HTTPException
    raise HTTPException(status_code=404, detail=f"User ID:'{user_id}' not found")
    

# Define a PUT endpoint at /users/{user_id}
@app.put("/users/{user_id}")
async def update_user(user_update: UserUpdateDetails, user_id: UUID):
    # Loop through each user in the database
    for user in db:
        # Check if the user's ID matches the given user_id
        if user.id == user_id:
            # If there's a match, update the user's information based on the provided UserUpdateDetails
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            # Return a success message
            return {"message": "User updated successfully"}
    # If no user is found with the given user_id, raise an HTTPException
    raise HTTPException(status_code=404, detail=f"User ID:'{user_id}' not found")
