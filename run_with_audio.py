import os
import subprocess
from moviepy.editor import VideoFileClip, AudioFileClip

def ensure_directory_exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def combine_audio_video():
    # Define paths
    video_path = os.path.join("media", "videos", "1080p60", "NewtonFirstLaw.mp4")
    audio_path = os.path.join("audio", "newton_first_law.mp3")
    output_path = os.path.join("media", "videos", "1080p60", "NewtonFirstLaw_WithAudio.mp4")
    
    # Ensure directories exist
    ensure_directory_exists(video_path)
    ensure_directory_exists(audio_path)
    ensure_directory_exists(output_path)
    
    # Check if audio file exists and is not empty
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        print(f"WARNING: Audio file '{audio_path}' is missing or empty. The final video will have no sound.")
        return
    print(f"Combining video '{video_path}' with audio '{audio_path}'...")
    try:
        # Load video and audio
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Combine video and audio
        final_video = video.set_audio(audio)
        
        # Write the result to a file
        final_video.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        # Close the clips
        video.close()
        audio.close()
        final_video.close()
        
        print(f"Successfully created video with audio at: {output_path}")
    except Exception as e:
        print(f"Error combining audio and video: {str(e)}")

if __name__ == "__main__":
    # Run the Manim animation first
    subprocess.run(["python", "-m", "manim", "-pqh", "newton_first_law_with_audio.py", "NewtonFirstLaw"])
    
    # Then combine with audio
    combine_audio_video() 