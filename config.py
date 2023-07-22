```python
# config.py

from constants import DATABASE_NAME, DATABASE_HOST, DATABASE_PORT

class Config:
    def __init__(self):
        self.database_name = DATABASE_NAME
        self.database_host = DATABASE_HOST
        self.database_port = DATABASE_PORT

    def get_database_config(self):
        return {
            'database_name': self.database_name,
            'database_host': self.database_host,
            'database_port': self.database_port,
        }
```