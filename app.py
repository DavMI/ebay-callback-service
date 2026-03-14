from fastapi import FastAPI, Request
import logging
import uvicorn

app = FastAPI()

# Configure logging for Render (stdout)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.get("/")
async def health_check():
    """Simple health check endpoint for Render."""
    return {"status": "ok"}

@app.post("/callback")
async def callback(request: Request):
    """
    Handles eBay Marketplace Account Deletion notifications.
    Render requires HTTPS automatically, so no extra config needed.
    """
    try:
        payload = await request.json()
    except Exception:
        logging.warning("Received invalid JSON payload")
        return {"error": "Invalid JSON"}

    logging.info(f"Received eBay callback: {payload}")

    # eBay may send a handshake for some topics, but MARKETPLACE_ACCOUNT_DELETION
    # does NOT require echoing a verificationToken.
    if "challengeCode" in payload:
        # Some eBay topics use challengeCode (not this one, but safe to support)
        return {"challengeResponse": payload["challengeCode"]}

    # For deletion events, simply acknowledge receipt
    return {"status": "received"}