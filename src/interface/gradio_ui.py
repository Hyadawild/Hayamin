"""
Gradio interface components and handlers
"""
import gradio as gr
from pathlib import Path
from src.utils.file_utils import create_temp_directory, cleanup_temp_directory

class AyayaUI:
    def __init__(self, image_processor, video_processor):
        self.image_processor = image_processor
        self.video_processor = video_processor
        
    def upscale_image_handler(self, image_path, scale_factor):
        """Handle image upscaling through Gradio interface"""
        temp_dir = None
        try:
            temp_dir = create_temp_directory()
            result = self.image_processor.upscale_image(image_path, scale_factor)
            output_path = temp_dir / "upscaled_image.png"
            result.save(output_path)
            return str(output_path)
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            if temp_dir:
                cleanup_temp_directory(temp_dir)
    
    def upscale_video_handler(self, video_path, scale_factor):
        """Handle video upscaling through Gradio interface"""
        temp_dir = None
        try:
            temp_dir = create_temp_directory()
            result = self.video_processor.upscale_video(video_path, scale_factor)
            output_path = temp_dir / "upscaled_video.mp4"
            result.write_videofile(str(output_path))
            return str(output_path)
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            if temp_dir:
                cleanup_temp_directory(temp_dir)
    
    def create_interface(self):
        """Create Gradio interface"""
        with gr.Blocks(title="Ayaya Upscaler") as interface:
            gr.Markdown("# Ayaya Upscaler")
            gr.Markdown("Upload an image or video to upscale using AI")
            
            with gr.Tabs():
                with gr.TabItem("Image Upscaling"):
                    image_input = gr.File(label="Upload Image")
                    image_scale = gr.Slider(minimum=2, maximum=4, value=2, step=2, label="Scale Factor")
                    image_button = gr.Button("Upscale Image")
                    image_output = gr.Image(label="Upscaled Result")
                    
                    image_button.click(
                        fn=self.upscale_image_handler,
                        inputs=[image_input, image_scale],
                        outputs=image_output
                    )
                
                with gr.TabItem("Video Upscaling"):
                    video_input = gr.File(label="Upload Video")
                    video_scale = gr.Slider(minimum=2, maximum=4, value=2, step=2, label="Scale Factor")
                    video_button = gr.Button("Upscale Video")
                    video_output = gr.Video(label="Upscaled Result")
                    
                    video_button.click(
                        fn=self.upscale_video_handler,
                        inputs=[video_input, video_scale],
                        outputs=video_output
                    )
        
        return interface