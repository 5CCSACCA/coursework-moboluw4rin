from fastapi import FastAPI
from model import BitNetModel, BitNetLLM
from pydantic import BaseModel

app = FastAPI(title="BitNet LLM Service")
llm = BitNetModel()

class FeedbackRequest(BaseModel):
    cleanliness_score: int
    detections: list   #list of dicts from YOLO ouput

@app.get("/")
def root():
    return {"message": "BitNet LLM service is running."}

@app.post("/generate")
def generate_feedback(request: FeedbackRequest):
    feedback = llm.generate_feedback(cleanliness_score=request.cleanliness_score, detections=request.detections)
    return {"feedback": feedback}

