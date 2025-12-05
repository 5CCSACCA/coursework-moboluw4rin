from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

YOLO_SERVICE_URL = "http://localhost:9001/predict"
BITNET_SERVICE_URL = "http://localhost:9002/analyse-text"

@app.post("/analyse")
async def analyse(file: UploadFile = File(...)):
    # Save file temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    #Call YOLO service
    #YOLO prediction
    yolo_response = requests.post(YOLO_SERVICE_URL, files={"image": open(file_location, "rb")})
    detected_objects = yolo_response.json()

    #Call BitNet service
    #BitNet analysis
    llm_response = requests.post(BITNET_SERVICE_URL, json={"text": str(detected_objects)})
    analysis = llm_response.json()

    return {"yolo": detected_objects, "analysis": analysis}
