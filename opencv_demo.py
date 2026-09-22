"""Minimal OpenCV check for the UAV Ground School environment."""

import cv2


def main() -> None:
    print(f"OpenCV version: {cv2.__version__}")

    image = cv2.imread("sample.jpg")
    if image is None:
        print("No sample.jpg found. OpenCV is installed and ready to use.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(f"Loaded sample.jpg at {image.shape[1]}x{image.shape[0]}")
    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
