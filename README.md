# FastAPI User Management System
This project is a simple user management system built using the FastAPI framework. It allows users to be created, updated, deleted, and retrieved from a list stored in memory.

## Installation
To get started with this project, you should first clone the repository to your local machine using the following command:

`git clone https://github.com/your-username/fastapi-user-management.git`

Once you have cloned the repository, you can install the required dependencies by running:
`pip install -r requirements.txt`

### Usage
To start the FastAPI server, simply run the following command:

bash
`uvicorn main:app --reload`

This will start the server on http://localhost:8000.

### API Endpoints

The following API endpoints are available:

GET /: Returns a simple "Hello, World!" message.

GET /users: Returns a list of all users in the database.

POST /users: Adds a new user to the database.

DELETE /users/{user_id}: Deletes a user from the database based on their ID.

PUT /users/{user_id}: Updates a user's information in the database based on their ID.

Resources
[FastAPI documentation](https://fastapi.tiangolo.com/)
[Pydantic documentation](https://pydantic-docs.helpmanual.io/)
[Uvicorn documentation](https://www.uvicorn.org/)