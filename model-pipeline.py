#imports
from ultralytics import YOLO
from bitnet import BitNet
import cv2

yolo_model = YOLO("yolov8n.pt")
bitnet_model = BitNet.load_pretrained()

#accept any type of input
def load_image(path):
    img =cv2.imread(path)
    if img is None:
        raise ValueError(f"Invalid Image: {path}")
    return img