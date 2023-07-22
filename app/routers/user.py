```python
from fastapi import APIRouter, HTTPException
from app.models.user import UserProgress
from app.database.firebase import update_user_progress, fetch_user_progress
from app.utils.error_handling import handle_exception
from app.utils.logging import log_request

router = APIRouter()

@router.post("/user/{user_id}/update_progress")
async def update_progress(user_id: str, user_progress: UserProgress):
    try:
        log_request("Update user progress", user_id, user_progress)
        result = await update_user_progress(user_id, user_progress)
        return {"message": "User progress updated successfully", "result": result}
    except Exception as e:
        handle_exception(e)

@router.get("/user/{user_id}/fetch_progress")
async def fetch_progress(user_id: str):
    try:
        log_request("Fetch user progress", user_id)
        result = await fetch_user_progress(user_id)
        return {"message": "User progress fetched successfully", "result": result}
    except Exception as e:
        handle_exception(e)
```