from firebase_db import save_detection, db

# Add a sample detection
doc_id = save_detection(
    label="pen",
    confidence=0.95,
    x1=10,
    y1=20,
    x2=50,
    y2=60,
    image_path="test_image.jpg"
)

print(f"Saved test document with ID: {doc_id}")

# Retrieve all documents to verify
docs = db.collection("detections").stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
