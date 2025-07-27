#!/bin/bash

# Cloud Cost Hero - Start Script
echo "🎮 Starting Cloud Cost Hero..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Build and start the application
echo "🐳 Building and starting Cloud Cost Hero with Docker..."
docker build -t cloud-cost-hero .
docker run -p 8501:8501 cloud-cost-hero

echo "✅ Cloud Cost Hero is running!"
echo "🌐 Open your browser to: http://localhost:8501"
echo "🛑 To stop the application, press Ctrl+C" 