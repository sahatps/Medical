# Tennis Pose Estimation Web Application

เว็บแอปพลิเคชันสำหรับวิเคราะห์ท่าทางในวิดีโอเทนนิสโดยใช้ YOLO-NAS Pose Estimation

## 🎯 จุดเด่น (ฟรี 100%!)

- ✅ **ประมวลผลบนเครื่องตัวเอง** - ใช้ GPU/CPU ของคุณเอง ไม่มี timeout!
- ✅ **เลือก Model Path ได้** - กำหนดที่เก็บโมเดลได้ตามต้องการ
- ✅ **รองรับ GPU (CUDA)** - ประมวลผลเร็วด้วย GPU ของคุณ
- ✅ **Frontend บน Vercel (ฟรี)** - เว็บ UI สวยงามโหลดเร็ว
- ✅ **ไม่มีค่าใช้จ่าย** - Backend รันบนเครื่องคุณ, Frontend ฟรีบน Vercel

## คุณสมบัติ

- อัปโหลดวิดีโอ (MP4, MOV, AVI) ขนาดใหญ่ได้ (500MB)
- เลือกโมเดล AI (N, S, M, L) ตามความต้องการความเร็วและความแม่นยำ
- เลือกใช้ CPU หรือ GPU (CUDA) สำหรับประมวลผล
- กำหนด Model Cache Path เองได้
- ประมวลผลวิดีโอและแสดงโครงกระดูกของผู้เล่น
- ดาวน์โหลดวิดีโอที่ผ่านการประมวลผล
- Frontend deploy บน Vercel (ฟรี)

## โมเดล AI ที่รองรับ

- **Nano (N)**: เร็วที่สุด, ขนาดเล็ก
- **Small (S)**: เร็ว, ความแม่นยำดี
- **Medium (M)**: สมดุลระหว่างความเร็วและความแม่นยำ
- **Large (L)**: ความแม่นยำสูงสุด, ช้าที่สุด

## 🚀 วิธีใช้งาน (3 ขั้นตอน)

### ขั้นตอนที่ 1: ติดตั้ง Backend บนเครื่องคุณ

#### ความต้องการของระบบ
- Python 3.8 ขึ้นไป
- pip
- (Optional) NVIDIA GPU + CUDA สำหรับประมวลผลเร็วขึ้น

#### ติดตั้ง Dependencies

```bash
# ติดตั้ง Python packages
pip install -r requirements.txt
```

#### สำหรับผู้ใช้ GPU (Optional)
```bash
# ติดตั้ง PyTorch with CUDA support
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### ขั้นตอนที่ 2: รัน Backend บนเครื่อง

#### Windows:
```bash
start_backend.bat
```

#### Mac/Linux:
```bash
chmod +x start_backend.sh
./start_backend.sh
```

#### หรือรันด้วยคำสั่ง Python:
```bash
python local_backend.py
```

Backend จะรันที่ `http://localhost:5000`

### ขั้นตอนที่ 3: เข้าใช้งานผ่าน Browser

**ตัวเลือก A: ใช้ผ่าน Vercel (แนะนำ)**
1. Deploy frontend บน Vercel (ดูขั้นตอนด้านล่าง)
2. เปิด URL ที่ Vercel ให้มา เช่น `https://your-app.vercel.app`
3. Backend URL จะถูกตั้งเป็น `http://localhost:5000` อัตโนมัติ

**ตัวเลือก B: เปิดไฟล์ในเครื่อง**
1. เปิดไฟล์ `public/index.html` ด้วย browser
2. ตั้งค่า Backend URL เป็น `http://localhost:5000`

## 🌐 การ Deploy Frontend บน Vercel (ฟรี!)

Vercel จะใช้เป็น **Static Site Hosting** เท่านั้น (ไม่มีข้อจำกัด timeout หรือ memory!)

### วิธี Deploy

#### วิธีที่ 1: ใช้ Vercel Dashboard (ง่ายสุด)

1. สร้าง GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit: Tennis Pose Estimation"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

