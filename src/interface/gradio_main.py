import gradio as gr
from pathlib import Path
from src.utils.file_utils import create_temp_directory, cleanup_temp_directory
import os
import subprocess
from pathlib import Path
from PIL import Image

def upscale_image(image, model_name, scale, noise_reduction):
    model_param = f"/content/models/{model_name}.param"
    model_bin = f"/content/models/{model_name}.bin"
    output_file = "/content/output/upscaled_image.png"

    # Perintah untuk Real-ESRGAN NCNN
    command = f"./realesrgan-ncnn-vulkan -i {image} -o {output_file} -s {scale} -n {noise_reduction} -m {model_param} -b {model_bin}"
    os.system(command)

    return output_file


def upscale_video(video, model_name, scale, noise_reduction):
    video_path = video.name  # Mendapatkan path file sementara
    output_video = "/content/output/upscaled_video.mp4"

    # Contoh perintah upscale dengan FFmpeg (proses setiap frame bisa diganti dengan NCNN jika diperlukan)
    command = f"ffmpeg -i {video_path} -vf scale=iw*{scale}:ih*{scale} {output_video}"
    os.system(command)

    return output_video  

def get_available_models():
    return [f.stem for f in Path(MODEL_PATH).glob("*.param")]

with gr.Blocks() as demo:
    gr.Markdown("# Real-ESRGAN NCNN Image/Video Upscaler")

    model_selector = gr.Dropdown(choices=get_available_models(), label="Choose Model")
    scale_slider = gr.Slider(1, 4, step=1, label="Upscale Factor (1x-4x)")
    noise_slider = gr.Slider(0, 3, step=1, label="Noise Reduction Level (0-3)")

    with gr.Tab("Image"):
        image_input = gr.Image(type="filepath", label="Input Image")
        image_output = gr.Image(label="Upscaled Image")
        upscale_button = gr.Button("Upscale Image")

    with gr.Tab("Video"):
        video_input = gr.Video(label="Input Video")
        video_output = gr.Video(label="Upscaled Video")
        upscale_video_button = gr.Button("Upscale Video")

    upscale_button.click(upscale_image, [image_input, model_selector, scale_slider, noise_slider], image_output)
    upscale_video_button.click(upscale_video, [video_input, model_selector, scale_slider, noise_slider], video_output)

demo.launch()