from manim import *

class Question(Scene):
    def construct(self):
        question = MathTex(r"\left| z \right| = ??")
        self.play(Write(question))