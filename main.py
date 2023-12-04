from pydantic import BaseModel, EmailStr


class User(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    id: int


user_data = {
    "user_name": "Test User",
    "password": "secretpassword",
    "email": "email@gmail.com",
    "id": 1
}

user_wrong = {
    "user_name": "Test User",
    "password": "secretpassword",
    "email": "email",
    "id": "hello"
}

user = User(**user_wrong)
print(user)
print(user.email)
