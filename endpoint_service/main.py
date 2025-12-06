# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI(title="YOLO Detection Service")

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read uploaded file
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes))

        # Perform inference
        results = model.predict(img)

        detections = []
        for result in results:
            for box, cls, conf in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
                detections.append({
                    "class_id": int(cls),
                    "confidence": float(conf),
                    "bbox": [float(x) for x in box]
                })

        return JSONResponse(content={"detections": detections})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
