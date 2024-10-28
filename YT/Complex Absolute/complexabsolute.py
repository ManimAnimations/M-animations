from manim import *

class Question(Scene):
    def construct(self):
        question = MathTex(r"\left| z \right| = ??",font_size=150)
        self.play(Write(question))
        self.wait(2)

class Graph(Scene):
    def construct(self):
        # Step 1: Set up the Complex Plane with specific tick labels
        complex_plane = ComplexPlane(
            x_range=[-2, 2, 1],        # Real axis range with ticks every 1 unit
            y_range=[-2, 2, 1],        # Imaginary axis range with ticks every 1 unit
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "include_ticks": True,
                "stroke_color": GREY,
            },
        )

        # Step 2: Add custom labels similar to a calculator display
        # Real axis labels
        real_labels = VGroup(
            MathTex("-2", font_size=40).next_to(complex_plane.c2p(-2, 0), DOWN),
            MathTex("-1", font_size=40).next_to(complex_plane.c2p(-1, 0), DOWN),
            MathTex("0", font_size=40).next_to(complex_plane.c2p(0, 0), DOWN),
            MathTex("1", font_size=40).next_to(complex_plane.c2p(1, 0), DOWN),
            MathTex("2", font_size=40).next_to(complex_plane.c2p(2, 0), DOWN),
        )

        # Imaginary axis labels
        imaginary_labels = VGroup(
            MathTex("2i", font_size=40).next_to(complex_plane.c2p(0, 2), LEFT),
            MathTex("i", font_size=40).next_to(complex_plane.c2p(0, 1), LEFT),
            MathTex("-i", font_size=40).next_to(complex_plane.c2p(0, -1), LEFT),
            MathTex("-2i", font_size=40).next_to(complex_plane.c2p(0, -2), LEFT),
        )

        # Step 3: Display the Complex Plane and Custom Labels
        self.play(Create(complex_plane))
        self.play(FadeIn(real_labels), FadeIn(imaginary_labels))
        self.wait(2)