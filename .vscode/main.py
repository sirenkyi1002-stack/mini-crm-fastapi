
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from routes.clients import router as clients_router

app = FastAPI(title="Creative Tasks API")

# Регіструємо router для clients
app.include_router(clients_router)

# Модель задачі
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    priority: int = 1  # 1 - високий, 2 - середній, 3 - низький
    created_at: datetime = Field(default_factory=datetime.now)

# База даних у пам'яті
tasks_db: List[Task] = []


# --- API Endpoints ---

# Create
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks_db.append(task)
    tasks_db.sort(key=lambda x: (x.priority, x.created_at))
    return task

# Read (list all)
@app.get("/tasks/", response_model=List[Task])
def list_tasks():
    return tasks_db

# Read (one by id)
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update (full replace)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Update (mark complete)
@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            deleted_task = tasks_db.pop(index)
            return {"message": "Task deleted", "task": deleted_task}
    raise HTTPException(status_code=404, detail="Task not found")


