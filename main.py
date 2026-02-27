
from fastapi import FastAPI

app = FastAPI()


clients = [
    {"id": 1, "name": "Artem", "balance": 1000},
    {"id": 2, "name": "Olena", "balance": 2500},
    {"id": 3, "name": "Ivan", "balance": 500},
]


@app.get("/")
def root():
    return {"message": "Mini CRM працює "}


@app.get("/clients")
def get_clients():
    return clients


