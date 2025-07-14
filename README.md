🔍 Project Title: RealTimeOD – Real-Time Object & Emotion Detection System
📌 Overview:
This project integrates two computer vision tasks:

Object Detection using YOLO (You Only Look Once): Real-time detection of multiple objects using different YOLOv8 models.

Facial Emotion Recognition: Detection of human facial emotions using Haar cascades and a custom emotion classifier.

🧠 Key Functionalities:
1. Facial Emotion Recognition
Script: emotion.py

Face Detection: Uses haarcascade_frontalface_default.xml

Emotion Classification: Predicts basic human emotions (e.g., happy, sad, angry) using facial features.

Testing Resource: emotion.png

2. YOLO-based Object Detection
Scripts:

yolo_basics.py: Detects objects in images or videos.

yolo-webcam.py: Performs real-time object detection using a webcam.

Models Used:

yolov8n.pt – Nano version (fast, lightweight)

yolov8l.pt – Large version (accurate, heavy)

Sample Data: Found in Resources/ folder:

Images: 1.png, 2.png, emotion.png

Video: Traffic.mp4

🗂 Folder Structure:
Folder/File	Description
face-emotions/	Facial emotion recognition logic and model
emotion.py	Main emotion detection script
haarcascade_frontalface_default.xml	Face detection Haar model
requirements.txt	Dependencies for emotion detection
yolo run/	Contains object detection scripts and test resources
Resources/	Images and videos used for detection testing
yolo_basics.py	Object detection from media files
Yolo with Webcam/	Folder for webcam-based detection
yolo-webcam.py	Real-time detection script using webcam
Yolo-Weights/	YOLOv8 model weights (.pt files)
requirements.txt	Dependencies for YOLO object detection

🧰 Technologies Used:
Languages & Libraries: Python, OpenCV, PyTorch, NumPy

Frameworks: Ultralytics YOLOv8, Haarcascade

Tools: Visual Studio Code, command-line interface
