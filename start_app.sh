#!/bin/bash
# Tennis Pose Estimation - Mac/Linux One-Click Launcher
# Double-click (or run) this file - it will install everything and start automatically!

echo ""
echo "============================================================"
echo "   Tennis Pose Estimation - One-Click Launcher"
echo "============================================================"
echo ""
echo "This will:"
echo "  1. Check Python installation"
echo "  2. Install pip (if needed)"
echo "  3. Install required packages (if needed)"
echo "  4. Start the backend server"
echo "  5. Open your browser automatically"
echo ""
echo "============================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "[ERROR] Python 3 is not installed"
    echo ""
    echo "Please install Python 3 from: https://www.python.org/downloads/"
    echo "Or use your package manager:"
    echo "  macOS: brew install python3"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[OK] Python 3 is installed"
python3 --version
echo ""

# Check if pip is installed
echo "============================================================"
echo "Checking pip installation..."
echo "============================================================"
echo ""

if ! python3 -m pip --version &> /dev/null
then
    echo "[WARNING] pip is not installed!"
    echo "[INFO] Installing pip automatically..."
    echo ""

    # Try to install pip using ensurepip
    python3 -m ensurepip --default-pip

    if [ $? -ne 0 ]; then
        echo ""
        echo "[ERROR] Failed to install pip automatically"
        echo ""
        echo "Please install pip manually:"
        echo "  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
        echo "  python3 get-pip.py"
        echo ""
        echo "Or use your package manager:"
        echo "  macOS: python3 -m ensurepip --upgrade"
        echo "  Ubuntu/Debian: sudo apt install python3-pip"
        echo "  Fedora: sudo dnf install python3-pip"
        echo ""
        read -p "Press Enter to exit..."
        exit 1
    fi

    echo ""
    echo "[OK] pip installed successfully!"
    echo ""
fi

echo "[OK] pip is installed"
python3 -m pip --version
echo ""

# Check if requirements file exists
if [ ! -f "requirements-local.txt" ]; then
    echo "[WARNING] requirements-local.txt not found!"
    echo "Creating basic requirements file..."
    cat > requirements-local.txt << EOF
flask
flask-cors
opencv-python-headless
torch
super-gradients
EOF
    echo ""
fi

# Upgrade pip first
echo "============================================================"
echo "Upgrading pip to latest version..."
echo "============================================================"
echo ""

python3 -m pip install --upgrade pip

if [ $? -ne 0 ]; then
    echo "[WARNING] Failed to upgrade pip, but continuing..."
    echo ""
fi

# Install dependencies automatically
echo "============================================================"
echo "Installing/Updating dependencies..."
echo "This may take a few minutes on first run (downloading PyTorch)"
echo "============================================================"
echo ""

python3 -m pip install -r requirements-local.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Failed to install dependencies"
    echo ""
    echo "Try running manually:"
    echo "  python3 -m pip install -r requirements-local.txt"
    echo ""
    echo "Or install one by one:"
    echo "  python3 -m pip install flask"
    echo "  python3 -m pip install flask-cors"
    echo "  python3 -m pip install opencv-python-headless"
    echo "  python3 -m pip install torch"
    echo "  python3 -m pip install super-gradients"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo ""
echo "[OK] All dependencies installed!"
echo ""

# Run the application launcher
echo "============================================================"
echo "Starting Tennis Pose Estimation Backend..."
echo "============================================================"
echo ""

python3 app_launcher.py

# If launcher exits with error, pause
if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Application failed to start"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi
