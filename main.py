from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    password: str
    email: str
    id: int


user_data = {
    "user_name": "Test User",
    "password": "secretpassword",
    "email": "email@gmail.com",
    "id": 1
}

user = User(**user_data)
print(user)
