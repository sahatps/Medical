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
echo   2. Install pip (if needed)
echo   3. Install required packages (if needed)
echo   4. Start the backend server
echo   5. Open your browser automatically
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

REM Check if pip is installed
echo ============================================================
echo Checking pip installation...
echo ============================================================
echo.

python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] pip is not installed!
    echo [INFO] Installing pip automatically...
    echo.

    REM Try to install pip using ensurepip
    python -m ensurepip --default-pip

    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to install pip automatically
        echo.
        echo Please install pip manually:
        echo   1. Download get-pip.py from: https://bootstrap.pypa.io/get-pip.py
        echo   2. Run: python get-pip.py
        echo.
        echo Or reinstall Python with pip included:
        echo   https://www.python.org/downloads/
        echo   Make sure to check "pip" during installation
        echo.
        pause
        exit /b 1
    )

    echo.
    echo [OK] pip installed successfully!
    echo.
)

echo [OK] pip is installed
python -m pip --version
echo.

REM Check if requirements file exists
if not exist requirements-local.txt (
    echo [WARNING] requirements-local.txt not found!
    echo Creating basic requirements file...
    (
        echo flask
        echo flask-cors
        echo opencv-python-headless
        echo torch
        echo super-gradients
    ) > requirements-local.txt
    echo.
)

REM Upgrade pip first
echo ============================================================
echo Upgrading pip to latest version...
echo ============================================================
echo.

python -m pip install --upgrade pip

if errorlevel 1 (
    echo [WARNING] Failed to upgrade pip, but continuing...
    echo.
)

REM Install dependencies automatically
echo ============================================================
echo Installing/Updating dependencies...
echo This may take a few minutes on first run (downloading PyTorch)
echo ============================================================
echo.

python -m pip install -r requirements-local.txt

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies
    echo.
    echo Try running manually:
    echo   python -m pip install -r requirements-local.txt
    echo.
    echo Or install one by one:
    echo   python -m pip install flask
    echo   python -m pip install flask-cors
    echo   python -m pip install opencv-python-headless
    echo   python -m pip install torch
    echo   python -m pip install super-gradients
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
