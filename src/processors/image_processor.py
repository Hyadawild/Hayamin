"""
Image processing functionality
"""
import torch
import numpy as np
from src.utils.image_utils import load_image, save_image
from PIL import Image

class ImageProcessor:
    def __init__(self, model):
        self.model = model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def preprocess_image(self, image_path):
        """Prepare image for upscaling"""
        img = load_image(image_path)
        return torch.from_numpy(img).permute(2, 0, 1).float().div(255.).unsqueeze(0).to(self.device)
    
    def postprocess_image(self, tensor):
        """Convert output tensor to image"""
        output = tensor.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output, (1, 2, 0))
        output = (output * 255.0).round().astype(np.uint8)
        return output
    
    def upscale_image(self, image_path, scale_factor=4):
        """Upscale image using the loaded model"""
        input_tensor = self.preprocess_image(image_path)
        
        with torch.no_grad():
            output = self.model(input_tensor)
        
        output_image = self.postprocess_image(output)
        return Image.fromarray(output_image)