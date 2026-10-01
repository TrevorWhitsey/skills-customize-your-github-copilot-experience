from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    raise NotImplementedError("Complete this endpoint")


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput) -> Task:
    raise NotImplementedError("Complete this endpoint")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput) -> Task:
    raise NotImplementedError("Complete this endpoint")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    raise NotImplementedError("Complete this endpoint")