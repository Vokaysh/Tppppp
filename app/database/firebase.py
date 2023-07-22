```python
import os
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate(os.getenv('FIREBASE_KEY_PATH'))
default_app = initialize_app(cred)
db = firestore.client()

def update_user_progress(user_id, progress):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set({'progress': progress})

def fetch_user_progress(user_id):
    doc_ref = db.collection('users').document(user_id)
    return doc_ref.get().to_dict()

def send_chat_message(message_details):
    db.collection('chat_messages').add(message_details)

def fetch_chat_messages():
    return [doc.to_dict() for doc in db.collection('chat_messages').stream()]

def update_chatbot_response(chat_request, response):
    doc_ref = db.collection('chat_requests').document(chat_request['id'])
    doc_ref.update({'response': response})
```