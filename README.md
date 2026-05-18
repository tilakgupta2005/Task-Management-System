# Task Management System API

A backend Task Management System built using **FastAPI** and **MySQL**, featuring JWT authentication, CRUD operations, and a modular architecture.

---

## 🚀 Features

### Auth
- User Signup
- User Login
- JWT Authentication

### Tasks
- Create Task
- View All Tasks (per user)
- View Task by ID
- Update Task
- Delete Task

### System
- Root endpoint
- Health check endpoint

---

## 🧱 Tech Stack

- Python 3.x
- FastAPI
- MySQL
- PyJWT
- bcrypt
- Pydantic
- mysql-connector-python

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Task-Management-System
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Database Setup

Create the MySQL database and required tables.

```sql
CREATE DATABASE task_management_system;

USE task_management_system;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(100) NOT NULL,
  Email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  due_date DATETIME,
  status VARCHAR(50),
  owner_email VARCHAR(255) NOT NULL,
  FOREIGN KEY (owner_email) REFERENCES users(Email)
);
```

### 6. Configure Application

Update `core/config.py` with your JWT settings:

```python
JWT_SECRET_KEY = "your-secret-key"
JWT_ALGORITHM = "HS256"
```

Update `core/database.py` with your MySQL credentials and port if needed:

```python
# filepath: c:\Users\tilak\Desktop\Task-Management-System\core\database.py
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="task_management_system"
    )
    return conn
```

If your database uses different values, replace `host`, `port`, `user`, `password`, and `database` accordingly.

### 7. Run the App

```bash
uvicorn main:app --reload --port 8000
```

---

## 📦 Project Structure

- `main.py` — FastAPI app entrypoint
- `router/auth.py` — authentication routes
- `router/task.py` — task routes
- `services/auth_service.py` — auth and JWT logic
- `services/task_service.py` — task CRUD logic
- `schema/users.py` — user request models
- `schema/tasks_schema.py` — task request models
- `core/database.py` — MySQL connection helper
- `core/config.py` — JWT and config settings

---

## 🧪 API Endpoints

### Auth

- `POST /auth/signup`
  - Body: `Name`, `Email`, `password`

- `POST /auth/login`
  - Body: `Email`, `password`
  - Response: JWT token

### Tasks

All task routes require the header:

```http
Authorization: Bearer <token>
```

- `POST /task/create`
- `GET /task/view`
- `GET /task/view/{task_id}`
- `PUT /task/update/{task_id}`
- `DELETE /task/delete/{task_id}`

### System

- `GET /`
- `GET /health`

---

## 🧾 Docs and Testing

After running the app, open these URLs in your browser:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Use Swagger UI to test endpoints directly, send requests, and provide the `Authorization` header.

Example curl for login:

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"Email":"you@example.com","password":"yourpassword"}'
```

---

## ⚠️ Notes

- JWT expiration must use a valid expiry claim.
- Store and verify passwords using `bcrypt`.
- Ensure task operations are only allowed for the authenticated task owner.
- If you run into `invalid salt`, check password hashing/storage and use `bcrypt.checkpw()`.
- If you run into `Object of type datetime is not JSON serializable`, ensure JWT `exp` is handled properly.

---

## 📝 License

Use or modify this project for your needs.