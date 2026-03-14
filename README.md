📘 README — eBay Callback Service

Overview

The eBay Callback Service is a lightweight FastAPI-based microservice designed to receive Account Deletion and Consent Revocation notifications from eBay’s Developer Program. eBay requires a publicly accessible HTTPS endpoint for these callbacks before enabling Production API access. This service provides that endpoint and is optimized for deployment on Render.com (Free Tier).

This service is separate from the main FMV (Fair Market Value) application and is deployed independently.

✨ Features

/ping endpoint for health checks

/callback endpoint for eBay Account Deletion / Consent Revocation events

JSON payload logging

FastAPI + Uvicorn + Gunicorn stack

Ready for Render.com deployment

Minimal, clean architecture

📁 Project Structure

ebay-callback-service/
│
├── app.py
├── requirements.txt
├── render.yaml
└── README.md

🚀 Running Locally

1. Install dependencies

pip install -r requirements.txt

2. Start the server

uvicorn app:app --reload

3. Test the health endpoint

Open your browser or use curl:

http://localhost:8000/ping

Expected response:

{"status": "ok"}

🌐 Deployment (Render.com)

This service is designed for easy deployment on Render’s free tier.

Steps

Push this repository to GitHub

Log into Render.com

Click New Web Service

Select this repo

Render will auto-detect Python

Deploy

Render will use the render.yaml file to configure:

Python environment

Install dependencies

Start command using Gunicorn + Uvicorn worker

After deployment

Test the live health endpoint:

https://<your-service>.onrender.com/ping

🔔 eBay Callback Integration

Required by eBay

eBay requires a public HTTPS endpoint for:

Account Deletion

Consent Revocation

This service exposes:

POST /callback

Example payload logging

When eBay sends a callback, the service logs the JSON payload:

@app.post("/callback")
async def callback(request: Request):
    payload = await request.json()
    logging.info(f"Received eBay callback: {payload}")
    return {"message": "Callback received"}

Next steps (optional)

You may extend the callback logic to:

Remove user tokens

Delete stored user data

Trigger cleanup workflows

🛠 Technologies Used

FastAPI — modern Python web framework

Uvicorn — ASGI server

Gunicorn — production process manager

Render.com — hosting platform

📄 License

This project is provided as-is for integration with eBay’s Developer Program. No license restrictions unless you choose to add one.

If you want, I can also generate:

A .gitignore for Python

A more advanced callback handler

Logging to a file or database

A version of this README with badges, diagrams, or API docs

Just tell me what direction you want to take next.