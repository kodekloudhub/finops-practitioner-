# FinOps Journey Simulation Game

An interactive Streamlit application that helps users learn about FinOps maturity stages through realistic company scenarios.

## Overview

This game presents users with fictional company scenarios and asks them to:
1. Identify the FinOps maturity stage (Crawl, Walk, or Run)
2. Select the key challenges and opportunities present in each scenario

The application provides immediate feedback and educational insights to help users understand FinOps maturity concepts.

## Features

- **Three Distinct Scenarios**: Each representing different FinOps maturity stages
  - **Crawl Stage**: Basic cloud usage without governance
  - **Walk Stage**: Some governance and cost allocation with gaps
  - **Run Stage**: Mature practices with high automation and team involvement

- **Interactive Assessment**: 
  - Radio button selection for maturity stage
  - Multi-select for identifying challenges
  - Immediate feedback with explanations

- **Educational Feedback**: 
  - Detailed explanations of correct answers
  - Identification of missed or incorrect selections
  - Guidance on what to look for in each maturity stage

- **Navigation**: Easy navigation between scenarios with progress tracking

## Installation and Setup

### Option 1: Direct Python Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the App**: Open your browser and navigate to `http://localhost:8501`

### Option 2: Using Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t finops-game .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 8501:8501 finops-game
   ```

3. **Access the App**: Open your browser and navigate to `http://localhost:8501`

### Option 3: Using the Startup Script

1. **Make the script executable** (if not already):
   ```bash
   chmod +x start.sh
   ```

2. **Run the startup script**:
   ```bash
   ./start.sh
   ```

## How to Play

1. **Read the Scenario**: Each scenario describes a fictional company's cloud and FinOps practices
2. **Analyze the Maturity**: Select which FinOps maturity stage the company appears to be in
3. **Identify Challenges**: Choose all the relevant challenges and opportunities present
4. **Submit Analysis**: Click "Analyze Scenario" to receive feedback
5. **Learn from Feedback**: Review the detailed feedback to understand the correct answers
6. **Navigate**: Use the navigation buttons to move between scenarios

## Learning Objectives

- Understand the characteristics of different FinOps maturity stages
- Identify common FinOps challenges and opportunities
- Learn to recognize patterns in organizational FinOps practices
- Develop skills in FinOps assessment and analysis

## Technical Details

- **Framework**: Streamlit
- **Language**: Python
- **State Management**: Streamlit session state
- **UI Components**: Radio buttons, multi-select, buttons, and markdown

## Scenarios Included

1. **Acme Corp's Cloud Chaos** (Crawl Stage)
   - No governance, poor cost visibility, manual processes

2. **TechStart Inc's Growing Pains** (Walk Stage)
   - Basic governance, inconsistent tagging, slow automation adoption

3. **CloudScale Enterprise's FinOps Excellence** (Run Stage)
   - Mature practices, high automation, strong team collaboration

## Contributing

Feel free to add more scenarios or enhance the feedback mechanisms to make the learning experience even better! 