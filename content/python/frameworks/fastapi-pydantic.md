# FastAPI Pydantic

- Install required packages:
  ```bash
  pip install fastapi uvicorn
  ```

## User Model

- Define Pydantic model in `models.py`:
  ```python
  from pydantic import BaseModel, EmailStr

  class User(BaseModel):
      id: int
      name: str
      email: EmailStr
      is_active: bool = True
  ```

## API Endpoints

- Create FastAPI app in `main.py`:
  ```python
  from fastapi import FastAPI
  from models import User

  app = FastAPI()
  users_db = []

  @app.post("/users/", response_model=User)
  def create_user(user: User):
      users_db.append(user)
      return user

  @app.get("/users/", response_model=list[User])
  def get_users():
      return users_db
  ```

## Running the API

- Start development server:
  ```bash
  uvicorn main:app --reload
  ```

- Access interactive docs at:
  `http://127.0.0.1:8000/docs`