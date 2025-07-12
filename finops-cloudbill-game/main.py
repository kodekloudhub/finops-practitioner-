from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import random
import json
import os

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

MOCK_BILLS_PATH = os.path.join(os.path.dirname(__file__), "mock_bills.json")

# Endpoint to serve a random mock AWS bill
def load_mock_bills():
    with open(MOCK_BILLS_PATH, "r") as f:
        return json.load(f)

@app.get("/api/bill")
def get_random_bill():
    bills = load_mock_bills()
    bill = random.choice(bills)
    # Remove answer keys before sending to user
    sanitized_items = [
        {k: v for k, v in item.items() if k not in ("category_answer", "optimization_answer")}
        for item in bill["items"]
    ]
    return {"bill_id": bill["bill_id"], "items": sanitized_items}

# Endpoint to validate user categorizations
@app.post("/api/validate-categories")
async def validate_categories(request: Request):
    data = await request.json()
    bill_id = data["bill_id"]
    user_categories = data["categories"]  # {item_id: category}
    bills = load_mock_bills()
    bill = next((b for b in bills if b["bill_id"] == bill_id), None)
    if not bill:
        return JSONResponse(status_code=404, content={"error": "Bill not found"})
    results = {}
    for item in bill["items"]:
        correct = item["category_answer"]
        user = user_categories.get(item["id"])
        results[item["id"]] = {"user": user, "correct": correct, "is_correct": user == correct}
    return {"results": results}

# Endpoint to validate user optimizations and show savings
@app.post("/api/validate-optimizations")
async def validate_optimizations(request: Request):
    data = await request.json()
    bill_id = data["bill_id"]
    user_opts = data["optimizations"]  # {item_id: optimization}
    bills = load_mock_bills()
    bill = next((b for b in bills if b["bill_id"] == bill_id), None)
    if not bill:
        return JSONResponse(status_code=404, content={"error": "Bill not found"})
    before_total = sum(item["cost"] for item in bill["items"])
    after_items = []
    savings = 0
    for item in bill["items"]:
        correct_opt = item["optimization_answer"]
        user_opt = user_opts.get(item["id"])
        cost = item["cost"]
        if user_opt == correct_opt and correct_opt != "no action":
            # Assume 80% savings for correct optimization (for demo)
            saved = round(cost * 0.8, 2)
            after_cost = round(cost - saved, 2)
            savings += saved
        else:
            after_cost = cost
        after_items.append({**item, "after_cost": after_cost, "user_opt": user_opt, "correct_opt": correct_opt})
    after_total = sum(i["after_cost"] for i in after_items)
    return {
        "before_total": before_total,
        "after_total": after_total,
        "savings": round(savings, 2),
        "details": after_items
    }

# Optional: Endpoint for tips/definitions
TIPS = [
    "Rightsizing means matching resource size to actual usage.",
    "Lifecycle policies can automatically delete old backups.",
    "Idle resources are a common source of cloud waste.",
    "Overprovisioned databases can be downsized for savings.",
    "Elastic IPs incur charges when not attached to running instances."
]

@app.get("/api/tips")
def get_tip():
    return {"tip": random.choice(TIPS)}

# Serve the main HTML file (if frontend is placed here)
@app.get("/")
def root():
    index_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "FinOps CloudBill Game API"} 