```python
import os
from openai import OpenAI, ChatCompletion

class OpenAIChatbot:
    def __init__(self):
        self.openai = OpenAI(os.getenv("OPENAI_API_KEY"))

    async def generate_response(self, message):
        chat = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )
        return chat['choices'][0]['message']['content']
```