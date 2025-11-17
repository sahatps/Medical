from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import tempfile
import torch
from super_gradients.training import models
from super_gradients.training.utils.visualization.pose_estimation import PoseVisualization
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi'}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Global settings
settings = {
    'model_path': None,
    'device': 'cpu',  # 'cpu' or 'cuda'
    'use_custom_path': False
}

# Cache for models
model_cache = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_device():
    """Get the selected device (CPU or GPU)"""
    if settings['device'] == 'cuda' and torch.cuda.is_available():
        return 'cuda'
    return 'cpu'

def get_model_name_key(model_name):
    """Get the full model key from short name"""
    model_dict = {
        "N": "yolo_nas_pose_n",
        "S": "yolo_nas_pose_s",
        "M": "yolo_nas_pose_m",
        "L": "yolo_nas_pose_l"
    }
    return model_dict.get(model_name)

def check_model_exists(model_name):
    """Check if model exists locally"""
    model_name_key = get_model_name_key(model_name)
    if not model_name_key:
        return False

    # Check custom path first
    if settings['use_custom_path'] and settings['model_path']:
        custom_file = os.path.join(settings['model_path'], f"{model_name_key}.pth")
        if os.path.exists(custom_file):
            return True

    # Check default cache location
    cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints/")
    default_file = os.path.join(cache_dir, f"{model_name_key}.pth")
    return os.path.exists(default_file)

def get_model(model_name):
    """Get or load model with caching"""
    cache_key = f"{model_name}_{settings['device']}"

    if cache_key in model_cache:
        return model_cache[cache_key]

    model_name_key = get_model_name_key(model_name)
    if not model_name_key:
        raise ValueError(f"Invalid model name: {model_name}")

    print(f"Loading model: {model_name_key}")

    # Check if model exists locally
    if not check_model_exists(model_name):
        print(f"Model {model_name_key} not found locally. Downloading...")
        print("This may take a few minutes depending on your internet speed.")

    # Load model
    if settings['use_custom_path'] and settings['model_path']:
        # Load from custom path if specified
        model_file = os.path.join(settings['model_path'], f"{model_name_key}.pth")
        if os.path.exists(model_file):
            print(f"Loading from custom path: {model_file}")
            model = models.get(model_name_key, checkpoint_path=model_file)
        else:
            # Fallback to default if custom path doesn't have the model
            print("Model not found in custom path, downloading to default location...")
            model = models.get(model_name_key, pretrained_weights="coco_pose")
    else:
        # Use default cache location (will auto-download if not exists)
        model = models.get(model_name_key, pretrained_weights="coco_pose")

    print(f"Model {model_name_key} loaded successfully!")

    # Move model to selected device
    device = get_device()
    print(f"Moving model to {device.upper()}...")
    model = model.to(device)

    model_cache[cache_key] = model
    return model

def process_single_image(image, prediction):
    """Process a single frame with pose estimation"""
    pose_data = prediction.prediction
    skeleton_image = PoseVisualization.draw_poses(
        image=image.copy(),
        poses=pose_data.poses,
        boxes=pose_data.bboxes_xyxy,
        scores=pose_data.scores,
        is_crowd=None,
        edge_links=pose_data.edge_links,
        edge_colors=pose_data.edge_colors,
        keypoint_colors=pose_data.keypoint_colors,
        joint_thickness=2,
        box_thickness=2,
        keypoint_radius=5
    )
    return skeleton_image

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    cuda_available = torch.cuda.is_available()
    cuda_device_name = torch.cuda.get_device_name(0) if cuda_available else "N/A"

    return jsonify({
        'status': 'ok',
        'message': 'Local Pose Estimation Backend is running',
        'device': settings['device'],
        'cuda_available': cuda_available,
        'cuda_device': cuda_device_name,
        'model_path': settings['model_path'],
        'use_custom_path': settings['use_custom_path']
    })

@app.route('/api/settings', methods=['GET', 'POST'])
def manage_settings():
    """Get or update settings"""
    if request.method == 'GET':
        return jsonify({
            'settings': settings,
            'cuda_available': torch.cuda.is_available(),
            'cuda_device': torch.cuda.get_device_name(0) if torch.cuda.is_available() else None
        })

    elif request.method == 'POST':
        data = request.get_json()

        if 'model_path' in data:
            path = data['model_path']
            if path and os.path.isdir(path):
                settings['model_path'] = path
                settings['use_custom_path'] = True
            else:
                settings['use_custom_path'] = False

        if 'device' in data:
            device = data['device']
            if device == 'cuda' and not torch.cuda.is_available():
                return jsonify({'error': 'CUDA is not available on this system'}), 400
            settings['device'] = device
            # Clear cache when device changes
            model_cache.clear()

        if 'use_custom_path' in data:
            settings['use_custom_path'] = data['use_custom_path']

        return jsonify({'success': True, 'settings': settings})

