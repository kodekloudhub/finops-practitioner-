# FinOps CloudBill Game (AWS Edition)

## 🎯 Overview
An interactive web-based game where you analyze a mock AWS bill, identify cloud cost “leaks,” and apply FinOps optimization solutions. Learn FinOps best practices in a fun, fast, and educational way!

## 🛠️ Tech Stack
- **Backend:** Python with FastAPI (REST APIs)
- **Frontend:** HTML, CSS, JavaScript (no frameworks)
- **Containerization:** Docker

## 🚀 Features
- Simulates an AWS bill with realistic line items (EC2, S3, RDS, Lambda, etc.)
- Categorize each line item by cost type (compute, storage, idle, overprovisioned)
- Identify and fix wasteful items with the best optimization (rightsizing, lifecycle policy, etc.)
- Instant feedback, scoring, and cost savings summary
- Fun FinOps tips and definitions

## 🏗️ Folder Structure
```
finops-cloudbill-game/
  ├── main.py              # FastAPI backend
  ├── mock_bills.json      # Mock AWS bill data
  ├── static/
  │   ├── index.html       # Game UI
  │   ├── styles.css       # Game styles
  │   └── app.js           # Game logic
  ├── Dockerfile           # Docker setup
  ├── requirements.txt     # Python dependencies
  └── README.md            # This file
```

## ⚡ Quick Start (Docker)
1. **Build the Docker image:**
   ```sh
   docker build -t finops-cloudbill-game .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8001:8001 finops-cloudbill-game
   ```
3. **Open the game:**
   Visit [http://localhost:8000](http://localhost:8000) in your browser.

## 🧑‍💻 Manual Setup (Local Python)
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the backend:**
   ```sh
   uvicorn main:app --reload
   ```
3. **Open the game:**
   Visit [http://localhost:8000](http://localhost:8000)

## 🎮 How to Play
1. **View the AWS Bill:**
   - The game shows a table of AWS resources, descriptions, and costs.
2. **Categorize Each Line Item:**
   - Select the correct cost category for each item (compute, storage, idle, overprovisioned).
   - Submit your answers and get instant feedback.
3. **Optimize Wasteful Items:**
   - For each item, choose the best optimization (rightsizing, lifecycle policy, release, or no action).
   - Submit to see your cost savings and the correct answers.
4. **Review Results:**
   - See before/after costs, total savings, and a FinOps tip.
   - Click "Play Again" to try a new bill!

## 🔑 Notes
- All data is mock/simulated for educational purposes.
- The game is modular and easy to expand with more bills, categories, or optimizations.

---
**Enjoy learning FinOps the fun way!** 