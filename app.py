from fastapi import FastAPI, Request
import hashlib
import logging
from urllib.parse import urlparse

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# MUST match exactly what you enter in the eBay Developer Portal
VERIFICATION_TOKEN = "D4V3-PR0J3CT-C0M1C-D4T4-H1ST0RY-TR4CK1NG-2026"

# MUST match exactly the endpoint URL you enter in the portal
ENDPOINT_URL = "https://ebay-callback-service.onrender.com/callback"

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/callback")
async def callback_get(request: Request):
    """
    Handles eBay's GET challenge request:
    GET /callback?challenge_code=123
    """
    challenge_code = request.query_params.get("challenge_code")

    if challenge_code:
        logging.info(f"Received challenge_code: {challenge_code}")

        # Concatenate in EXACT order:
        # challengeCode + verificationToken + endpoint
        to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL

        # SHA-256 hash
        response_hash = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()

        logging.info(f"Responding with challengeResponse: {response_hash}")

        return {"challengeResponse": response_hash}

    return {"status": "callback GET received"}

@app.post("/callback")
async def callback_post(request: Request):
    """
    Handles actual deletion notifications after validation succeeds.
    """
    payload = await request.json()
    logging.info(f"Received deletion event: {payload}")
    return {"status": "received"}