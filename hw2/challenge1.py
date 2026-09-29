import os
import matplotlib.pyplot as plt
from skimage import color, feature, io

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("challenge_output", exist_ok=True)

for filename in ["polka_dots_1.png", "polka_dots_2.jpg", "polka_dots_3.jpg"]:
    image = color.rgb2gray(io.imread("TestImages/" + filename)[:, :, :3])
    blobs_log = feature.blob_log(image, max_sigma=30, num_sigma=10, threshold=0.1)

    # Compute radii
    blobs_log[:, 2] = blobs_log[:, 2] * (2 ** 0.5)

    # Display
    fig, ax = plt.subplots()
    ax.imshow(image, cmap="gray")
    for y, x, r in blobs_log:
        c = plt.Circle((x, y), r, color="red", linewidth=2, fill=False)
        ax.add_patch(c)
    fig.savefig("challenge_output/" + filename.split(".")[0] + "_log.jpg")
    plt.close()
