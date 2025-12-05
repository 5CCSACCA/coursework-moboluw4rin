# SaaS: Desk Cleanliness Checker – SaaS Microservices Application
## Project Overview
This project is a Software-as-a-Service (SaaS) prototype designed for Students! Students often struggle with staying organised while studying. Research suggests that a clean study environment reduces stress and improves focus.

## Features
This SaaS tool provides:
- Desk Object Detection
- Cleanliness Scoring System
- Study Habit Insights
- Motivational and behavioural guidance

## System Architecture
The Desk Cleanliness Checker is a microservice-based SaaS project that uses:
- YOLO (Ultralytics): to detect objects on a desk (cups, bottles, books, keyboards, laptops, food items, clutter objects, etc.)
- BitNet LLM (Microsoft): to interpret results, generate feedback, and provide study-habit suggestions
- FastAPI Gateway: to coordinate YOLO + LLM services
- Firebase: user authentication & cloud storage (optional)
- Database: store analysis history
- Docker + docker-compose: full microservices deployment

## GitFlow Guidelines
- `main` branch: contains final, production-ready code.  
- `develop` branch: ongoing development.  
- `feature/*`: individual features.  
- All pull requests must be merged into `dev` before release to `main`.

## Installation & Deployment on Linux

### Prerequisites
- Linux machine with **Docker** and **Docker Compose** installed  
- Python 3.10+ (for local scripts/testing)  
- Git

### 1. Clone Repository
```bash
git clone https://github.com/5CCSACCA/coursework-moboluw4rin.git
cd coursework-moboluw4rin
```
### 2. Build Docker Images
```bash
./deploy_build.sh
#!/bin/bash
docker-compose build
```

### 3. Run the SaaS
```bash
./deploy_run.sh
#!/bin/bash
docker-compose up
```

## How it works: Example Usage 
YOLO Service

- Receives an uploaded image
- Detects objects (cups, bottles, books, laptops, snacks, clutter)
- Returns JSON containing bounding boxes + classes
- Computes a basic clutter score

Example return: 
```
{
  "objects": ["cup", "bottle", "laptop", "book"],
  "clutter_score": 72
}
```
BitNet LLM Service

Receives the JSON from YOLO and generates:

- Cleanliness explanation
- Study habit advice
- Optional productivity motivation

Example:

“Your desk is moderately cluttered with cups, bottles, and loose items. Try removing drink containers and grouping books together to improve focus.”

## Directory Structure
```
Main
│
├── feature/yolo
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── main.py
│   ├── model.py
│   └── README.md
│
├── feature/bitnet
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── docker-compose.yml
│   ├── app.py
│   └── README.md
│
├── feature/fastapi
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── docker-compose.yml
│   ├── app.py
│   └── README.md
│
├── feature/database
│   ├── docker-compose.yml
│   ├── init.sql
│   └── README.md
│
├── feature/firebase
│   ├── firebase_config.json
│   └── README.md
│
└── review-branch

