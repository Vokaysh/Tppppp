```python
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import user, chat
from app.utils import error_handling, logging

load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logging.log_info("Starting up the server")

@app.on_event("shutdown")
async def shutdown_event():
    logging.log_info("Shutting down the server")

app.include_router(user.router)
app.include_router(chat.router)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return error_handling.handle_exception(exc)
```