from fastapi import FastAPI
from model import BitNetModel

app = FastAPI()
llm = BitNetModel()

@app.get("/")
def root():
    return {"message": "BitNet LLM service is running."}

@app.post("/analyse-text")
def analyse_text(input_data: dict):
    """
    Input example:
    {
      "yolo_result": "Detected cup, bottle, book, clutter score 72"
    }
    """
    prompt = f"You are an academic productivity assistant. Based on the following desk analysis, give feedback: {input_data['yolo_result']}"
    
    response = llm.generate_text(prompt)
    return {"analysis": response}

