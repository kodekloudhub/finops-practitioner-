# FinOps City: Match & Solve (Streamlit Edition)

An interactive web-based educational game designed to teach FinOps (Financial Operations) concepts through problem-solving and persona matching, built with Streamlit for a modern, responsive user experience.

## 🎮 Game Overview

"FinOps City: Match & Solve" is an educational game that helps players learn about FinOps roles and responsibilities by matching real-world cloud cost management problems to the appropriate FinOps personas. Players engage in a gamified experience with instant feedback, mini-missions, and scoring.

## 🎯 Learning Objectives

- Understand FinOps personas and their responsibilities
- Learn which persona is best suited for different cloud cost challenges
- Gain knowledge of practical cost optimization strategies
- Understand the collaborative nature of FinOps

## 🏗️ Technical Stack

- **Frontend & Backend**: Streamlit (Python)
- **Styling**: Custom CSS with modern gradients and animations
- **Containerization**: Docker
- **Port**: 8501 (Streamlit default)

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
   docker build -t finops-game-streamlit .
   docker run -p 8501:8501 finops-game-streamlit
   ```

3. **Access the game**
   Open your browser and navigate to: `http://localhost:8501`

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
chmod +x start.sh
./start.sh
```

### Option 2: Manual Docker commands
```bash
cd finops-persona
docker build -t finops-game-streamlit .
docker run -p 8501:8501 finops-game-streamlit
```

### Option 3: Run in background
```bash
cd finops-persona
docker build -t finops-game-streamlit .
docker run -d -p 8501:8501 --name finops-game-streamlit-container finops-game-streamlit
```

### Option 4: Run locally without Docker
```bash
cd finops-persona
pip install -r requirements.txt
streamlit run streamlit_app.py
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

- **Cloud Engineer (Core)**: Optimizes cloud resources and infrastructure
- **Finance Analyst (Allied)**: Handles budgeting, forecasting, and financial planning
- **Product Manager (Allied)**: Balances business needs with cost considerations
- **Procurement Specialist (Allied)**: Manages vendor relationships and policies
- **Executive Leader (Allied)**: Ensures accountability and strategic alignment

## 🏆 Scoring System

- **Correct Match**: 10 points
- **Mini-Mission Success**: 5 points
- **Maximum Score**: 75 points (5 problems × 15 points each)

## 🛠️ Development

### Project Structure

```
finops-persona/
├── streamlit_app.py        # Main Streamlit application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── start.sh              # Easy startup script
├── README.md             # This file
└── one-pager.txt         # Game design document
```

### Key Features

- **Modern UI**: Beautiful gradients, animations, and responsive design
- **Interactive Cards**: Click-to-select interface for problems and personas
- **Real-time Feedback**: Instant visual feedback with color-coded results
- **Progress Tracking**: Visual progress bar and score display
- **Mini-Missions**: Engaging scenarios that test practical knowledge
- **Comprehensive Results**: Detailed match summary and learning outcomes

### Local Development

If you want to run the application without Docker:

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the application**
   Open your browser and navigate to: `http://localhost:8501`

## 🎨 UI Improvements

### Visual Enhancements

- **Gradient Headers**: Beautiful gradient backgrounds for main sections
- **Card-based Design**: Modern card layout with hover effects
- **Color-coded Feedback**: Green for success, red for errors
- **Progress Visualization**: Animated progress bar
- **Responsive Layout**: Works seamlessly on desktop and mobile

### User Experience

- **Intuitive Navigation**: Clear screen transitions
- **Instant Feedback**: Immediate response to user actions
- **Visual Hierarchy**: Clear distinction between different elements
- **Accessibility**: High contrast and readable fonts
- **Smooth Animations**: Subtle transitions for better engagement

## 🔧 Configuration

### Environment Variables

The application can be configured using environment variables:

- `PYTHONUNBUFFERED=1` - Ensures Python output is not buffered (useful for Docker)

### Port Configuration

The default port is 8501 (Streamlit default). To change it:

1. Update the `EXPOSE` line in `Dockerfile`
2. Update the port in the `docker run` command
3. Update the port in `start.sh`

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Check what's using port 8501
   lsof -i :8501
   
   # Kill the process or change the port
   ```

2. **Docker build fails**
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t finops-game-streamlit .
   ```

3. **Streamlit app doesn't load**
   - Check browser console for errors
   - Verify the app is running: `curl http://localhost:8501/`
   - Check Docker logs: `docker logs finops-game-streamlit-container`

### Logs

View application logs:
```bash
docker logs finops-game-streamlit-container
```

## 📚 Educational Value

This game teaches:

- **FinOps Fundamentals**: Understanding of cloud financial operations
- **Role Clarity**: Clear distinction between different FinOps personas
- **Problem-Solving**: How to approach different cloud cost challenges
- **Collaboration**: The importance of teamwork in FinOps
- **Best Practices**: Practical strategies for cost optimization

## 🆕 What's New in Streamlit Edition

### Enhanced Features

- **Modern UI**: Complete redesign with gradients and animations
- **Better UX**: Improved navigation and feedback systems
- **Responsive Design**: Works perfectly on all screen sizes
- **Real-time Updates**: Instant feedback and progress tracking
- **Simplified Deployment**: Single Streamlit app instead of separate frontend/backend

### Technical Improvements

- **Single Codebase**: Everything in one Python file
- **No API Calls**: Direct state management within Streamlit
- **Better Performance**: Faster loading and interactions
- **Easier Maintenance**: Simplified architecture
- **Docker Optimization**: Smaller, more efficient container

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
4. Ensure port 8501 is available

---

**Happy Learning! 🎓**