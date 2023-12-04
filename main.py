from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    id: int

    @validator('id')
    def id_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"id must be positive: {value}")
        return value


user_data = {
    "user_name": "Test User",
    "password": "secretpassword",
    "email": "email@gmail.com",
    "id": -1
}

user_wrong = {
    "user_name": "Test User",
    "password": "secretpassword",
    "email": "email",
    "id": "hello"
}

user = User(**user_data)
print(user)
print(user.email)
