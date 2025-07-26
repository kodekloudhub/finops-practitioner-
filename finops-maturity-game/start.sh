#!/bin/bash

# FinOps Journey Simulation Game Startup Script

echo "🚀 Starting FinOps Journey Simulation Game..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Start the Streamlit application
echo "🌐 Starting Streamlit application..."
echo "📱 The application will be available at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

streamlit run streamlit_app.py 