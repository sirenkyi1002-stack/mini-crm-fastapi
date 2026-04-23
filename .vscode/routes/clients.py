import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Client

router = APIRouter()


def build_clients_dataframe(clients):
    """Конвертує список клієнтів у pandas DataFrame"""
    return pd.DataFrame([{
        'id': c.id,
        'name': c.name,
        'email': c.email,
        'city': c.city
    } for c in clients])


def calculate_stats(df):
    """Обчислює статистику по клієнтам"""
    return {
        'total': len(df),
        'unique_cities': df['city'].nunique()
    }


def group_by_city(df):
    """Групує клієнтів по містам"""
    return df.groupby('city').size().to_dict()


@router.get("/clients")
def get_clients():
    return {"message": "list of clients"}


@router.get("/clients/stats")
def get_clients_stats(db: Session = Depends(get_db)):
    """
    Повертає статистику по клієнтам:
    - Загальна кількість
    - Унікальні міста
    - Кількість клієнтів по містам
    """
    clients = db.query(Client).all()

    if not clients:
        return {"message": "No clients found"}

    df = build_clients_dataframe(clients)

    stats = calculate_stats(df)
    by_city = group_by_city(df)

    return {
        "stats": stats,
        "by_city": by_city
    }

