from fastapi import FastAPI
from model import BitNetModel

app = FastAPI()
llm = BitNetModel()

@app.get("/")
def root():
    return {"message": "BitNet LLM service is running."}

@app.post("/analyse-text")
def analyse_text(input_data: dict):
    prompt = input_data["text"]
    response = llm.generate_text(prompt)
    return {"analysis": response}

