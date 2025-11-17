#!/bin/bash
# Tennis Pose Estimation - Mac/Linux Launcher
# Run this file to start the application

echo ""
echo "========================================="
echo "Tennis Pose Estimation - Starting..."
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed"
    echo ""
    echo "Please install Python 3 from: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

# Run the launcher
python3 app_launcher.py
