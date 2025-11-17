# Tennis Pose Estimation - Browser Auto Processing

**Automatic pose estimation running 100% in your browser - No backend setup required!**

## 🎯 Key Features

- ✅ **Fully Automatic** - Just open the link and use immediately
- ✅ **No Installation** - Runs directly in your web browser
- ✅ **No Backend Server** - Everything processes on your device
- ✅ **Uses Your CPU/GPU** - Automatic hardware acceleration via WebGL
- ✅ **100% Free** - No server costs, no API fees
- ✅ **Privacy First** - Videos never leave your device
- ✅ **Deploy Anywhere** - Works on Vercel, GitHub Pages, or open locally

## 🚀 How to Use (Just 1 Step!)

### Option 1: Use Deployed Version (Recommended)
1. Open the deployed URL (e.g., on Vercel)
2. Upload a video
3. Click "Start Processing"
4. Download the result!

### Option 2: Open Locally
1. Open `public/index.html` in your web browser
2. Upload a video
3. Click "Start Processing"
4. Download the result!

That's it! No Python, no backend server, no installation needed!

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

- **Frontend**: Pure HTML, CSS, JavaScript
- **AI Engine**: MediaPipe Pose (Google)
- **Processing**: WebAssembly + WebGL acceleration
- **Recording**: MediaRecorder API
- **Hosting**: Static hosting (Vercel, GitHub Pages, etc.)

## 📁 Project Structure

```
Medical/
├── public/
│   └── index.html          # Complete application (all-in-one file)
├── local_backend.py        # OLD - No longer needed
├── vercel.json            # Vercel configuration
├── package.json           # Project metadata
└── README.md             # This file
```

## 🔍 How It Works

1. **User uploads video** - Video loaded into browser memory
2. **MediaPipe initializes** - AI model loads from CDN (cached after first use)
3. **Frame-by-frame processing**:
   - Video plays in the background
   - Each frame is analyzed by MediaPipe Pose
   - Skeleton overlay is drawn on canvas
   - Canvas is recorded in real-time
4. **Output generation** - Recorded frames compiled into WebM video
5. **Download** - User downloads the processed video

All of this happens in your browser using WebAssembly and WebGL!

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
