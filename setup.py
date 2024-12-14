from setuptools import setup, find_packages

setup(
    name="ayaya-upscaler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.13.0",
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "gradio>=3.50.0",
        "numpy>=1.24.0",
        "Pillow>=10.0.0",
        "opencv-python>=4.8.0",
        "basicsr>=1.4.2",
        "facexlib>=0.3.0",
        "gfpgan>=1.3.8",
        "moviepy>=1.0.3"
    ],
    python_requires=">=3.8",
)