@app.route('/api/check-model', methods=['POST'])
def check_model():
    """Check if a specific model exists locally"""
    data = request.get_json()
    model_name = data.get('model', 'N')

    try:
        exists = check_model_exists(model_name)
        model_name_key = get_model_name_key(model_name)

        # Get model file path
        cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints/")
        default_path = os.path.join(cache_dir, f"{model_name_key}.pth")

        custom_path = None
        if settings['use_custom_path'] and settings['model_path']:
            custom_path = os.path.join(settings['model_path'], f"{model_name_key}.pth")

        return jsonify({
            'model': model_name,
            'model_key': model_name_key,
            'exists': exists,
            'default_path': default_path,
            'custom_path': custom_path,
            'using_custom': settings['use_custom_path']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download-model', methods=['POST'])
def download_model():
    """Download a specific model"""
    data = request.get_json()
    model_name = data.get('model', 'N')

    try:
        model_name_key = get_model_name_key(model_name)
        if not model_name_key:
            return jsonify({'error': 'Invalid model name'}), 400

        # Check if already exists
        if check_model_exists(model_name):
            cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints/")
            model_file = os.path.join(cache_dir, f"{model_name_key}.pth")
            return jsonify({
                'success': True,
                'message': f'Model {model_name} already exists',
                'path': model_file,
                'already_exists': True
            })

        print(f"Downloading model {model_name_key}...")

        # Download model (this will cache it)
        model = models.get(model_name_key, pretrained_weights="coco_pose")

        # Get model cache path
        cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints/")
        model_file = os.path.join(cache_dir, f"{model_name_key}.pth")

        print(f"Model {model_name_key} downloaded successfully!")

        return jsonify({
            'success': True,
            'message': f'Model {model_name} downloaded successfully',
            'path': model_file,
            'exists': os.path.exists(model_file),
            'already_exists': False
        })

    except Exception as e:
        print(f"Error downloading model: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/process-video', methods=['POST'])
def process_video():
    """Process uploaded video with pose estimation"""
    try:
        # Check if video file is present
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400

        video_file = request.files['video']
        model_name = request.form.get('model', 'N')

        if video_file.filename == '':
            return jsonify({'error': 'No video file selected'}), 400

        if not allowed_file(video_file.filename):
            return jsonify({'error': 'Invalid file type. Allowed types: mp4, mov, avi'}), 400

        # Save uploaded video
        filename = secure_filename(video_file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"input_{filename}")
        video_file.save(input_path)

        # Output path
        output_filename = f"output_{filename}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        # Load model
        device = get_device()
        model = get_model(model_name)

        # Open video
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            os.remove(input_path)
            return jsonify({'error': 'Could not open video file'}), 400

        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_count = 0

        print(f"Processing video on {device.upper()}...")
        print(f"Total frames: {total_frames}")

        # Process video frame by frame
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Run pose estimation
            result = model.predict(frame, conf=0.4, fuse_model=False)
            skeleton_frame = process_single_image(frame, result)

            # Write processed frame
            out.write(skeleton_frame)
            frame_count += 1

            if frame_count % 30 == 0:  # Log every 30 frames
                print(f"Processed {frame_count}/{total_frames} frames ({(frame_count/total_frames*100):.1f}%)")

        # Cleanup
        cap.release()
        out.release()
        os.remove(input_path)

        print(f"Processing complete! Output saved to: {output_path}")

        # Return processed video
        return send_file(
            output_path,
            mimetype='video/mp4',
            as_attachment=True,
            download_name=output_filename
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get information about available models"""
    models_info = {
        "N": {
            "name": "YOLO-NAS Pose Nano",
            "speed": "Fastest",
            "accuracy": "Good",
            "size": "~50MB"
        },
        "S": {
            "name": "YOLO-NAS Pose Small",
            "speed": "Fast",
            "accuracy": "Better",
            "size": "~70MB"
        },
        "M": {
            "name": "YOLO-NAS Pose Medium",
            "speed": "Medium",
            "accuracy": "Great",
            "size": "~120MB"
        },
        "L": {
            "name": "YOLO-NAS Pose Large",
            "speed": "Slower",
            "accuracy": "Best",
            "size": "~200MB"
        }
    }

    # Check which models are already downloaded
    cache_dir = os.path.expanduser("~/.cache/torch/hub/checkpoints/")
    for model_key in models_info:
        model_dict = {"N": "yolo_nas_pose_n", "S": "yolo_nas_pose_s",
                     "M": "yolo_nas_pose_m", "L": "yolo_nas_pose_l"}
        model_file = os.path.join(cache_dir, f"{model_dict[model_key]}.pth")
        models_info[model_key]["downloaded"] = os.path.exists(model_file)
        models_info[model_key]["path"] = model_file if os.path.exists(model_file) else None

    return jsonify(models_info)

if __name__ == '__main__':
    print("=" * 60)
    print("Tennis Pose Estimation - Local Backend")
    print("=" * 60)
    print(f"CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA Device: {torch.cuda.get_device_name(0)}")
        print(f"Current Device: {settings['device'].upper()}")
    else:
        print("Running on CPU")
    print(f"Model Cache: ~/.cache/torch/hub/checkpoints/")
    print("=" * 60)
    print("\nBackend is running on http://localhost:5000")
    print("Access the web interface at your Vercel URL or index.html")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)

    app.run(debug=True, host='0.0.0.0', port=5000)
