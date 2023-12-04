from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    id: int

    @field_validator('id')
    def id_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"id must be positive: {value}")
        return value


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

user = User(**user_data)
# print(user)
# print(user.email)

user_json_string = user.model_dump_json()
print(user_json_string)
