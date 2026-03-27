"""
Insights Hub - Business Analytics Platform
Main entry point for running the application with: streamlit run main.py
"""
import sys
from pathlib import Path

# Add the project root to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import and run the app
from app_main import *
