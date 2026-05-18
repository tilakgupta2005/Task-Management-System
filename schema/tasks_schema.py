from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal, Optional
import re

class CreateTask(BaseModel):
    Title: Annotated[str, Field(..., min_length=3, max_length=100, title="Title", description="The title of the task")]
    Description: Annotated[str, Field(..., min_length=10, max_length=500, title="Description", description="The description of the task")]
    Status: Annotated[Literal["pending", "in progress", "completed"], Field(..., title="Status", description="The status of the task (e.g., pending, in progress, completed)")]
    Priority: Annotated[Literal["low", "medium", "high"], Field(..., title="Priority", description="The priority of the task (e.g., low, medium, high)")]  
    Due_Date: Annotated[str, Field(..., title="Due Date", description="The due date of the task in YYYY-MM-DD format")]

    @field_validator('Due_Date')
    @classmethod
    def validate_due_date(cls, v: str) -> str:
        """Validate due date format"""
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', v):
            raise ValueError("Due date must be in YYYY-MM-DD format")
        return v
    

class UpdateTask(BaseModel):
    Title: Annotated[Optional[str], Field(None, min_length=3, max_length=100, title="Title", description="The title of the task")]
    Description: Annotated[Optional[str], Field(None, min_length=10, max_length=500, title="Description", description="The description of the task")]
    Status: Annotated[Optional[Literal["pending", "in progress", "completed"]], Field(None, title="Status", description="The status of the task (e.g., pending, in progress, completed)")]
    Priority: Annotated[Optional[Literal["low", "medium", "high"]], Field(None, title="Priority", description="The priority of the task (e.g., low, medium, high)")]  
    Due_Date: Annotated[Optional[str], Field(None, title="Due Date", description="The due date of the task in YYYY-MM-DD format")]

    @field_validator('Due_Date')
    @classmethod
    def validate_due_date(cls, v: str) -> str:
        """Validate due date format"""
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', v):
            raise ValueError("Due date must be in YYYY-MM-DD format")
        return v