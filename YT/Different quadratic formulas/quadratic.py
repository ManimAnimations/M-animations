from manim import *

class intro(Scene):
    def construct(self):
        text = Text("All quadratic formulas:",font_size=100)
        self.play(Write(text))
        self.wait(2)

    
