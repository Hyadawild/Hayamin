# Ayaya Upscaler

An AI-powered image and video upscaling application using deep learning models. full features in [colab]([https://github.com/Linaqruf](https://colab.research.google.com/drive/1RFBZw4gEQdg4k3GgqnwiDe6uTZV5wd_Z?usp=sharing))

## Features

- Image upscaling up to 4K resolution
- Video upscaling with batch processing
- GPU acceleration support
- User-friendly Gradio interface
- Image restoration support
- image to image conversion support
- mergeable image creation support

## Requirements

- Python 3.8+
- directml (radeon or intel gpu support)
- 
- CUDA-capable GPU (optional but recommended)
- See requirements.txt for full dependencies

## Installation web interface

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

## Usage

1. Open the Gradio interface in your browser
2. Choose between image or video upscaling
3. Upload your file
4. Select the desired scale factor
5. Click the upscale button
6. Download the processed result

## GPU Support

The application automatically detects and uses available GPU resources. For optimal performance, using a CUDA-capable GPU is recommended.

### Installation

1. Clone repo

   ```bash
   git clone https://github.com/Hyadawild/Ayaya-Upscale.git
   cd Real-ESRGAN
   ```

1. Install dependent packages

   ```bash
   # Install basicsr - https://github.com/xinntao/BasicSR
   # We use BasicSR for both training and inference
   pip install basicsr
   # facexlib and gfpgan are for face enhancement
   pip install facexlib
   pip install gfpgan
   pip install -r requirements.txt
   python setup.py develop
   ```

---
