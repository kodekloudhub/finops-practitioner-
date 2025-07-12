from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

# Serve static files (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint to get flip card data
@app.get("/api/flipcards")
def get_flipcards():
    with open("flipcards.json", "r") as f:
        data = json.load(f)
    return JSONResponse(content=data)

# Serve the main HTML file
@app.get("/")
def root():
    return FileResponse("static/index.html") 