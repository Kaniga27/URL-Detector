from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize app
app = FastAPI()

# Allow frontend (React) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input format
class UrlRequest(BaseModel):
    url: str

# Prediction endpoint
@app.post("/predict")
async def predict(request: UrlRequest):
    url = request.url

    # -------------------------------
    # 🔹 Dummy logic (replace with ML model later)
    # -------------------------------
    if "login" in url or "bank" in url or "verify" in url:
        prediction = "phishing"
    else:
        prediction = "legitimate"

    # ✅ Must return JSON with "prediction" field
    return {"prediction": prediction}
