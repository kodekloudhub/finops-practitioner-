# 🎯 Azure Cost Optimization Puzzle Game

An interactive educational game that teaches FinOps practitioners the logical sequence of Azure cost optimization through hands-on practice. Built with Streamlit for easy deployment and accessibility.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.32.2-red.svg)
![Docker](https://img.shields.io/badge/docker-ready-green.svg)

## 🎮 Game Overview

**Scenario**: You're an Engineering Manager dealing with skyrocketing Azure bills. Your task is to arrange 7 cost optimization steps in the correct logical order.

**Learning Objectives**:
- Understand the systematic approach to cloud cost optimization
- Learn the dependencies between different FinOps activities
- Practice real-world decision-making in cost management

## 🚀 Quick Start

### Option 1: Run with Docker (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd finops-realworld-game

# Build the Docker image
docker build -t finops-puzzle .

# Run the container
docker run -p 8501:8501 finops-puzzle
```

Visit `http://localhost:8501` in your browser to play!

### Option 2: Run Locally

```bash
# Clone the repository
git clone <your-repo-url>
cd finops-realworld-game

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📋 The 7 Steps (Scrambled in Game)

The game challenges you to arrange these steps in the correct order:

1. **Gather Data** - Review Azure bills and usage reports
2. **Identify Cost Drivers** - Analyze data to find high-cost services
3. **Set Budgets and Alerts** - Establish spending limits and notifications
4. **Optimize Resources** - Rightsize, delete unused, switch to cost-effective options
5. **Implement Reservations** - Purchase reserved instances for predictable workloads
6. **Enforce Tagging** - Mandate resource tagging for cost allocation
7. **Monitor and Iterate** - Continuously review and adjust strategies

## 🎯 How to Play

1. **Read the Scenario**: Understand your role as an Engineering Manager handling FinOps
2. **Arrange Steps**: Use the dropdown selectors to put steps in order (1-7)
3. **Submit**: Click submit when you've arranged all 7 steps
4. **Review Feedback**: 
   - ✅ Green checkmarks show correct positions
   - ❌ Red X's indicate incorrect positions with explanations
5. **Learn**: View the correct order and understand why each step follows the previous
6. **Try Again**: Reset to practice until you master the sequence

## 🏗️ Architecture

```
finops-realworld-game/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
├── design.md          # Original design document
└── .gitignore         # Git ignore rules
```

## 🛠️ Technical Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Pure Python with session state management
- **Deployment**: Docker-ready for easy containerization
- **Dependencies**: Minimal (streamlit, pandas)

## 📊 Features

- **Interactive Learning**: Hands-on practice vs passive reading
- **Immediate Feedback**: Know what's wrong and why
- **Visual Indicators**: Emojis and colors for engagement
- **Explanations**: Understand the logic behind the correct order
- **Mobile Responsive**: Works on desktop and mobile devices
- **No Database Required**: All logic handled in-memory

## 🚢 Deployment Options

### Deploy to Streamlit Cloud (Free)

1. Fork this repository
2. Sign up at [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy directly from your fork

### Deploy with Docker

```bash
# Build image
docker build -t finops-puzzle:latest .

# Run with auto-restart
docker run -d \
  --name finops-puzzle \
  --restart unless-stopped \
  -p 8501:8501 \
  finops-puzzle:latest
```





