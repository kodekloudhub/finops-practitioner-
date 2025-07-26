# FinOps Practitioner Educational Tools 🎓💰

A comprehensive collection of interactive web applications designed to teach FinOps (Financial Operations) concepts through gamification and hands-on learning experiences.

## 🚀 Overview

This repository contains 6 educational tools that help practitioners understand cloud cost optimization and FinOps fundamentals through interactive games and simulations:

### 1. [FinOps CloudBill Game](./finops-cloudbill-game/) 🎮
Analyze mock AWS bills to identify and fix cloud cost "leaks" using FinOps best practices.

### 2. [FinOps Exam Flipcards](./finops-exam-flipcard/) 📚
Interactive study tool with 20 flipcards covering essential FinOps concepts for exam preparation.

### 3. [Kubecost FinOps Detective Game](./finops-kubecost-game/) 🕵️‍♂️
Choose-your-own-adventure game where you investigate high Kubernetes costs using simulated Kubecost data.

### 4. [FinOps Journey Simulation](./finops-maturity-game/) 📈
Learn to identify FinOps maturity stages (Crawl, Walk, Run) through realistic company scenarios.

### 5. [FinOps City: Match & Solve](./finops-persona/) 🏙️
Match cloud cost management problems to the appropriate FinOps personas in this interactive puzzle game.

### 6. [Azure Cost Optimization Puzzle](./finops-realworld-game/) 🧩
Practice the logical sequence of Azure cost optimization steps through hands-on problem-solving.

## 🛠️ Technology Stack

All applications share similar architectures:
- **Backend:** Python with FastAPI or Streamlit
- **Frontend:** Vanilla HTML/CSS/JavaScript or Streamlit UI
- **Data:** JSON files for scenarios and content
- **Containerization:** Docker support for easy deployment
- **No External Dependencies:** Run completely offline

## 🏃‍♂️ Quick Start

Each application can be run independently using Docker:

```bash
# Navigate to any game directory
cd finops-[game-name]

# Build and run with Docker
docker build -t finops-[game-name] .
docker run -p [PORT]:[PORT] finops-[game-name]
```

Default ports:
- CloudBill Game: 8001
- Exam Flipcards: 8000
- Kubecost Detective: 8501
- Journey Simulation: 8501
- FinOps City: 8501
- Azure Puzzle: 8501

## 📖 Learning Path

### For Beginners:
1. Start with **Exam Flipcards** to understand core concepts
2. Try **Journey Simulation** to learn about maturity stages
3. Play **FinOps City** to understand different personas
4. Practice with **CloudBill Game** for hands-on optimization

### For Practitioners:
1. Jump into **Kubecost Detective** for Kubernetes cost management
2. Master **Azure Puzzle** for systematic optimization approaches
3. Challenge yourself with **CloudBill Game** scenarios

## 🎯 Key Learning Areas

- **FinOps Fundamentals:** Three phases (Inform, Optimize, Operate)
- **Cost Optimization:** Rightsizing, lifecycle policies, reserved instances
- **Kubernetes FinOps:** Namespace analysis, workload efficiency
- **Maturity Assessment:** Crawl, Walk, Run stages
- **Team Collaboration:** Understanding different FinOps personas
- **Systematic Approaches:** Logical sequences for cost optimization

## 🤝 Contributing

Each project is self-contained with its own README. Feel free to:
- Add new scenarios or questions
- Improve UI/UX
- Fix bugs or enhance features
- Add more educational content

## 📄 License

These tools are designed for educational purposes. Use and modify freely for learning FinOps concepts.

---

**Start your FinOps learning journey today! 🚀**
