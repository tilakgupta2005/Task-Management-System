from fastapi import APIRouter, HTTPException, Depends, Header, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.auth_service import authenticate_user
from services.task_service import *

router = APIRouter(prefix="/task", tags=["task"])
security = HTTPBearer()

@router.post("/create")
async def create_task(task_data: CreateTask, user_email: str = Depends(authenticate_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        task_create(user_email, task_data)
        return JSONResponse(content={"message": "Task created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/view")
async def get_task(user_email: str = Depends(authenticate_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        tasks, count = get_tasks(user_email)
        return JSONResponse(content={"success": True, "count": count, "tasks": tasks}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/view/{task_id}")
async def get_task(task_id: int, user_email: str = Depends(authenticate_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        tasks, count = get_taskby_id(task_id, user_email)
        if count == 0:
            return JSONResponse(content={"message": "Task not found"}, status_code=404)
        return JSONResponse(content={"success": True, "count": count, "tasks": tasks}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update/{task_id}")
async def update_task(task_id: int, task_data: UpdateTask, user_email: str = Depends(authenticate_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        if update_taskby_id(task_id, user_email, task_data):
            return JSONResponse(content={"message": "Task updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Task not found or Update details are missing"}, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, user_email: str = Depends(authenticate_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        if delete_taskby_id(task_id, user_email):
            return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Task not found"}, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
