 #!/bin/bash

echo "🚀 Starting FinOps City: Match & Solve"
echo "======================================"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "📦 Building the Docker image..."
docker build -t finops-game .

echo "🚀 Starting the application..."
docker run -d -p 8002:8002 --name finops-game-container finops-game

echo "⏳ Waiting for the application to start..."
sleep 3

# Check if the application is running
if curl -f http://localhost:8002/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "🌐 Open your browser and navigate to:"
    echo "   http://localhost:8002"
    echo ""
    echo "🎮 Enjoy learning FinOps!"
    echo ""
    echo "To stop the application, run:"
    echo "   docker stop finops-game-container"
    echo "   docker rm finops-game-container"
else
    echo "❌ Application failed to start. Check the logs with:"
    echo "   docker logs finops-game-container"
    exit 1
fi