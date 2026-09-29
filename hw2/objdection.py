import glob
import os
import cv2

HW2_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(HW2_DIR, "TestImages")
OUTPUT_DIR = os.path.join(HW2_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

params = cv2.SimpleBlobDetector_Params()
params.filterByColor = False
params.filterByArea = True
params.minArea = 100
params.maxArea = 200000
params.filterByCircularity = True
params.minCircularity = 0.6
params.filterByInertia = True
params.minInertiaRatio = 0.6

detector = cv2.SimpleBlobDetector_create(params)

image_paths = sorted(glob.glob(os.path.join(IMAGE_DIR, "polka_dots_*")))

for image_path in image_paths:
    image = cv2.imread(image_path)
    blue, green, red = cv2.split(image)

    keypoints = []
    for channel in (blue, green, red):
        channel = cv2.GaussianBlur(channel, (7, 7), 0)
        keypoints.extend(detector.detect(channel))

    marked = cv2.drawKeypoints(
        image,
        keypoints,
        None,
        (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )

    name = os.path.splitext(os.path.basename(image_path))[0]
    out_path = os.path.join(OUTPUT_DIR, f"{name}_blobs.jpg")
    cv2.imwrite(out_path, marked)
    print(f"{name}: found {len(keypoints)} polka dots")
