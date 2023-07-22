```python
from fastapi import HTTPException

def handle_error(status_code: int, detail: str):
    raise HTTPException(status_code=status_code, detail=detail)

def handle_404(detail: str = "Not Found"):
    handle_error(404, detail)

def handle_500(detail: str = "Internal Server Error"):
    handle_error(500, detail)
```