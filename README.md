# 📝 Todo-list API

A simple and clean **To-Do List API** built with **FastAPI**, providing full CRUD operations.  
This backend project is perfect for learning, testing, and building on top of FastAPI.

> ⚠️ This project does **not** have authentication yet and is currently **backend only** with no frontend.

---

## 📌 Features

- ✅ Create new tasks
- ✅ Read (list, get by ID)
- ✅ Update existing tasks
- ✅ Delete tasks
- ✅ RESTful API design with Swagger UI

---

## 🧱 Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Framework    | FastAPI                |
| Database     | SQLite + SQLAlchemy    |
| Docs / UI    | Swagger (built-in FastAPI) |
| Dev Tools    | pip, Uvicorn           |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alighotbi/Todo-list.git
cd Todo-list
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

Server will start at
```cpp
http://127.0.0.1:8000
```
---

## 📘 API Documentation
You can test all endpoints with the auto-generated Swagger UI:
```arduino
http://127.0.0.1:8000/docs
```

Or use the ReDoc UI:
```arduino
http://127.0.0.1:8000/redoc
```
