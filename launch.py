#!/usr/bin/env python
"""
Launcher script for Global Startup Analytics Hub
Automatically opens the app in the default browser
"""
import webbrowser
import subprocess
import time
import sys
import os
from pathlib import Path

def open_browser(url, delay=2):
    """Open the app in default browser after a delay"""
    time.sleep(delay)
    try:
        webbrowser.open(url, new=1)  # new=1 opens in new tab
        print(f"✅ Browser opened: {url}")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print(f"📍 Open manually: {url}")

def main():
    """Main launcher function"""
    # Get the directory of this script
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # App URL (default Streamlit port)
    app_url = "http://localhost:8501"
    
    print("=" * 60)
    print("🌍 Global Startup Analytics Hub - Launcher")
    print("=" * 60)
    print(f"📊 Starting application...")
    print(f"🔗 View at: {app_url}")
    print("-" * 60)
    
    # Start browser opening in background thread
    import threading
    browser_thread = threading.Thread(target=open_browser, args=(app_url,), daemon=True)
    browser_thread.start()
    
    # Run Streamlit app
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "app_main.py"],
            cwd=str(project_dir)
        )
    except KeyboardInterrupt:
        print("\n\n✋ Application stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error running app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
