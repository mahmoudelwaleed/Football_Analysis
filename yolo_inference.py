# Description: This script is used to perform inference on a video using the YOLOv5 model.

from ultralytics import YOLO

model = YOLO('models/best.pt')  # Use YOLOv8 (Recommended)


result = model.predict(r"input_videos/test.mp4", save=True)

print(result[0])
print("=====================================")
for box in result[0].boxes:
    print(box)