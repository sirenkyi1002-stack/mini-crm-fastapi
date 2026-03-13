from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, Base, engine, get_db

app = FastAPI()

# Створюємо таблиці (якщо їх ще немає)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Database connected!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
