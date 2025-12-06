from model import YOLOModel
from firebase_db import save_detection

print("Initializing YOLO model...")
yolo = YOLOModel()
print(dir(yolo))
print("YOLO model loaded successfully.\n")

# Path to your test image
image_path = "images/messy_desk1.jpg"
print(f"Running prediction on image: {image_path}")

# Run YOLO prediction
results = yolo.predict(image_path)

print("\n--- Prediction Results ---")
print(f"Cleanliness Score: {results['cleanliness_score']}/100")
print("Detected Objects:")
for det in results['detections']:
    print(f" - {det['class_name']} | Confidence: {det['confidence']:.2f} | Box: {det['box']}")

# Save each detected object to Firebase
print("\nSaving detections to Firebase...")
for det in results['detections']:
    doc_id = save_detection(
        label=det['class_name'],
        confidence=det['confidence'],
        x1=det['box'][0],
        y1=det['box'][1],
        x2=det['box'][2],
        y2=det['box'][3],
        image_path=image_path
    )
    print(f"Saved detection with ID: {doc_id}")

print("\nAll detections saved successfully!")
