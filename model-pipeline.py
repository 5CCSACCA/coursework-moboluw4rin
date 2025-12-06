#imports the pre-trained models
from ultralytics import YOLO
import cv2

yolo_model = YOLO("yolov8n.pt")

#accept any type of input
#for YOLO, accpets any image
def load_image(path):
    img =cv2.imread(path)
    if img is None:
        raise ValueError(f"Invalid Image: {path}")
    return img

