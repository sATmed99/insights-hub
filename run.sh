#!/bin/bash
# Quick Start Script for EuroStartup Radar

echo "🚀 EuroStartup Radar - Quick Setup"
echo "=================================="
echo ""

# Check Python version
echo "✓ Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python3 is not installed. Please install Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "  Found Python $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "✓ Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Virtual environment created"
else
    echo "  Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate
echo "  Virtual environment activated"

# Install dependencies
echo ""
echo "✓ Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
echo "  Dependencies installed"

# Run the app
echo ""
echo "✓ Starting EuroStartup Radar..."
echo ""
echo "🌐 App will be available at http://localhost:8501"
echo "📊 Press Ctrl+C to stop the application"
echo ""

streamlit run main.py
