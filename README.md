# Tennis Pose Estimation - Dual Engine Support

**Choose between browser-based processing (MediaPipe) or powerful backend processing (YOLO-NAS)!**

## 🎯 Key Features

- ✅ **Dual Engine Support** - Choose MediaPipe (Browser) or YOLO-NAS (Backend)
- ✅ **MediaPipe Mode** - 100% browser-based, no installation required
- ✅ **YOLO-NAS Mode** - Advanced accuracy with Python backend
- ✅ **Automatic Model Download** - Models download automatically when needed
- ✅ **Privacy First** - Browser mode keeps videos on your device
- ✅ **Flexible Deployment** - Works on Vercel, GitHub Pages, or locally
- ✅ **Easy Switching** - Toggle between engines with a dropdown

## 🚀 How to Use

### ⚡ Quick Start (Recommended) - **One-Click Launch**

**Easiest way to use both engines!**

#### Windows:
```bash
# Double-click this file:
start_app.bat

# Or run in terminal:
python app_launcher.py
```

#### Mac/Linux:
```bash
# In terminal:
./start_app.sh

# Or:
python3 app_launcher.py
```

**What happens:**
1. ✅ Automatically starts Flask backend (for YOLO-NAS)
2. ✅ Opens web interface in your browser
3. ✅ Both engines ready to use!

---

### 🌐 Engine 1: MediaPipe (Browser Mode) - **No Setup Required**

Perfect for quick, hassle-free processing!

1. Open `public/index.html` in your browser (or deployed URL)
2. Select **"MediaPipe (Browser)"** from the Pose Engine dropdown
3. Upload a video
4. Click "Start Processing"
5. Download the result!

**Advantages:**
- ✅ Zero setup - works immediately
- ✅ 100% private - videos stay in browser
- ✅ No backend server needed
- ✅ Works on any device with a browser

### 🔥 Engine 2: YOLO-NAS (Backend Mode) - **Better Accuracy**

For professional-grade pose estimation!

#### Method A: Use One-Click Launcher (Recommended)
```bash
# Backend starts automatically!
python app_launcher.py
```

#### Method B: Manual Setup
1. **Start the Backend Server:**
   ```bash
   python local_backend.py
   ```
   The server will start at `http://localhost:5000`

2. **Use the Frontend:**
   - Open `public/index.html` in your browser
   - Select **"YOLO-NAS (Backend)"** from the Pose Engine dropdown
   - The UI will automatically check backend connection
   - Choose your model: Nano (fastest) to Large (most accurate)

3. **Download Model (if needed):**
   - If the model isn't downloaded, you'll see a download button
   - Click "📥 Download Model" or it will auto-download on first use
   - Models are cached locally after download

4. **Process Video:**
   - Upload a video
   - Click "Start Processing"
   - Download the result!

**Advantages:**
- ✅ Better accuracy than MediaPipe
- ✅ 4 model sizes to choose from (Nano, Small, Medium, Large)
- ✅ GPU acceleration support (CUDA)
- ✅ Professional-grade results

## 🌐 Deploy to Vercel (Free Forever)

### Method 1: Using Vercel Dashboard (Easiest)

1. Create a GitHub repository:
```bash
git init
git add .
git commit -m "Tennis Pose Estimation - Browser Version"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "Add New Project"
4. Import your GitHub repository
5. Click "Deploy"
6. Done! You'll get a URL like `https://tennis-pose.vercel.app`

### Method 2: Using Vercel CLI

```bash
npm install -g vercel
vercel
```

## ⚙️ Settings & Configuration

The application includes adjustable settings:

- **Model Quality**:
  - Lite (Fastest)
  - Full (Balanced) - Default
  - Heavy (Best Quality)

- **Detection Confidence**: How confident the AI should be before detecting a pose
  - Low (0.3)
  - Medium (0.5) - Default
  - High (0.7)

- **Tracking Confidence**: How well poses are tracked between frames
  - Low (0.3)
  - Medium (0.5) - Default
  - High (0.7)

- **Smooth Pose**: Enable smoothing for more stable skeleton visualization

## 🎥 Supported Video Formats

- MP4
- MOV
- WebM
- Any video format supported by your browser

Output format: WebM (VP9 codec)

## 🛠️ Technology Stack

### Frontend:
- **UI**: Pure HTML, CSS, JavaScript
- **Recording**: MediaRecorder API
- **Hosting**: Static hosting (Vercel, GitHub Pages, etc.)

### AI Engines:

**Option 1: MediaPipe (Browser)**
- **Engine**: MediaPipe Pose (Google)
- **Processing**: WebAssembly + WebGL acceleration
- **Runtime**: 100% browser-based
- **Models**: Lite, Full, Heavy

**Option 2: YOLO-NAS (Backend)**
- **Engine**: SuperGradients YOLO-NAS Pose
- **Framework**: PyTorch
- **Backend**: Flask + Flask-CORS
- **Processing**: CPU or CUDA (GPU)
- **Models**: Nano (~50MB), Small (~70MB), Medium (~120MB), Large (~200MB)

## 📁 Project Structure

