from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Basic logger
logging.basicConfig(level=logging.INFO)

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.post("/callback")
async def callback(request: Request):
    payload = await request.json()
    logging.info(f"Received eBay callback: {payload}")

    # TODO: Add logic to delete user data/tokens here

    return {"message": "Callback received"}