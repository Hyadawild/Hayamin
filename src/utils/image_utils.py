"""
Image processing utilities for Ayaya Upscaler
"""
import cv2
import numpy as np
from PIL import Image

def convert_to_rgb(image):
    """Convert image to RGB format if needed"""
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:
        return cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return image

def load_image(image_path):
    """Load and preprocess image from path"""
    img = Image.open(image_path)
    img = np.array(img)
    return convert_to_rgb(img)

def save_image(image, output_path):
    """Save image to specified path"""
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    image.save(output_path)