"""Sample frames from a video and stitch them with OpenCV's built-in Stitcher."""

import os
import cv2

VIDEO = "Minecraft_stitch_test.mp4"
FRAME_STEP = 30 
MAX_WIDTH = 1280

os.makedirs("output", exist_ok=True)

cap = cv2.VideoCapture(VIDEO)
if not cap.isOpened():
    raise RuntimeError(f"Could not open {VIDEO}")

frames = []
index = 0

while True:
    ok, frame = cap.read()
    if not ok:
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

stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, panorama = stitcher.stitch(frames)

if status != cv2.Stitcher_OK:
    raise RuntimeError(f"Stitching failed with status {status}")

cv2.imwrite("output/panorama.jpg", panorama)
print(f"Saved output/panorama.jpg ({panorama.shape[1]}x{panorama.shape[0]})")