```
Medical/
├── public/
│   └── index.html          # Frontend with dual-engine support
├── app_launcher.py         # 🆕 One-click launcher (starts backend + opens browser)
├── start_app.bat           # 🆕 Windows launcher (double-click to run)
├── start_app.sh            # 🆕 Mac/Linux launcher
├── local_backend.py        # Flask backend for YOLO-NAS
├── requirements-local.txt  # Python dependencies for backend
├── start_backend.sh/.bat   # Manual backend startup scripts (legacy)
├── vercel.json            # Vercel configuration
├── package.json           # Project metadata
└── README.md             # This file
```

**Quick Start Files:**
- **app_launcher.py** - Main launcher (recommended)
- **start_app.bat** - Windows one-click launcher
- **start_app.sh** - Mac/Linux one-click launcher

## 🆚 Engine Comparison

| Feature | MediaPipe (Browser) | YOLO-NAS (Backend) |
|---------|--------------------|--------------------|
| **Setup** | None - instant | Python + dependencies |
| **Speed** | Fast (10-20 FPS) | Very Fast (20-60 FPS with GPU) |
| **Accuracy** | Good | Excellent |
| **Privacy** | 100% local | Requires local server |
| **Models** | 3 options | 4 options (N/S/M/L) |
| **GPU Support** | WebGL only | Full CUDA support |
| **Best For** | Quick testing, portability | Production, best quality |
| **Internet** | CDN load once | Model download once |

## 🔍 How It Works

### MediaPipe (Browser) Workflow:

1. **User uploads video** - Video loaded into browser memory
2. **MediaPipe initializes** - AI model loads from CDN (cached after first use)
3. **Frame-by-frame processing**:
   - Video plays in the background
   - Each frame is analyzed by MediaPipe Pose
   - Skeleton overlay is drawn on canvas
   - Canvas is recorded in real-time
4. **Output generation** - Recorded frames compiled into WebM video
5. **Download** - User downloads the processed video

*All processing happens in your browser using WebAssembly and WebGL!*

### YOLO-NAS (Backend) Workflow:

1. **User selects YOLO-NAS engine** - Frontend checks backend availability
2. **Model verification** - Checks if selected YOLO model is downloaded
3. **Auto-download** - Downloads model if not present (~50-200MB, one-time)
4. **Video upload** - Video sent to local backend server
5. **Backend processing**:
   - Flask receives video
   - YOLO-NAS processes each frame
   - Skeleton overlay drawn using SuperGradients
   - Processed video encoded as MP4
6. **Download** - Processed video sent back to browser

*Backend can use CUDA for GPU acceleration!*

## 💡 Key Benefits

### vs. Old Flask Backend Version:
- ❌ No Python installation needed
- ❌ No dependency management
- ❌ No backend server to run
- ❌ No CORS issues
- ✅ Instant startup
- ✅ Works on any device with a browser
- ✅ Easy to deploy and share

### vs. Cloud Processing:
- ✅ No upload time
- ✅ No download time (for input)
- ✅ Complete privacy
- ✅ No API costs
- ✅ Works offline (after first load)
- ✅ No file size limits

## 🔧 Troubleshooting

### Processing is slow
- Try using the "Lite" model quality
- Use a modern browser (Chrome, Edge, Firefox)
- Close other tabs/applications
- Reduce video resolution before uploading

### Video won't upload
- Check file format (MP4, MOV, WebM)
- Try a different browser
- Check browser console for errors

### Pose detection not working
- Ensure people are clearly visible in the video
- Try adjusting detection confidence to "Low"
- Check that the video has good lighting

### Download not working
- Check browser's download settings
- Try a different browser
- Ensure pop-ups are not blocked

## 🌟 Browser Compatibility

Works best on:
- Chrome 80+
- Edge 80+
- Firefox 75+
- Safari 14+

Requires:
- WebAssembly support
- Canvas API
- MediaRecorder API
- ES6+ JavaScript

## 📊 Performance

Approximate processing speeds (depends on device):

| Device Type | Model Quality | Speed |
|------------|---------------|-------|
| High-end laptop | Heavy | 5-10 FPS |
| Mid-range laptop | Full | 10-15 FPS |
| Low-end device | Lite | 15-20 FPS |

Note: WebGL acceleration significantly improves performance

## 🔐 Privacy & Security

- **No data collection** - Nothing is sent to any server
- **Local processing** - All computation happens in your browser
- **No tracking** - No analytics, no cookies
- **Open source** - Code is transparent and auditable

## 📝 License

MIT License - Free to use, modify, and distribute

## 👨‍💻 Credits

- **MediaPipe**: Google's ML framework for pose detection
- **Original Concept**: Tennis Pose Estimation Project

---

**Enjoy analyzing tennis poses with zero setup! 🎾**

## 🆚 Comparison: Old vs New Version

### Old Version (Flask Backend):
1. Install Python
2. Install dependencies (`pip install -r requirements.txt`)
3. Download AI models (50-200MB)
4. Run backend server (`python local_backend.py`)
5. Open frontend
6. Configure backend URL
7. Upload and process video

### New Version (Browser Auto):
1. Open link
2. Upload and process video

**That's it!** 🎉
