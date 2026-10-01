# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining routes, validating request data, using HTTP methods and status codes, and testing endpoints through FastAPI's interactive documentation.

## 📝 Tasks

### 🛠️ Define Task Read Endpoints

#### Description
Complete the `GET` endpoints in the starter code so clients can list tasks and retrieve one task by its ID.

#### Requirements
Completed program should:

- Return all tasks from `GET /tasks`.
- Return the matching task from `GET /tasks/{task_id}`.
- Return an HTTP 404 response when a requested task ID does not exist.

### 🛠️ Create and Update Tasks

#### Description
Implement the endpoints that create a task and replace an existing task's details. Use the provided Pydantic model to validate incoming data.

#### Requirements
Completed program should:

- Create a task with `POST /tasks` and return the created task with HTTP 201.
- Assign each new task a unique ID.
- Update an existing task with `PUT /tasks/{task_id}` and return HTTP 404 if the ID does not exist.

### 🛠️ Delete and Test Tasks

#### Description
Implement task deletion, then run the API and try each endpoint in FastAPI's interactive docs.

#### Requirements
Completed program should:

- Delete a task with `DELETE /tasks/{task_id}` and return HTTP 404 if the ID does not exist.
- Return HTTP 204 when a task is deleted successfully.
- Start the API with the following commands, then open `http://127.0.0.1:8000/docs` to test it:

  ```bash
  python -m pip install fastapi uvicorn
  uvicorn main:app --reload
  ```