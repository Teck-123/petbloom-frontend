import firebase_admin
from firebase_admin import credentials, auth
from app.config import get_settings
import os
import json

def init_fbase():
    settings = get_settings()
    if not firebase_admin._apps:
        cred_path = settings.FBASE_CREDENTIALS
        try:
            # Check if FBASE_CREDENTIALS is a JSON string (for Railway/environment)
            if cred_path and cred_path.startswith('{'):
                cred_dict = json.loads(cred_path)
                cred = credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred)
            # Check if it's a file path
            elif cred_path and os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            else:
                print("Warning: Firebase credentials not configured. Using default credentials.")
        except Exception as e:
            print(f"Warning: Failed to initialize Firebase: {e}")

def verify_fbase_token(token: str):
    try:
        init_fbase()
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
