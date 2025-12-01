# coursework-moboluw4rin
coursework-moboluw4rin created by GitHub Classroom
# SaaS Prototype - Bias detection in Facial Image Recognition for SKin Tones

## Project Overview
This project is a Software-as-a-Service (SaaS) prototype designed to detect racial bias in AI facial recognition models, focusig on skin tone representation. The system integrate:
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
