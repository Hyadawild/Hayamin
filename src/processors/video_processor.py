"""
Video processing functionality
"""
import cv2
from pathlib import Path
from src.utils.video_utils import extract_frames, create_video_from_frames, get_video_info
from src.utils.file_utils import create_temp_directory, cleanup_temp_directory

class VideoProcessor:
    def __init__(self, image_processor):
        self.image_processor = image_processor
        self.temp_dir = None
    
    def upscale_video(self, video_path, scale_factor=4):
        """Upscale video frame by frame"""
        try:
            self.temp_dir = create_temp_directory()
            video_info = get_video_info(video_path)
            frames = extract_frames(video_path)
            upscaled_frames = []
            
            for i, frame in enumerate(frames):
                frame_path = self.temp_dir / f"frame_{i}.png"
                cv2.imwrite(str(frame_path), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                
                upscaled_frame = self.image_processor.upscale_image(frame_path, scale_factor)
                upscaled_frames.append(np.array(upscaled_frame))
            
            return create_video_from_frames(upscaled_frames, video_info['fps'])
        
        finally:
            if self.temp_dir:
                cleanup_temp_directory(self.temp_dir)