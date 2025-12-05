from fastapi import FastAPI, UploadFile, File
from model import YOLOModel

app = FastAPI()
yolo = YOLOModel()

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"

    #saves uploaded image to a temp file
    content = await file.read()
    with open(file_location, "wb") as f:
        f.write(content)

    #YOLO prediction
    results = yolo.predict(file_location)
    return {"predictions": results}

#image_path = "images/messy_desk1.jpg"
#results = yolo.predict(image_path)
#print(results)
