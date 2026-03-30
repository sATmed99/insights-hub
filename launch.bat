@echo off
REM Global Startup Analytics Hub - Windows Launcher
REM Automatically opens the app in your default browser

echo ============================================================
echo.
echo     Global Startup Analytics Hub - Launcher
echo.
echo ============================================================
echo.

REM Activate conda environment if it exists
if exist "%CONDA_PREFIX%\envs\insights-hub" (
    call conda activate insights-hub
    echo ✓ Conda environment activated
) else (
    echo ⚠ insights-hub environment not found
    echo   Install with: conda create -n insights-hub python=3.9
)

echo.
echo 🌍 Starting application...
echo 📊 The app will open in your default browser
echo 🔗 View at: http://localhost:8501
echo.
echo ============================================================
echo.

REM Run the launcher
python launch.py

pause
