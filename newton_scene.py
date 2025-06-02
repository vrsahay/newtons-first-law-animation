from manim import *

class NewtonFirstLaw(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.wait(1) 