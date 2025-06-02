import os
import subprocess

def run_animation():
    # Change to the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run the Manim command
    cmd = ["python", "-m", "manim", "-pqh", "newton_first_law_with_audio.py", "NewtonFirstLaw"]
    subprocess.run(cmd)

if __name__ == "__main__":
    run_animation() 