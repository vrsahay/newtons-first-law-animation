# Newton's First Law Animation

This project uses Manim to create an animation demonstrating Newton's First Law of Motion with audio support.

## Prerequisites

Before running the animations, make sure you have the following installed:

1. Python 3.7 or higher
2. FFmpeg
3. Manim
4. Required Python packages

### Installation Steps

1. Install Python from [python.org](https://python.org)

2. Install FFmpeg:
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

3. Install Manim and dependencies:

pip install manim
pip install manim-voiceover


## Running the Animation

### High Quality Animation with Audio
To render the animation with high quality and audio:

manim -pqh newton_first_law_with_audio.py NewtonFirstLaw


This command:
- `-p`: Shows the preview window after rendering
- `-qh`: Renders in high quality (1080p, 60fps)
- `newton_first_law_with_audio.py`: The main animation file
- `NewtonFirstLaw`: The scene class name

### Quality Flags
- `-ql`: Low quality (480p, 15fps)
- `-qm`: Medium quality (720p, 30fps)
- `-qh`: High quality (1080p, 60fps)
- `-qk`: 4K quality (2160p, 60fps)

## Output

The rendered animations will be saved in the `media` directory:
- Video files: `media/videos/newton_first_law_with_audio/`
- Audio files: `media/audio/newton_first_law_with_audio/`

## Project Structure
```
newtons_first_law/
├── newton_first_law_with_audio.py    # Main animation file
├── README.md                         # This file
└── media/                           # Generated output directory
    ├── videos/
    └── audio/
```

## Tips

1. The `-p` flag will automatically open the preview window after rendering
2. Use `-qh` for high-quality final renders
3. Make sure your audio files are in a supported format (WAV, MP3)
4. Check the console output for any error messages during rendering

## Common Issues

1. If you get FFmpeg errors:
   - Verify FFmpeg is installed correctly
   - Check if FFmpeg is in your system PATH

2. If audio doesn't work:
   - Ensure audio files are in the correct format
   - Check audio file paths in your code
   - Verify audio file permissions

## Additional Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Voiceover Documentation](https://github.com/ManimCommunity/manim-voiceover)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html) 
