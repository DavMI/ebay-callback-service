from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Basic logger
logging.basicConfig(level=logging.INFO)

@app.post("/callback")
async def callback(request: Request):
    try:
        payload = await request.json()
    except Exception:
        return {"error": "Invalid JSON"}

    logging.info(f"Received eBay callback: {payload}")

    # Echo back eBay's verification token during handshake
    if "verificationToken" in payload:
        return {"verificationToken": payload["verificationToken"]}

    return {"message": "Callback received"}