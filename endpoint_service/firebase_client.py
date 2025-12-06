from fastapi import HTTPException, Header
import firebase_admin
from firebase_admin import auth, firestore

#path to your service account key
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

def verify_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print("Invalid token:", e)
        return None

async def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")
    token = authorization.split(" ")[1]
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return decoded

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...), user=Depends(get_current_user)):
    image_bytes = await file.read()
    message = aio_pika.Message(body=image_bytes)
    await app.state.channel.default_exchange.publish(message, routing_key="image_tasks")
    return {"status": "queued"}