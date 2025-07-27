# Cloud Cost Hero 🎮

A single-file Streamlit mini-game to teach **Compute Savings Plans** through interactive gameplay.

## 🎯 Purpose

Learn how to minimize your 30-day AWS bill by choosing the right hourly commitment for a Compute Savings Plan. The game simulates real-world usage patterns and lets you experiment with different commitment levels to see their impact on costs.

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Build and run with Docker:**
   ```bash
   # Build the Docker image
   docker build -t cloud-cost-hero .
   
   # Run the container
   docker run -p 8501:8501 cloud-cost-hero
   ```

2. **Or use the start script:**
   ```bash
   ./start.sh
   ```

3. **Open your browser** to `http://localhost:8501`

### Option 2: Local Python

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game:**
   ```bash
   streamlit run cloud_cost_hero.py
   ```

3. **Open your browser** to the URL shown in the terminal (usually `http://localhost:8501`)

## 🎮 How to Play

1. **Watch the simulation** - See your startup's usage patterns in real-time
2. **Set your commitment** - Choose your hourly Compute Savings Plan commitment ($0.0 - $5.0)
3. **Lock in your plan** - Once you're confident, lock your commitment
4. **See the results** - Watch the simulation complete and see your final bill
5. **Play again** - Try different strategies with new random personas

## 🏢 Startup Personas

The game features three different startup types, each with unique usage patterns:

- **Steady SaaS**: Consistent usage with occasional small spikes
- **Spiky Batch**: Low base usage with frequent large spikes
- **Weekend Peak**: Moderate usage with weekend spikes

## 💰 Cost Calculation

- **On-Demand Rate**: $0.05 per CPU-hour
- **Savings Plan Cost**: Your commitment × 720 hours (30 days)
- **Overage Cost**: Any usage above your commitment × $0.05
- **Total Cost**: Savings Plan Cost + Overage Cost
- **Savings %**: (On-Demand Cost - Total Cost) / On-Demand Cost × 100

## 🎉 Success Criteria

- **≥30% savings**: 🎈 Balloons celebration!
- **0-30% savings**: Good job, room for improvement
- **<0% savings**: You paid more than On-Demand - try a lower commitment

## 📊 Features

- **Real-time simulation** with live usage charts
- **Interactive commitment slider** with instant cost projections
- **Detailed cost breakdown** showing savings plan vs overage costs
- **Usage statistics** including peak, average, and total usage
- **Random personas** for replayability
- **Responsive design** that works on desktop and mobile

## 🛠️ Technical Details

- **Single file**: All game logic in `cloud_cost_hero.py`
- **Zero external dependencies**: Only requires `streamlit`
- **Session state management**: Persistent game state across interactions
- **Performance optimized**: Shows last 50 data points for responsive charts
- **Docker ready**: Containerized with health checks and proper networking
- **Production ready**: Configured for deployment with environment variables

## 🎯 Learning Objectives

- Understand how Compute Savings Plans work
- Learn to balance commitment levels with usage patterns
- See the impact of usage spikes on cost optimization
- Practice cost optimization strategies in a risk-free environment

## 🐳 Docker Management

### Useful Docker Commands

```bash
# Build the image
docker build -t cloud-cost-hero .

# Run the container
docker run -p 8501:8501 cloud-cost-hero

# Run in background
docker run -d -p 8501:8501 --name cloud-cost-hero cloud-cost-hero

# View logs
docker logs -f cloud-cost-hero

# Stop the container
docker stop cloud-cost-hero

# Remove the container
docker rm cloud-cost-hero

# Access container shell
docker exec -it cloud-cost-hero /bin/bash

# List running containers
docker ps

# List all containers
docker ps -a
```

### Production Deployment

For production deployment, consider:

- Using a reverse proxy (nginx, traefik)
- Setting up SSL/TLS certificates
- Configuring proper logging
- Using Docker secrets for sensitive data
- Setting up monitoring and alerting

---

Happy cost optimizing! 🚀 