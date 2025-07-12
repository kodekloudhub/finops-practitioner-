from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the main HTML file
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Serve persona-responsibility pairs
@app.get("/api/pairs")
def get_pairs():
    pairs = [
        {"persona": "Cloud Engineer (Core)", "responsibility": "Optimizes resources"},
        {"persona": "Finance Analyst (Allied)", "responsibility": "Handles budgeting"},
        {"persona": "Product Manager (Allied)", "responsibility": "Balances business needs"},
        {"persona": "Procurement Specialist (Allied)", "responsibility": "Manages vendor policies"},
        {"persona": "Executive Leader (Allied)", "responsibility": "Ensures accountability"}
    ]
    return JSONResponse(content=pairs)

# Check a match
@app.post("/api/check")
async def check_match(request: Request):
    body = await request.json()
    persona = body.get("persona")
    responsibility = body.get("responsibility")
    
    pairs = [
        {"persona": "Cloud Engineer (Core)", "responsibility": "Optimizes resources"},
        {"persona": "Finance Analyst (Allied)", "responsibility": "Handles budgeting"},
        {"persona": "Product Manager (Allied)", "responsibility": "Balances business needs"},
        {"persona": "Procurement Specialist (Allied)", "responsibility": "Manages vendor policies"},
        {"persona": "Executive Leader (Allied)", "responsibility": "Ensures accountability"}
    ]
    
    correct = next((p for p in pairs if p["persona"] == persona), None)
    if correct and correct["responsibility"] == responsibility:
        return {"result": "correct"}
    else:
        return {"result": "incorrect", "correct_answer": correct["responsibility"] if correct else None}