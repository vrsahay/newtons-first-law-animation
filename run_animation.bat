@echo off
cd /d "%~dp0"
python -m manim -pqh newton_first_law_with_audio.py NewtonFirstLaw
python run_with_audio.py
pause 