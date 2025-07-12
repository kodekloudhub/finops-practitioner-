# FinOps Practitioner Educational Tools 🎓💰

Welcome to the FinOps Practitioner repository! This collection features interactive web applications designed to teach FinOps (Financial Operations) concepts through gamification and hands-on learning experiences.

## 🚀 Overview

This repository contains two educational tools that help practitioners understand cloud cost optimization and FinOps fundamentals:

### 1. [FinOps CloudBill Game](./finops-cloudbill-game/README.md) 🎮
An interactive game where you analyze mock AWS bills to identify and fix cloud cost "leaks" using FinOps best practices.

**Key Features:**
- Analyze realistic AWS service costs (EC2, S3, RDS, Lambda, etc.)
- Categorize resources as idle, overprovisioned, or underprovisioned
- Apply optimizations like rightsizing, lifecycle policies, and resource releases
- Get instant feedback with cost savings calculations
- Learn through practical, real-world scenarios

### 2. [FinOps Exam Flipcards](./finops-exam-flipcard/README.md) 📚
An interactive study tool with 20 flipcards covering essential FinOps concepts for exam preparation.

**Key Topics:**
- The three FinOps phases (Inform, Optimize, Operate)
- Iron Triangle trade-offs (Quality, Speed, Cost)
- FinOps terminology (MDCO, amortization, showback vs chargeback)
- Commitment-based discounts and optimization strategies
- Persona motivations and collaboration principles

## 🛠️ Technology Stack

Both applications share a similar architecture:
- **Backend:** Python with FastAPI for REST APIs
- **Frontend:** Vanilla HTML, CSS, and JavaScript (no frameworks)
- **Data Storage:** JSON files for game scenarios and flipcard content
- **Containerization:** Docker support for easy deployment
- **No External Dependencies:** Runs completely offline without cloud services

## 🏃‍♂️ Quick Start

Each application can be run independently. Choose your learning path:

### Option 1: Run with Docker (Recommended)

```bash
# For CloudBill Game
cd finops-cloudbill-game
docker build -t finops-cloudbill-game .
docker run -p 8001:8001 finops-cloudbill-game

# For Exam Flipcards
cd finops-exam-flipcard
docker build -t finops-flipcards .
docker run -p 8000:8000 finops-flipcards
```

### Option 2: Run with Python

```bash
# Install dependencies
pip install fastapi uvicorn

# For CloudBill Game
cd finops-cloudbill-game
uvicorn main:app --reload --port 8001

# For Exam Flipcards
cd finops-exam-flipcard
uvicorn main:app --reload --port 8000
```

## 📖 Learning Path

### For Beginners:
1. Start with the **Exam Flipcards** to understand core FinOps concepts
2. Move to the **CloudBill Game** to apply your knowledge practically

### For Practitioners:
1. Jump into the **CloudBill Game** to test your optimization skills
2. Use the **Exam Flipcards** for quick concept reviews

