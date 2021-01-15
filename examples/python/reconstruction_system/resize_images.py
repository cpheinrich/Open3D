import cv2
import os

IMAGE_DIR = "dataset/guest-bedroom/image"
WIDTH = 256
HEIGHT = 144
SIZE = (WIDTH, HEIGHT)


images = sorted(os.listdir(IMAGE_DIR))

for image in images:
    img_path = os.path.join(IMAGE_DIR, image)
    img = cv2.imread(img_path)
    if img.shape[0] != HEIGHT:
        resized = cv2.resize(img, SIZE, interpolation=cv2.INTER_AREA)
        print("Image shape ", img.shape)
        cv2.imwrite(img_path, resized)
