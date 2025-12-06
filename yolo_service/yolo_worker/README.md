# YOLO Worker Microservice

## Overview

The YOLO Worker Microservice is responsible for processing desk images sent by students, detecting objects on the desk using YOLO, calculating a cleanliness score, and saving the results to Firestore. It is designed to work as part of a larger SaaS application for monitoring study habits.

This microservice uses **RabbitMQ** to receive image processing requests and **Firebase Firestore** to store the results.

---

## Folder Structure

```
yolo_worker/
│
├─ consumer.py        # Main worker that listens to RabbitMQ queues, processes images with YOLO, and saves to Firestore
├─ firebase_db.py     # Handles Firestore operations: create, read, update, delete detections
├─ Dockerfile         # Dockerfile to containerize this worker
├─ requirements.txt   # Python dependencies
├─ README.md          # This file
└─ .env               # (Optional) environment variables for credentials and RabbitMQ connection
```

---

## Features

1. **YOLO Object Detection**

   * Detects items on a student's study desk.
   * Labels objects with class names and confidence scores.
   * Calculates a cleanliness score based on detected items.

2. **Firestore Database**

   * Stores detection results along with image metadata.
   * Provides endpoints to retrieve, update, or delete previous records.

3. **RabbitMQ Integration**

   * Listens to a queue for new image processing requests.
   * Ensures asynchronous and scalable processing.

---

## Setup & Installation

### Prerequisites

* Docker & Docker Compose
* RabbitMQ instance (can be containerized)
* Firebase credentials JSON file

### Build Docker Container

```bash
docker build -t yolo-worker .
```

### Run Worker

```bash
docker run --env-file .env yolo-worker
```

---

## Environment Variables (`.env`)

```bash
FIREBASE_CREDENTIALS=/path/to/firebase_key.json
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_QUEUE=desk_images
```

---

## How It Works

1. `consumer.py` listens for messages on a RabbitMQ queue.
2. When a new image is received:

   * YOLO detects objects in the image.
   * The cleanliness score is calculated.
   * Detection results are saved to Firestore using `firebase_db.py`.
3. Other services can retrieve, update, or delete results via Firestore endpoints.

---

## Example Request (via RabbitMQ)

Message payload:

```json
{
  "image_name": "messy_desk1.jpg",
  "image_path": "/path/to/image/messy_desk1.jpg",
  "student_id": "12345"
}
```

---

## Dependencies

See `requirements.txt` for full list of dependencies, including:

* `pika` for RabbitMQ
* `firebase-admin` for Firestore
* `ultralytics` for YOLO inference
* `torch` for model computations
