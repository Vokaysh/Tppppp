```python
from pydantic import BaseModel
from typing import Optional

class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: Optional[str]

class ChatResponse(BaseModel):
    bot_response: str
    timestamp: Optional[str]
```