# FinOps CloudBill Game (AWS Edition) - Streamlit Version

## 🎯 Overview
An interactive web-based game where you analyze a mock AWS bill, identify cloud cost "leaks," and apply FinOps optimization solutions. Learn FinOps best practices in a fun, fast, and educational way! Now built with Streamlit for a modern, responsive interface.

## 🛠️ Tech Stack
- **Framework:** Streamlit (Python web app framework)
- **Data:** JSON-based mock AWS bills
- **Containerization:** Docker

## 🚀 Features
- Simulates an AWS bill with realistic line items (EC2, S3, RDS, Lambda, etc.)
- Categorize each line item by cost type (compute, storage, idle, overprovisioned)
- Identify and fix wasteful items with the best optimization (rightsizing, lifecycle policy, etc.)
- Instant feedback, scoring, and cost savings summary
- Fun FinOps tips and definitions
- Modern, responsive UI with Streamlit components

## 🏗️ Folder Structure
```
finops-cloudbill-game/
  ├── main.py              # Streamlit application
  ├── mock_bills.json      # Mock AWS bill data
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
   docker run -p 8501:8501 finops-cloudbill-game
   ```
3. **Open the game:**
   Visit [http://localhost:8501](http://localhost:8501) in your browser.

## 🧑‍💻 Manual Setup (Local Python)
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the Streamlit app:**
   ```sh
   streamlit run main.py
   ```
3. **Open the game:**
   Visit [http://localhost:8501](http://localhost:8501)

## 🔧 Troubleshooting
If you encounter numpy compatibility issues, try:
```bash
pip uninstall streamlit numpy pandas -y
pip install -r requirements.txt
```

## 🎮 How to Play
1. **View the AWS Bill:**
   - The game shows a table of AWS resources, descriptions, and costs.
2. **Categorize Each Line Item:**
   - Select the correct cost category for each item (idle, underprovisioned, overprovisioned).
   - Submit your answers and get instant feedback.
3. **Optimize Wasteful Items:**
   - For each item, choose the best optimization (rightsizing, lifecycle policy, release, or no action).
   - Submit to see your cost savings and the correct answers.
4. **Review Results:**
   - See before/after costs, total savings, and a FinOps tip.
   - Click "Play Again" to try a new bill!

## 🔑 Key Improvements with Streamlit
- **Simplified Architecture:** Single Python file replaces FastAPI + HTML/CSS/JavaScript
- **Better UX:** Native Streamlit widgets provide responsive, modern interface
- **Easier Development:** No need for API endpoints or frontend/backend separation
- **Session Management:** Built-in state management for game progression
- **Mobile Friendly:** Responsive design that works on all devices

## 🎯 Game Categories
- **Idle:** Resources that are running but not being used
- **Underprovisioned:** Resources that need more capacity
- **Overprovisioned:** Resources with more capacity than needed

## 🛠️ Optimization Options
- **Rightsizing:** Adjust resource size to match actual usage
- **Lifecycle Policy:** Automatically manage data lifecycle
- **Release:** Delete unused resources
- **No Action:** Resource is already optimized

## 🔑 Notes
- All data is mock/simulated for educational purposes.
- The game is modular and easy to expand with more bills, categories, or optimizations.
- Streamlit provides hot-reloading for development - changes are reflected immediately.

---
**Enjoy learning FinOps the fun way with Streamlit!** 🚀 