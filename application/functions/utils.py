import os
import cv2
import numpy as np

def load_image(file_path):
    module_dir, _ = os.path.split(os.path.realpath(__file__))
    absolute_path = os.path.join(module_dir, file_path)
    image = cv2.imread(absolute_path)
    # (h, w, c), uint8
    # Change BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def load_template(file_path, resize_shape, color):
    module_dir, _ = os.path.split(os.path.realpath(__file__))
    absolute_path = os.path.join(module_dir, file_path)
    image = cv2.imread(absolute_path, -1) # -1 == RGBA
    image = cv2.resize(image, resize_shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i][j]
            rate = pixel[3] / 255
            pixel[0] = int(255 - rate * (255 - color[0]))
            pixel[1] = int(255 - rate * (255 - color[1]))
            pixel[2] = int(255 - rate * (255 - color[2]))
            pixel = np.clip(pixel, 0, 255)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    return image

def save_image(image, file_path):
    module_dir, _ = os.path.split(os.path.realpath(__file__))
    absolute_path = os.path.join(module_dir + "/../..", file_path)

    # Change RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(absolute_path, image)
