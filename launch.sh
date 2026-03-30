#!/bin/bash
# Global Startup Analytics Hub - Unix Launcher
# Automatically opens the app in your default browser

echo "============================================================"
echo ""
echo "    Global Startup Analytics Hub - Launcher"
echo ""
echo "============================================================"
echo ""

# Activate conda environment if it exists
if [ -d "$HOME/miniconda3/envs/insights-hub" ] || [ -d "$HOME/anaconda3/envs/insights-hub" ]; then
    source activate insights-hub 2>/dev/null || conda activate insights-hub
    echo "✓ Conda environment activated"
else
    echo "⚠ insights-hub environment not found"
    echo "  Install with: conda create -n insights-hub python=3.9"
fi

echo ""
echo "🌍 Starting application..."
echo "📊 The app will open in your default browser"
echo "🔗 View at: http://localhost:8501"
echo ""
echo "============================================================"
echo ""

# Run the launcher
python launch.py
