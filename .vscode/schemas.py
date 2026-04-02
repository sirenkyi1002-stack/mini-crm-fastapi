from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    done: bool = False
    user_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool
    user_id: int

    class Config:
        from_attributes = True
