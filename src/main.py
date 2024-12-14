"""
Main entry point for Ayaya Upscaler
"""
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.models.model_loader import ModelLoader
from src.processors.image_processor import ImageProcessor
from src.processors.video_processor import VideoProcessor
from src.interface.gradio_ui import AyayaUI

def main():
    # Initialize model loader and load ESRGAN
    model_loader = ModelLoader()
    print(model_loader.check_gpu())
    model = model_loader.load_esrgan()
    
    # Initialize processors
    image_processor = ImageProcessor(model)
    video_processor = VideoProcessor(image_processor)
    
    # Create and launch Gradio interface
    ui = AyayaUI(image_processor, video_processor)
    interface = ui.create_interface()
    interface.launch(share=True)

if __name__ == "__main__":
    main()