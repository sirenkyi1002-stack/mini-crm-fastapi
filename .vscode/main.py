from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, Base, engine

app = FastAPI()

# Створюємо таблиці (якщо їх ще немає)
Base.metadata.create_all(bind=engine)

# Dependency для отримання сесії
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Database connected!"}

