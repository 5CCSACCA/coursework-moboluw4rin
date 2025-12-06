"""
Saves detection data to a firestore database. 
Has endpoints to update, retrieve or delete data from the Firestore database.
"""
import firebase_admin
from firebase_admin import credentials, firestore

# initialize firebase admin
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

# get firestore client
db = firestore.client()

# save a detection record, stores a single detected object
def save_detection(label, confidence, x1, y1, x2, y2, image_path):
    doc_ref = db.collection("detections").document()
    doc_ref.set({
        "label": label,
        "confidence": confidence,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "image_path": image_path
    })
    return doc_ref.id

def update_image_path(doc_id, new_image_path):
    doc_ref = db.collection("detections").document(doc_id)
    try:
        doc_ref.update({"image_path": new_image_path})
        print(f"Updated image_path for document {doc_id} to '{new_image_path}'")
    except Exception as e:
        print(f"Error updating document {doc_id}: {e}")
    
#CRUD operations
def get_doc_data(doc_id):
    doc_ref = db.collection("detections").document(doc_id)
    doc_snap = doc_ref.get()
    return doc_snap.to_dict() if doc_snap.exists else None    

def edit_doc_data(doc_id, new_info):
    doc_ref = db.collection("detections").document(doc_id)
    doc_ref.update(new_info)

def delete_doc_data(doc_id):
    doc_ref = db.collection("detections").document(doc_id)
    doc_ref.delete()
