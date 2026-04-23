from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# 1. Завантажуємо .env
load_dotenv()

# 2. Беремо URL бази
DATABASE_URL = os.getenv("DATABASE_URL")

# (опціонально, але круто)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

# 3. Створюємо engine і сесію
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
