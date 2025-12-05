from model import YOLOModel

yolo = YOLOModel()

image_path = "images/messy_desk1.jpg"
results = yolo.predict(image_path)
print(results)
