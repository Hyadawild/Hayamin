import os
import gradio as gr


os.makedirs("output", exist_ok=True)
os.makedirs("models", exist_ok=True)

def get_available_models():
    model_files = [os.path.splitext(f)[0] for f in os.listdir("models") if f.endswith(".param")]
    return model_files




def upscale_image(image, model_name, scale, noise_reduction):
    model_param = f"models/{model_name}.param"
    model_bin = f"models/{model_name}.bin"
    output_file = "output/upscaled_image.png"

    # Debugging: Pastikan file ada
    if not os.path.exists(model_param) or not os.path.exists(model_bin):
        return f"Error: Model files not found for {model_name}"

    # Simpan gambar input
    input_image_path = "input_image.png"
    image.save(input_image_path)

    # Jalankan Real-ESRGAN
    command = f"./realesrgan-ncnn-vulkan -i {input_image_path} -o {output_file} -s {scale} -n {noise_reduction} -m {model_param} -b {model_bin}"
    result = os.system(command)

    if result != 0 or not os.path.exists(output_file):
        return "Error: Real-ESRGAN process failed. Check logs."

    return output_file

def upscale_video(video_path, model, scale, noise):
    output_path = "output/upscaled_video.mp4"
    os.makedirs("output", exist_ok=True)  

    ncnn_bin = "./Real-ESRGAN/ncnn-bin/realesrgan-ncnn-vulkan"
    command = [
        ncnn_bin,
        "-i", video_path,
        "-o", output_path,
        "-n", model,
        "-s", str(scale),
        "-g", str(noise)
    ]

    try:
        subprocess.run(command, check=True)
        return output_path  
    except subprocess.CalledProcessError as e:
        print("Error during upscaling:", e)
        return None

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Ayaya Upscale")
    
    model_selector = gr.Dropdown(choices=get_available_models(), label="Choose Model")
    scale_slider = gr.Slider(1, 4, step=1, label="Upscale Factor (1x-4x)")
    noise_slider = gr.Slider(0, 3, step=1, label="Noise Reduction Level (0-3)")

    with gr.Tab("Image"):
        image_input = gr.Image(type="pil", label="Input Image")
        image_output = gr.Image(label="Upscaled Image")
        upscale_button = gr.Button("Upscale Image")

    with gr.Tab("Video"):
        video_input = gr.Video(label="Input Video")
        video_output = gr.Video(label="Upscaled Video")
        upscale_video_button = gr.Button("Upscale Video")

    # Callback
    upscale_button.click(upscale_image, [image_input, model_selector, scale_slider, noise_slider], image_output)
    upscale_video_button.click(upscale_video, [video_input, model_selector, scale_slider, noise_slider], video_output)

demo.launch()