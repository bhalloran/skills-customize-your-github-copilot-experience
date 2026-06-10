# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to practice designing endpoints, using Pydantic models for validation, and handling HTTP request/response flows.

## 📝 Tasks

### 🛠️ Create a REST API with FastAPI

#### Description
Implement a simple CRUD API for an `Item` resource. The API should allow clients to create, read, update, and delete items. Use Pydantic models for request/response validation and run the app with Uvicorn.

#### Requirements
Completed project should:

- Implement endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, and `DELETE /items/{id}`
- Use a Pydantic `Item` model for input validation and responses
- Return appropriate HTTP status codes (201 for create, 204 for delete, 404 when not found, etc.)
- Validate and handle error conditions (duplicate IDs, missing items, invalid input)
- Include example requests and run instructions

#### Example requests

Create an item:

```bash
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"id":1,"name":"Sword","description":"A sharp blade"}'
```

List items:

```bash
curl http://localhost:8000/items
```

Get an item:

```bash
curl http://localhost:8000/items/1
```

Run instructions

```bash
pip install -r requirements.txt
uvicorn starter-code:app --reload
```
