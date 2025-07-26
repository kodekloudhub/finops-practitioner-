#!/bin/bash

echo "🚀 Starting FinOps City: Match & Solve (Streamlit)"
echo "=================================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "📦 Building the Docker image..."
docker build -t finops-game-streamlit .

echo "🚀 Starting the Streamlit application..."
docker run -d -p 8501:8501 --name finops-game-streamlit-container finops-game-streamlit

echo "⏳ Waiting for the application to start..."
sleep 5

# Check if the application is running
if curl -f http://localhost:8501/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "🌐 Open your browser and navigate to:"
    echo "   http://localhost:8501"
    echo ""
    echo "🎮 Enjoy learning FinOps with the new Streamlit interface!"
    echo ""
    echo "To stop the application, run:"
    echo "   docker stop finops-game-streamlit-container"
    echo "   docker rm finops-game-streamlit-container"
else
    echo "❌ Application failed to start. Check the logs with:"
    echo "   docker logs finops-game-streamlit-container"
    exit 1
fi