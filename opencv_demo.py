"""Sample frames from a video and stitch them with OpenCV's built-in Stitcher."""

import os
import cv2

VIDEO = "Minecraft_stitch_test.mp4"
FRAME_STEP = 30 
MAX_WIDTH = 1280

os.makedirs("output", exist_ok=True)

cap = cv2.VideoCapture(VIDEO)
frames = []
index = 0
#add video frames every 30 frames to frames array after resizing and scaling
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if index % FRAME_STEP == 0:
        height, width = frame.shape[:2]
        if width > MAX_WIDTH:
            scale = MAX_WIDTH / width
            frame = cv2.resize(frame, (int(width * scale), int(height * scale)))
        frames.append(frame)
        cv2.imwrite(f"output/frame_{len(frames) - 1:03d}.jpg", frame)

    index += 1

cap.release()
print(f"Sampled {len(frames)} frames")
#create stitcher and input frames
stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, panorama = stitcher.stitch(frames)

if status != cv2.Stitcher_OK:
    raise RuntimeError(f"Stitching failed with status {status}")
#write stitched image to a new file
cv2.imwrite("output/panorama.jpg", panorama)