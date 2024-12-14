"""
File handling utilities for Ayaya Upscaler
"""
import os
from pathlib import Path
import tempfile
import shutil

def create_temp_directory():
    """Create a temporary directory and return its path"""
    return Path(tempfile.mkdtemp())

def ensure_directory_exists(directory_path):
    """Ensure a directory exists, create if it doesn't"""
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def get_model_directory():
    """Get the models directory path, create if it doesn't exist"""
    models_dir = Path('models')
    ensure_directory_exists(models_dir)
    return models_dir

def cleanup_temp_file(file_path):
    """Safely remove a temporary file"""
    try:
        Path(file_path).unlink(missing_ok=True)
    except Exception as e:
        print(f"Warning: Failed to cleanup temporary file {file_path}: {e}")

def cleanup_temp_directory(directory_path):
    """Safely remove a temporary directory and its contents"""
    try:
        shutil.rmtree(directory_path, ignore_errors=True)
    except Exception as e:
        print(f"Warning: Failed to cleanup temporary directory {directory_path}: {e}")