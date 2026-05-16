from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.post("/create")
async def create_task():
    return

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
