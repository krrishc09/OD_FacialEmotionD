from ultralytics import YOLO
import cv2
model=YOLO('../Yolo-Weights/yolov8l.pt')
results=model("Resources/Traffic.mp4", show=True)
cv2.waitKey(0)