from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        # loads YOLOv8 model
        self.model = YOLO("yolov8n.pt")

        # Define items considered "messy" or "clean"
        self.clean_items = ["laptop", "keyboard", "mouse", "book"]
        self.messy_items = ["cup", "bottle", "plate", "pen", "paper", "phone", "bag"]

def predict(self, image_path):
    # runs YOLO inference
    results = self.model.predict(source=image_path)

    # parses raw YOLO detections
    parsed = self._parse_results(results)

    # calculates desk cleanliness score
    score = self._calculate_cleanliness(parsed)

    return {
        "detections": parsed,
        "cleanliness_score": score
    }

def _parse_results(self, results):
    parsed = []

    for r in results:
        class_names = r.names
        for box, conf, cls in zip(r.boxes.xyxy.tolist(),
                                  r.boxes.conf.tolist(),
                                  r.boxes.cls.tolist()):

            parsed.append({
                "box": box,
                "confidence": float(conf),
                "class_id": int(cls),
                "class_name": class_names[int(cls)]
            })

    return parsed

def _calculate_cleanliness(self, detections):
    """
    Cleanliness score is based on number of messy items.
    Score = 100 - (penalty * number_of_messy_items)
    Minimum score = 0
    """
    messy_count = 0

    for item in detections:
        if item["class_name"].lower() in self.messy_items:
            messy_count += 1

    # Penalty per messy item (adjustable)
    penalty = 10
    score = 100 - (messy_count * penalty)

    return max(score, 0)