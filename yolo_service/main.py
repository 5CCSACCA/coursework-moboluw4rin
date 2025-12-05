from model import YOLOModel

yolo = YOLOModel()

image_path = "path/to/sample.jpg"
results = yolo.predict(image_path)
print(results)
