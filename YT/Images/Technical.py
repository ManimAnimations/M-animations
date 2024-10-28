from manim import *

class Technical(Scene):
    def construct(self):
        technical = Text("Technical Difficulties", font_size = 100, color = RED)
        error = MathTex(r"-4058",font_size = 200)

        self.play(Write(technical))
        self.play(Write(error))