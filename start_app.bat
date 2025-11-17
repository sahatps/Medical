@echo off
REM Tennis Pose Estimation - Windows One-Click Launcher
REM Double-click this file - it will install everything and start automatically!

echo.
echo ============================================================
echo    Tennis Pose Estimation - One-Click Launcher
echo ============================================================
echo.
echo This will:
echo   1. Check Python installation
echo   2. Install required packages (if needed)
echo   3. Start the backend server
echo   4. Open your browser automatically
echo.
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check if requirements file exists
if not exist requirements-local.txt (
    echo [WARNING] requirements-local.txt not found!
    echo Creating basic requirements file...
    echo flask>requirements-local.txt
    echo flask-cors>>requirements-local.txt
    echo opencv-python-headless>>requirements-local.txt
    echo torch>>requirements-local.txt
    echo super-gradients>>requirements-local.txt
    echo.
)

REM Install dependencies automatically
echo ============================================================
echo Installing/Updating dependencies...
echo This may take a few minutes on first run (downloading PyTorch)
echo ============================================================
echo.

python -m pip install --upgrade pip --quiet
python -m pip install -r requirements-local.txt --quiet

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies
    echo.
    echo Try running manually:
    echo   pip install -r requirements-local.txt
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] All dependencies installed!
echo.

REM Run the application launcher
echo ============================================================
echo Starting Tennis Pose Estimation Backend...
echo ============================================================
echo.

python app_launcher.py

REM If launcher exits, pause to see any error messages
if errorlevel 1 (
    echo.
    echo [ERROR] Application failed to start
    echo.
    pause
    exit /b 1
)

pause
