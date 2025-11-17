#!/usr/bin/env python3
"""
Tennis Pose Estimation - Application Launcher
Automatically starts the Flask backend and opens the web interface
"""

import os
import sys
import time
import threading
import webbrowser
from pathlib import Path

def print_banner():
    """Print application banner"""
    print("=" * 70)
    print("🎾 Tennis Pose Estimation - Application Launcher")
    print("=" * 70)
    print()

def check_dependencies():
    """Check if required dependencies are installed"""
    print("📦 Checking dependencies...")

    required_packages = [
        'flask',
        'flask_cors',
        'cv2',
        'torch',
        'super_gradients'
    ]

    missing_packages = []

    for package in required_packages:
        try:
            if package == 'cv2':
                import cv2
            elif package == 'flask_cors':
                import flask_cors
            elif package == 'super_gradients':
                import super_gradients
            else:
                __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} - NOT INSTALLED")
            missing_packages.append(package)

    if missing_packages:
        print("\n⚠️  Missing dependencies detected!")
        print("🔧 Auto-installing missing packages...")
        print()

        # Auto-install missing packages
        import subprocess

        # Map package names to pip install names
        pip_package_map = {
            'cv2': 'opencv-python-headless',
            'flask_cors': 'flask-cors',
            'super_gradients': 'super-gradients'
        }

        for pkg in missing_packages:
            pip_name = pip_package_map.get(pkg, pkg)
            print(f"  📥 Installing {pip_name}...")

            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', pip_name, '--quiet'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f"  ✅ {pip_name} installed successfully!")
            except subprocess.CalledProcessError:
                print(f"  ❌ Failed to install {pip_name}")
                print(f"\n⚠️  Please install manually: pip install {pip_name}")
                print("\nOr run: pip install -r requirements-local.txt")
                print()
                response = input("Continue anyway? (y/N): ").strip().lower()
                if response != 'y':
                    print("Exiting...")
                    sys.exit(1)

        print("\n✅ All missing dependencies have been installed!")
        print("🔄 Please restart the application to use the new packages.\n")
        sys.exit(0)

    print("✅ All dependencies are installed!\n")

def start_backend():
    """Start Flask backend server in a separate thread"""
    print("🚀 Starting Flask backend server...")

    try:
        # Import Flask app
        from local_backend import app

        # Run Flask app (suppress Flask's default output)
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        sys.exit(1)

def wait_for_backend(url='http://localhost:5000', timeout=30):
    """Wait for backend to be ready"""
    import urllib.request
    import urllib.error

    print("⏳ Waiting for backend to start", end='', flush=True)
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            urllib.request.urlopen(f"{url}/api/health", timeout=1)
            print(" ✅")
            return True
        except (urllib.error.URLError, ConnectionRefusedError):
            print(".", end='', flush=True)
            time.sleep(0.5)

    print(" ❌")
    print(f"⚠️  Backend failed to start within {timeout} seconds")
    return False

def open_browser():
    """Open the web interface in default browser"""
    # Find the HTML file
    html_path = Path(__file__).parent / 'public' / 'index.html'

    if not html_path.exists():
        print(f"❌ Error: {html_path} not found!")
        return False

    # Convert to absolute file URL
    file_url = f"file://{html_path.absolute()}"

    print(f"🌐 Opening web interface...")
    print(f"   URL: {file_url}")

    try:
        webbrowser.open(file_url)
        print("✅ Web interface opened in your default browser!")
        return True
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print(f"\nPlease manually open: {html_path}")
        return False

def main():
    """Main application launcher"""
    print_banner()

    # Check dependencies
    check_dependencies()

    # Start Flask backend in a separate thread
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()

    # Wait for backend to be ready
    if not wait_for_backend():
        print("❌ Failed to start backend server")
        sys.exit(1)

    print("✅ Backend server is running at http://localhost:5000")
    print()

    # Open browser
    open_browser()

    print()
    print("=" * 70)
    print("📝 Instructions:")
    print("   1. The web interface should open in your browser")
    print("   2. Select 'YOLO-NAS (Backend)' from the Pose Engine dropdown")
    print("   3. Choose your model and upload a video")
    print("   4. Click 'Start Processing' to begin")
    print()
    print("💡 Both engines are now available:")
    print("   • MediaPipe (Browser) - Works in browser, no backend needed")
    print("   • YOLO-NAS (Backend) - Uses the Flask backend running now")
    print()
    print("⚠️  To stop the application: Press Ctrl+C")
    print("=" * 70)
    print()

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
        print("✅ Application stopped successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
