 # FinOps City: Match & Solve

An interactive web-based educational game designed to teach FinOps (Financial Operations) concepts through problem-solving and persona matching.

## 🎮 Game Overview

"FinOps City: Match & Solve" is an educational game that helps players learn about FinOps roles and responsibilities by matching real-world cloud cost management problems to the appropriate FinOps personas. Players engage in a gamified experience with instant feedback, mini-missions, and scoring.

## 🎯 Learning Objectives

- Understand FinOps personas and their responsibilities
- Learn which persona is best suited for different cloud cost challenges
- Gain knowledge of practical cost optimization strategies
- Understand the collaborative nature of FinOps

## 🏗️ Technical Stack

- **Backend**: Python with FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker
- **Port**: 8002

## 🚀 Quick Start

### Prerequisites

- Docker

### Running the Game

1. **Clone or navigate to the project directory**
   ```bash
   cd finops-persona
   ```

2. **Build and run the application**
   ```bash
   docker build -t finops-game .
   docker run -p 8003:8003 finops-game
   ```

3. **Access the game**
   Open your browser and navigate to: `http://localhost:8002`

4. **Stop the application**
   Press `Ctrl+C` in the terminal or run:
   ```bash
   docker ps
   docker stop <container_id>
   ```

## 🚀 Quick Start Options

### Option 1: Using the startup script (Recommended)
```bash
cd finops-persona
./start.sh
```

### Option 2: Manual Docker commands
```bash
cd finops-persona
docker build -t finops-game .
docker run -p 8002:8002 finops-game
```

### Option 3: Run in background
```bash
cd finops-persona
docker build -t finops-game .
docker run -d -p 8002:8002 --name finops-game finops-game
```

## 🎮 How to Play

### Game Flow

1. **Start Screen**: Read the introduction and game rules
2. **Matching Phase**: Match 5 cloud cost problems to the correct FinOps personas
3. **Feedback**: Receive instant feedback with explanations
4. **Mini-Missions**: Complete short scenarios for bonus points
5. **Results**: View your final score and learning outcomes

### Problem Statements

1. **Unexpected Cost Spike**: Cloud bill jumped by 50% due to unoptimized resources
2. **Budget Forecasting Issue**: Need to predict next quarter's cloud spending
3. **Lack of Cost Visibility**: Teams unaware of cloud usage costs
4. **Resource Scaling Dilemma**: Scale resources for a product launch while controlling costs
5. **Compliance Gap**: Risk of violating cloud spending policies

### FinOps Personas

- **Cloud Engineer** (Core): Optimizes cloud resources and infrastructure
- **Finance Analyst** (Allied): Handles budgeting, forecasting, and financial planning
- **Product Manager** (Allied): Balances business needs with cost considerations
- **Procurement Specialist** (Allied): Manages vendor relationships and policies
- **Executive Leader** (Allied): Ensures accountability and strategic alignment

## 🏆 Scoring System

- **Correct Match**: 10 points
- **Mini-Mission Success**: 5 points
- **Maximum Score**: 75 points (5 problems × 15 points each)

## 🛠️ Development

### Project Structure

```
finops-persona/
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── static/
│   ├── index.html          # Main game interface
│   ├── styles.css          # Game styling
│   └── script.js           # Game logic
├── Dockerfile              # Container configuration
├── start.sh               # Easy startup script
├── README.md              # This file
└── one-pager.txt          # Game design document
```

### API Endpoints

- `GET /` - Health check
- `GET /api/problems` - Get all problem statements
- `GET /api/personas` - Get all FinOps personas
- `POST /api/match` - Validate problem-persona matches
- `GET /api/mini-mission/{problem_id}` - Get mini-mission for a problem
- `POST /api/mini-mission/{problem_id}` - Submit mini-mission answer
- `GET /api/game-summary` - Get game summary and learning outcomes

### Local Development

If you want to run the application without Docker:

1. **Install Python dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server**
   ```bash
   python main.py
   ```

3. **Serve static files**
   You can use any static file server or open `static/index.html` directly in your browser.

## 🎨 Features

- **Responsive Design**: Works on desktop and mobile devices
- **Interactive UI**: Drag-and-drop style matching interface
- **Instant Feedback**: Color-coded feedback with explanations
- **Educational Content**: Detailed explanations of FinOps concepts
- **Progress Tracking**: Real-time score and progress updates
- **Mini-Missions**: Additional learning scenarios for each correct match

## 🔧 Configuration

### Environment Variables

The application can be configured using environment variables:

- `PYTHONUNBUFFERED=1` - Ensures Python output is not buffered (useful for Docker)

### Port Configuration

The default port is 8002. To change it:

1. Update the `EXPOSE` line in `Dockerfile`
2. Update the port in the `docker run` command
3. Update the `API_BASE` constant in `static/script.js`

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Check what's using port 8002
   lsof -i :8002
   
   # Kill the process or change the port in docker-compose.yml
   ```

2. **Docker build fails**
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t finops-game .
   ```

3. **Game doesn't load**
   - Check browser console for JavaScript errors
   - Verify the API is running: `curl http://localhost:8002/`
   - Ensure CORS is properly configured

### Logs

View application logs:
```bash
docker logs finops-game-container
```

## 📚 Educational Value

This game teaches:

- **FinOps Fundamentals**: Understanding of cloud financial operations
- **Role Clarity**: Clear distinction between different FinOps personas
- **Problem-Solving**: How to approach different cloud cost challenges
- **Collaboration**: The importance of teamwork in FinOps
- **Best Practices**: Practical strategies for cost optimization

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is designed for educational purposes. Feel free to use and modify for learning FinOps concepts.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the browser console for errors
3. Verify Docker is properly installed
4. Ensure port 8002 is available

---

**Happy Learning! 🎓**