2. ไปที่ [Vercel Dashboard](https://vercel.com/dashboard)

3. คลิก "Add New Project"

4. Import repository จาก GitHub

5. Vercel จะตรวจจับ `vercel.json` อัตโนมัติ

6. คลิก "Deploy"

7. เสร็จแล้ว! คุณจะได้ URL เช่น `https://tennis-pose.vercel.app`

#### วิธีที่ 2: ใช้ Vercel CLI

```bash
# ติดตั้ง Vercel CLI
npm install -g vercel

# Deploy
vercel

# หรือ deploy เป็น production
vercel --prod
```

### ✅ ข้อดีของระบบนี้

- ✅ **ไม่มี Timeout** - ประมวลผลบนเครื่องคุณเอง นานแค่ไหนก็ได้!
- ✅ **ไม่มี Memory Limit** - ใช้ RAM/GPU ของคุณเองเต็มที่
- ✅ **Vercel ฟรี** - เพราะใช้แค่ static hosting
- ✅ **วิดีโอขนาดใหญ่ได้** - จำกัดแค่ storage ของคุณ
- ✅ **โมเดลใหญ่ได้** - ไม่มีข้อจำกัด download size

## 📁 โครงสร้างโปรเจกต์

```
tenniss/
├── public/
│   └── index.html           # Frontend (Static site สำหรับ Vercel)
├── local_backend.py         # Backend ที่รันบนเครื่องคุณ
├── start_backend.bat        # Script รัน backend (Windows)
├── start_backend.sh         # Script รัน backend (Mac/Linux)
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration (Static hosting)
├── package.json            # Project metadata
├── .gitignore              # Git ignore rules
└── README.md               # Documentation (ไฟล์นี้)
```

## ⚙️ การตั้งค่า

### เลือก GPU/CPU

ในหน้าเว็บ คุณสามารถเลือกได้ว่าจะใช้:
- **CPU**: ประมวลผลช้ากว่า แต่ทุกเครื่องมี
- **GPU (CUDA)**: ประมวลผลเร็วมาก ต้องมี NVIDIA GPU

### กำหนด Model Path

คุณสามารถกำหนดที่เก็บ model ได้ 2 แบบ:

1. **ใช้ Default Path** (แนะนำ):
   - Windows: `C:\Users\YOUR_NAME\.cache\torch\hub\checkpoints\`
   - Mac/Linux: `~/.cache/torch/hub/checkpoints/`

2. **กำหนด Custom Path**:
   - ใส่ path ที่ต้องการในหน้าเว็บ
   - โมเดลจะถูกโหลดมาจาก path ที่กำหนด

## 🔌 API Endpoints (Local Backend)

### GET /api/health
ตรวจสอบสถานะของ Backend
```json
{
  "status": "ok",
  "message": "Local Pose Estimation Backend is running",
  "device": "cuda",
  "cuda_available": true,
  "cuda_device": "NVIDIA GeForce RTX 3080",
  "model_path": null,
  "use_custom_path": false
}
```

### GET /api/settings
ดูการตั้งค่าปัจจุบัน

### POST /api/settings
อัพเดทการตั้งค่า
```json
{
  "device": "cuda",           // "cpu" หรือ "cuda"
  "model_path": "/path/to/models",
  "use_custom_path": true
}
```

### GET /api/model-info
ดูข้อมูลโมเดลที่มี

### POST /api/download-model
ดาวน์โหลดโมเดล
```json
{
  "model": "N"  // N, S, M, หรือ L
}
```

### POST /api/process-video
ประมวลผลวิดีโอ

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body:
  - `video`: ไฟล์วิดีโอ (MP4, MOV, AVI)
  - `model`: โมเดล AI (N, S, M, L)

**Response:**
- วิดีโอที่ผ่านการประมวลผล (video/mp4)

## 🛠️ เทคโนโลยีที่ใช้

- **Backend**: Flask (Python) - รันบน Local
- **Frontend**: HTML, CSS, JavaScript - Host บน Vercel
- **AI Model**: YOLO-NAS Pose Estimation (Super-Gradients)
- **Deep Learning**: PyTorch + CUDA Support
- **Computer Vision**: OpenCV
- **Hosting**: Vercel (Static Site - ฟรี!)

## 🎓 Architecture

```
┌─────────────────┐
│   Vercel        │
│   (Frontend)    │  <- Static HTML/CSS/JS (ฟรี)
│  your-app.      │
│  vercel.app     │
└────────┬────────┘
         │ HTTP Request
         ↓
┌─────────────────┐
│  Your Computer  │
│  (Backend)      │  <- Flask + PyTorch + GPU
│  localhost:5000 │
└─────────────────┘
         │
         ↓
    Process Video
    with AI Model
```

## 🔧 Troubleshooting

### Backend ไม่ติด
- ตรวจสอบว่ารัน `python local_backend.py` แล้วหรือยัง
- ตรวจสอบว่า port 5000 ไม่ถูกใช้งานโดยโปรแกรมอื่น
- ลองเปลี่ยน port ใน `local_backend.py` (บรรทัดสุดท้าย)

### GPU ไม่ทำงาน
- ตรวจสอบว่าติดตั้ง CUDA แล้ว: `nvidia-smi`
- ติดตั้ง PyTorch with CUDA: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118`
- ตรวจสอบใน Backend console ว่า CUDA available หรือไม่

### ประมวลผลช้า
- ลองใช้โมเดลเล็กกว่า (N แทน L)
- เปลี่ยนจาก CPU เป็น GPU (ถ้ามี)
- ลดความละเอียดของวิดีโอ

## 📝 License

MIT

## 👨‍💻 Author

Tennis Pose Estimation Project - Local Processing Edition

---

**สนุกกับการวิเคราะห์ท่าทางเทนนิส! 🎾**
