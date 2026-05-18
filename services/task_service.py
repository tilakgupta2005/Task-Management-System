from fastapi import HTTPException, Request
from pydantic import EmailStr
from schema.tasks_schema import *
from core.database import get_connection

def task_create(email: EmailStr, task_data: CreateTask):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (title, description, status, priority, due_date, created_by) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (task_data.Title, task_data.Description, task_data.Status, task_data.Priority, task_data.Due_Date, email))
    conn.commit()
    cursor.close()
    conn.close()


def get_tasks(email: EmailStr):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id, title, description, status, priority, due_date FROM tasks WHERE created_by = %s"
    cursor.execute(query, (email,))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()

    task_list = []

    count = len(tasks)

    for task in tasks:

        task_list.append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "status": task[3],
            "priority": task[4],

            "due_date": (
                task[5].isoformat()
                if task[5] else None
            )
        })

    return task_list, count


def get_taskby_id(task_id: int, email: EmailStr):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id, title, description, status, priority, due_date FROM tasks WHERE id = %s AND created_by = %s"
    cursor.execute(query, (task_id, email))
    task = cursor.fetchone()
    cursor.close()
    conn.close()

    if not task:
        return None, 0

    task_data = {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "status": task[3],
        "priority": task[4],
        "due_date": (
            task[5].isoformat()
            if task[5] else None
        )
    }

    return task_data, 1

def update_taskby_id(task_id: int, email: EmailStr, task_data: UpdateTask):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id FROM tasks WHERE id = %s AND created_by = %s"
    cursor.execute(query, (task_id, email))
    task = cursor.fetchone()
    if not task:
        cursor.close()
        conn.close()
        return False
    
    update_fields = task_data.model_dump(exclude_unset=True)
    if not update_fields:
        cursor.close()
        conn.close()
        return False
    
    set_clause = ", ".join([f"{key} = %s" for key in update_fields.keys()])
    values = list(update_fields.values())
    values.extend([task_id, email])

    query = f"""UPDATE tasks SET {set_clause} WHERE id = %s AND created_by = %s"""
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def delete_taskby_id(task_id: int, email: EmailStr):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id, title, description, status, priority, due_date FROM tasks WHERE id = %s AND created_by = %s"
    cursor.execute(query, (task_id, email))
    task = cursor.fetchone()
    print(task)
    if not task:
        cursor.close()
        conn.close()
        return False
    query = "DELETE FROM tasks WHERE id = %s AND created_by = %s"
    cursor.execute(query, (task_id, email))
    conn.commit()
    cursor.close()
    conn.close()
    return True
