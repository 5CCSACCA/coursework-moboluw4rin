# SaaS: Bias detection in Facial Image Recognition for SKin Tones

## Project Overview
This project is a Software-as-a-Service (SaaS) prototype designed to detect racial bias in AI facial recognition models, focusing on skin tone representation. The system integrate:
- YOLO: Detects faces in images, provides confidence scores and assigns a skin-tone label.
- BitNet: Analyses detection results and produces a textual summary highlighting potential biases.
- FastAPI: Serves both services as a single, user-friendly API.
This project centres around AI ethics, specifically algorithmic bias against darker-skinned women, and demonstrates how AI systems can be audited for fairness and transparency

## Features
- Detects faces in images with bounding boxes and confidence scores.  
- Aggregates confidence scores by skin tone categories.  
- Uses an LLM to generate a text summary of potential bias patterns.  
- Fully containerized with Docker and Docker Compose for reproducibility.  
- Lightweight and CPU-friendly: designed to run on 4 CPUs with 16GB RAM.

## System Architecture
User Upload → YOLO11n → Data Processing → BitNet → FastAPI API → JSON Output

## GitFlow Guidelines
- `main` branch: contains final, production-ready code.  
- `develop` branch: ongoing development.  
- `feature/*`: individual features.  
- `release/*` and `hotfix/*`: optional for testing and fixes.  
- All pull requests must be merged into `develop` before release to `main`.

## Installation & Deployment on Linux

### Prerequisites
- Linux machine with **Docker** and **Docker Compose** installed  
- Python 3.10+ (for local scripts/testing)  
- Git

### 1. Clone Repository
```bash
git clone https://github.com/5CCSACCA/coursework-moboluw4rin/bias-detection-saas.git
cd bias-detection-saas
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

## Example Usage 
## Testing
## Directory Structure
```
bias-detection-saas/
│
├── yolo/                  # YOLO service Dockerfile & scripts
├── bitnet/                # BitNet service Dockerfile & scripts
├── fastapi/               # FastAPI API Dockerfile & app code
├── examples/              # Example images for testing
├── tests/                 # Unit and integration tests
├── docker-compose.yml     # Compose orchestration
├── deploy_build.sh         # Script to build containers
├── deploy_run.sh           # Script to run containers
└── README.md
```
