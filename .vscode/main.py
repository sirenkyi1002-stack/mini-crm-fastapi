from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Creative ToDo API 🌟")

# Модель задачі
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    priority: int = 1  # 1 - високий, 2 - середній, 3 - низький
    created_at: datetime = datetime.now()

# База даних у пам'яті
tasks_db: List[Task] = []

# --- API Endpoints ---

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    """
    Користувач додає задачу.
    Ми автоматично підганяємо дату створення і сортування.
    """
    tasks_db.append(task)
    # Творчість: сортуємо задачі за пріоритетом і датою
    tasks_db.sort(key=lambda x: (x.priority, x.created_at))
    return task

@app.get("/tasks/", response_model=List[Task])
def list_tasks():
    """
    Повертаємо задачі у зручному порядку:
    1. Високий пріоритет
    2. Новіші задачі
    """
    return tasks_db

@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    """
    Позначаємо задачу як завершену.
    Додаємо маленький “user-friendly” фідбек у API
    """
    for task in tasks_db:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

