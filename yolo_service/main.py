from fastapi import FastAPI, UploadFile, File
from model import YOLOModel
from fastapi.responses import JSONResponse

app = FastAPI(title="YOLO Detection Service")

yolo = YOLOModel()

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Save uploaded image
        file_location = f"temp_{file.filename}"
        content = await file.read()
        with open(file_location, "wb") as f:
            f.write(content)

        # Run YOLO
        results = yolo.predict(file_location)

        # Parse YOLO Results → JSON serializable format
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class_id": int(box.cls[0]),
                    "confidence": float(box.conf[0]),
                    "bbox": [float(x) for x in box.xyxy[0].tolist()]
                })

        return JSONResponse(content={"detections": detections})

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
