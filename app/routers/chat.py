```python
from fastapi import APIRouter, HTTPException
from app.models.chat import ChatMessage, ChatResponse
from app.database.firebase import get_db
from app.chatbot.openai import generate_response
from app.utils.error_handling import handle_exception
from app.utils.logging import log_info, log_error

router = APIRouter()

@router.post("/chat/send_message")
async def send_message(message: ChatMessage, db = Depends(get_db)):
    try:
        log_info(f"Sending message: {message}")
        db.collection('chat').add(message.dict())
        return {"message": "Message sent successfully"}
    except Exception as e:
        log_error(f"Error sending message: {e}")
        handle_exception(e)

@router.get("/chat/get_messages")
async def get_messages(db = Depends(get_db)):
    try:
        log_info("Fetching chat messages")
        messages = [doc.to_dict() for doc in db.collection('chat').stream()]
        return {"messages": messages}
    except Exception as e:
        log_error(f"Error fetching messages: {e}")
        handle_exception(e)

@router.post("/chat/generate_response")
async def generate_chat_response(request: ChatResponse):
    try:
        log_info(f"Generating chatbot response for request: {request}")
        response = generate_response(request.message)
        return {"response": response}
    except Exception as e:
        log_error(f"Error generating chatbot response: {e}")
        handle_exception(e)
```
