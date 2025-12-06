from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        self.model = YOLO("yolov8n.pt") 

    def predict(self, image_path):
        results = self.model.predict(source=image_path)
        return self._parse_results(results)

    def _parse_results(self, results):
        parsed = []
        for r in results:
            parsed.append({
                "boxes": r.boxes.xyxy.tolist(),
                "confidence": r.boxes.conf.tolist(),
                "classes": r.boxes.cls.tolist(),
                "names": r.names
            })
        return parsed
