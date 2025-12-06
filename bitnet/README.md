# BitNet LLM Microservice

This microservice wraps Microsoft's BitNet model into a FastAPI endpoint.

## Purpose
- Receive YOLO object detection results.
- Generate feedback and study-habit suggestions.
- Serve text responses to the API Gateway.

## Endpoints

### GET /
Health check.

### POST /analyse-text
Input:
```json
{
  "yolo_result": "Detected cup, bottle, laptop, clutter score 80"
}
Output:
{
  "analysis": "Your desk has several loose items..."
}
Run with Docker
```
```
docker-compose up --build
```
Runs on port 9002
http://localhost:9002

### Summary — What Goes in `feature/bitnet-service`

| File | Purpose |
|------|---------|
| Dockerfile | Build the container and run Uvicorn |
| docker-compose.yml | Expose port 9002 and run container |
| requirements.txt | Dependencies (FastAPI + BitNet) |
| model.py | Loads and runs BitNet model |
| app.py | FastAPI server exposing `/analyse-text` |
| README.md | Documentation |
