# app.py
from fastapi import FastAPI, UploadFile, File
import requests
from firebase_client import db

app = FastAPI()

YOLO_SERVICE_URL = "http://localhost:9001/predict"
BITNET_SERVICE_URL = "http://localhost:9002/analyse-text"


@app.post("/analyse")
async def analyse(file: UploadFile = File(...)):
    # Save the uploaded file
    file_location = f"temp_{file.filename}"
    content = await file.read()
    with open(file_location, "wb") as f:
        f.write(content)

    # Call YOLO microservice
    yolo_response = requests.post(
        YOLO_SERVICE_URL,
        files={"file": open(file_location, "rb")}
    )
    detected_objects = yolo_response.json()

    # Call BitNet microservice
    llm_response = requests.post(
        BITNET_SERVICE_URL,
        json={"text": str(detected_objects)}
    )
    analysis = llm_response.json()

    # Save results to Firebase
    doc_ref = db.collection("requests").document()
    doc_ref.set({
        "image_name": file.filename,
        "yolo_output": detected_objects,
        "llm_output": analysis
    })

    return {
        "yolo": detected_objects,
        "analysis": analysis
    }


@app.get("/history")
def get_history():
    docs = db.collection("requests").stream()
    result = []
    for doc in docs:
        entry = doc.to_dict()
        entry["id"] = doc.id
        result.append(entry)
    return result