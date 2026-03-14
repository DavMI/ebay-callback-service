from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Basic logger
logging.basicConfig(level=logging.INFO)

@app.post("/callback")
async def callback(request: Request):
    payload = await request.json()
    logging.info(f"Received eBay callback: {payload}")

    # Echo back eBay's verification token during handshake
    if "verificationToken" in payload:
        return {"verificationToken": payload["verificationToken"]}

    # Handle real deletion events
    return {"message": "Callback received"}