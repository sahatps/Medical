@echo off
REM Tennis Pose Estimation - Windows Launcher
REM Double-click this file to start the application

echo.
echo =========================================
echo Tennis Pose Estimation - Starting...
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Run the launcher
python app_launcher.py

pause
