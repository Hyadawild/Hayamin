"""
Video processing utilities for Ayaya Upscaler
"""
from moviepy.editor import VideoFileClip, ImageSequenceClip
import cv2
import numpy as np
from pathlib import Path

def get_video_info(video_path):
    """Get video metadata"""
    clip = VideoFileClip(str(video_path))
    return {
        'duration': clip.duration,
        'fps': clip.fps,
        'size': clip.size
    }

def extract_frames(video_path):
    """Extract frames from video file"""
    clip = VideoFileClip(str(video_path))
    return list(clip.iter_frames())

def create_video_from_frames(frames, fps, output_path):
    """Create video from list of frames"""
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(str(output_path))
    return clip