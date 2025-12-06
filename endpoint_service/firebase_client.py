import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key
cred = credentials.Certificate("feature/firebase/firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
