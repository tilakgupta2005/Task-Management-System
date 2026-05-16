from fastapi import APIRouter, HTTPException, Depends, Header, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.auth_service import authenticate_user

router = APIRouter(prefix="/task", tags=["task"])
security = HTTPBearer()

@router.post("/create")
async def create_task(request: Request, user_email: str = Depends(authenticate_user)):
    return user_email

@router.get("/view")
async def get_task(task_id: int):
    return

@router.get("/view/{task_id}")
async def get_task(task_id: int):
    return

@router.put("/update/{task_id}")
async def update_task(task_id: int):
    return

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int):
    return
