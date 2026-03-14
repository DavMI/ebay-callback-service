from fastapi import FastAPI, Request
import logging

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# IMPORTANT: This must match EXACTLY what you enter in the eBay portal
VERIFICATION_TOKEN = "D4V3-PR0J3CT-C0M1C-D4T4-H1ST0RY-TR4CK1NG-2026"

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/callback")
async def callback(request: Request):
    try:
        payload = await request.json()
    except Exception:
        logging.warning("Invalid JSON received")
        return {"error": "Invalid JSON"}

    logging.info(f"Received eBay callback: {payload}")

    # eBay validation handshake
    if "verificationToken" in payload:
        return {"verificationToken": VERIFICATION_TOKEN}

    # Normal deletion event
    return {"status": "received"}