# Import necessary modules and classes
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# Define an enumeration of gender values
class Gender(str, Enum):
    male = "male"
    female = "female"
    
# Define an enumeration of role values
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
  
# Define a User data model that inherits from the BaseModel class
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str 
    middle_name: Optional[str] = None 
    gender: Gender 
    roles: List[Role] 
