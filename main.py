from fastapi import FastAPI, HTTPException

app = FastAPI()

# Список клієнтів (fake data)
clients = [
    {"id": 1, "name": "Artem", "email": "artem@gmail.com"},
    {"id": 2, "name": "Olena", "email": "olena@gmail.com"},
    {"id": 3, "name": "Ivan", "email": "ivan@gmail.com"},
]

# Головна сторінка
@app.get("/")
def read_root():
    return {"message": "Mini CRM працює"}

# Список усіх клієнтів
@app.get("/clients")
def get_clients():
    return clients

# Один клієнт по id
@app.get("/clients/{client_id}")
def get_client(client_id: int):
    for client in clients:
        if client["id"] == client_id:
            return client
    raise HTTPException(status_code=404, detail="Клієнт не знайдений")
