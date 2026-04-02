from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "database connection successful!"}

@app.post("/users")
def create_user(user: User):
    return {"message": "User created", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

