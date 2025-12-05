from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        # Load pretrained YOLO11n
        self.model = YOLO("yolov8n.pt")

    def predict(self, image_path):
        results = self.model.predict(source=image_path)
        return results
