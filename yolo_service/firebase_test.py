import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection("detections").stream()
found= False
for doc in docs:
    found = True
    print(f"{doc.id} => {doc.to_dict()}")

if not found:
    print("No documents found in the 'detections' collection")
