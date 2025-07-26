# Kubecost FinOps Detective Game 🕵️‍♂️

An interactive detective game that teaches Kubecost and FinOps principles through a branching scenario simulation. Players act as a "Cost Detective" investigating high Kubernetes costs in a fictional company.

## Overview

This game uses a choose-your-own-adventure format with 5 stages where you:
- Investigate cluster costs using simulated Kubecost data
- Make strategic decisions on optimizations
- Learn FinOps principles through immediate feedback
- Earn points and badges based on your choices

## Features

- **5 Interactive Stages**: Each with unique scenarios and Kubecost insights
- **Point System**: Earn up to 500 points based on your decisions
- **Educational Feedback**: Learn why each choice matters in FinOps
- **Randomized Data**: Cost values vary for replayability
- **Achievement Badges**: Unlock special badges like 🏆 Master Detective
- **Success Metrics**: Reduce costs by 40% to win!

## Installation & Running

### Option 1: Using Python

1. Clone this repository or download the files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser to `http://localhost:8501`

### Option 2: Using Docker

1. Build the Docker image:
   ```bash
   docker build -t kubecost-detective-game .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 kubecost-detective-game
   ```

3. Open your browser to `http://localhost:8501`

### Option 3: Using Docker Compose

Create a `docker-compose.yml` file:
```yaml
version: '3.8'
services:
  game:
    build: .
    ports:
      - "8501:8501"
```

Then run:
```bash
docker-compose up
```

## How to Play

1. **Start**: Click "Begin Investigation" to start your mission
2. **Analyze**: Read the Kubecost reports showing cost and efficiency data
3. **Decide**: Choose from 3-4 options for each scenario
4. **Learn**: Get immediate feedback on your choices
5. **Progress**: Advance through 5 stages of cost optimization
6. **Win**: Achieve 300+ points to successfully reduce costs by 40%!

## Key Concepts Covered

- **Kubecost Features**: Namespace analysis, workload efficiency, cost allocation
- **FinOps Pillars**: Inform (visibility), Optimize (rightsizing), Operate (monitoring)
- **Best Practices**: Tagging, spot instances, reserved instances, autoscaling
- **Cost Attribution**: Team accountability through proper resource labeling

## Game Stages

1. **Cluster Overview**: Identify high-cost namespaces
2. **Namespace Investigation**: Find idle and overprovisioned resources
3. **Workload Optimization**: Implement tagging policies
4. **Cost Optimization**: Choose savings strategies (spot, RIs, scaling)
5. **Monitoring Setup**: Establish ongoing FinOps practices

## Tips for Success

- Always investigate before taking action
- Focus on data-driven decisions
- Consider both immediate and long-term impacts
- Remember the FinOps principle: "Visibility first!"

## Requirements

- Python 3.8+
- Mesop 0.12.0+
