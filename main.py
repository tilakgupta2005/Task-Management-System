from fastapi import FastAPI
from router import auth, task
from schema.users import *

app = FastAPI()
app.include_router(auth.router)
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"message": "Task Management System API"}

@app.get("/health")
def health_check():
    return{
        "status": "OK"
    }