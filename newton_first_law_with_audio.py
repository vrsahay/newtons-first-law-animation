from manim import *
from gtts import gTTS
import os
import random

# Generate audio narration
def generate_audio():
    script = """
    Newton's First Law of Motion: The Law of Inertia.

    An object at rest stays at rest. An object in motion stays in motion, unless acted upon by an external force.

    Here is a ball at rest. It will not move unless something pushes it.

    Now, an external force is applied. The ball moves forward.

    Watch as the ball moves forward with constant speed, just as Newton's First Law predicts.

    Let's see what happens in space, where there is almost no friction.

    In space, with almost no friction, a moving object would keep going forever.

    Now, let's summarize the key points of Newton's First Law.

    First point: Objects resist changes to their motion. This is what we call inertia.

    Second point: Only external forces can change an object's state, as we saw with the ball.

    This is Newton's First Law — the Law of Inertia, a fundamental principle of physics.
    """
    
    # Create audio directory if it doesn't exist
    if not os.path.exists("audio"):
        os.makedirs("audio")
    
    tts = gTTS(text=script)
    tts.save("audio/newton_first_law.mp3")
    print("Audio narration generated at audio/newton_first_law.mp3")

class NewtonFirstLaw(Scene):
    def construct(self):
        self.add_sound("audio/newton_first_law.mp3")
        self.camera.background_color = "#1a1a2e"
        gradient = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            stroke_width=0
        )
        gradient.set_color_by_gradient(["#1a1a2e", "#16213e", "#0f3460"])
        self.add(gradient)

        # 0-5s: Title
        title = Text("Newton's First Law of Motion", font_size=48).to_edge(UP)
        subtitle = Text("The Law of Inertia", font_size=36, color=YELLOW).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title, subtitle))
        self.wait(0.5)

        # 5-13s: Ball at rest
        ground = Rectangle(
            width=config.frame_width,
            height=1,
            fill_opacity=1,
            stroke_width=0
        ).to_edge(DOWN)
        ground.set_color_by_gradient(["#2c3e50", "#34495e"])
        self.play(Create(ground))
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1).set_stroke(WHITE, width=2)
        ball.move_to(LEFT * 4 + UP * 0.5)
        rest_label = Text("At Rest", font_size=32, color=WHITE).next_to(ball, DOWN, buff=0.3)
        self.play(Create(ball), Write(rest_label))
        self.wait(2)
        self.play(FadeOut(rest_label))
        self.wait(1)

        # 13-20s: External force
        force_arrow = Arrow(
            start=ball.get_right(),
            end=ball.get_right() + RIGHT * 2.5,
            color=RED,
            buff=0,
            stroke_width=8
        )
        force_label = Text("External Force", font_size=32, color=RED).next_to(force_arrow, UP, buff=0.3)
        self.play(Create(force_arrow), Write(force_label))
        self.wait(2)
        self.play(FadeOut(force_label, force_arrow))
        self.wait(1)

        # 20-30s: Ball moves (no friction)
        self.wait(1)  # Wait for narration to introduce ball movement
        self.play(ball.animate.shift(RIGHT * 5), run_time=4, rate_func=linear)
        self.wait(3)  # Wait after ball movement

        # 30-40s: Friction slows ball
        friction_arrow = Arrow(
            start=ball.get_center(),
            end=ball.get_center() + LEFT * 2.5,
            color=BLUE,
            buff=0,
            stroke_width=8
        )
        friction_label = Text("Friction", font_size=32, color=BLUE).next_to(friction_arrow, UP, buff=0.3)
        self.play(Create(friction_arrow), Write(friction_label))
        self.wait(1)
        self.play(ball.animate.shift(RIGHT * 2), run_time=2, rate_func=lambda t: t**2)
        self.wait(1)
        self.play(FadeOut(friction_arrow, friction_label, ball))
        self.wait(0.5)  # Wait before space scene

        # 40-48s: Space example
        space_bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            stroke_width=0,
            color=BLACK
        )
        stars = VGroup(*[Dot(
            point=[
                random.uniform(-config.frame_width/2, config.frame_width/2),
                random.uniform(-config.frame_height/2, config.frame_height/2),
                0
            ],
            radius=0.03,
            color=WHITE
        ) for _ in range(40)])
        space_ball = Circle(radius=0.5, color=YELLOW, fill_opacity=1).set_stroke(WHITE, width=2)
        space_ball.move_to(LEFT * 4)
        
        # Wait for space narration to begin
        self.wait(1)
        self.play(FadeIn(space_bg), FadeIn(stars), Create(space_ball), FadeOut(ground))
        self.wait(1)  # Wait for space scene setup
        self.play(space_ball.animate.shift(RIGHT * 8), run_time=5, rate_func=linear)
        self.wait(2)  # Wait after space animation
        self.play(FadeOut(space_bg), FadeOut(stars), FadeOut(space_ball))
        self.wait(1)  # Wait before summary

        # Create bullet points for summary
        bullet_points = VGroup(
            Text("• Objects resist changes to their motion", font_size=32, color=YELLOW),
            Text("• Only external forces can change an object's state", font_size=32, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 1.5)
        
        # Synchronize bullet points with narration
        for i, point in enumerate(bullet_points):
            self.play(
                Write(point),
                run_time=0.8
            )
            if i == 0:  # First point
                self.wait(2)  # Wait for first point
            elif i == 1:  # Second point
                self.wait(2)  # Wait for second point
        
        # Add final explanation with emphasis
        final_explanation = Text(
            "This is Newton's First Law — the Law of Inertia",
            font_size=36,
            color=WHITE
        ).next_to(bullet_points, DOWN, buff=0.7)
        
        self.wait(1)  # Wait before final explanation
        self.play(
            Write(final_explanation),
            run_time=1.5
        )
        
        # Add emphasis animation to the final explanation
        self.play(
            final_explanation.animate.scale(1.1).set_color(YELLOW),
            run_time=0.8
        )
        self.play(
            final_explanation.animate.scale(1/1.1).set_color(WHITE),
            run_time=0.8
        )
        
        self.wait(1)  # Final wait
        
        # Fade out everything with a smooth transition
        self.play(
            FadeOut(Group(bullet_points, final_explanation, gradient)),
            run_time=1.5
        )
        self.wait(0.5)

if __name__ == "__main__":
    # Generate audio first
    generate_audio() 