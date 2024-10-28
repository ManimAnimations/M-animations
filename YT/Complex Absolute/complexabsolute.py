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
            x_range=[-7, 7, 1],        # Real axis range with ticks every 1 unit
            y_range=[-5, 5, 1],        # Imaginary axis range with ticks every 1 unit
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
            MathTex("-6", font_size=40).next_to(complex_plane.c2p(-6, 0), DOWN),
            MathTex("-5", font_size=40).next_to(complex_plane.c2p(-5, 0), DOWN),
            MathTex("-4", font_size=40).next_to(complex_plane.c2p(-4, 0), DOWN),
            MathTex("-3", font_size=40).next_to(complex_plane.c2p(-3, 0), DOWN),
            MathTex("-2", font_size=40).next_to(complex_plane.c2p(-2, 0), DOWN),
            MathTex("-1", font_size=40).next_to(complex_plane.c2p(-1, 0), DOWN),
            MathTex("0", font_size=40).next_to(complex_plane.c2p(0, 0), DOWN),
            MathTex("1", font_size=40).next_to(complex_plane.c2p(1, 0), DOWN),
            MathTex("2", font_size=40).next_to(complex_plane.c2p(2, 0), DOWN),
            MathTex("3", font_size=40).next_to(complex_plane.c2p(3, 0), DOWN),
            MathTex("4", font_size=40).next_to(complex_plane.c2p(4, 0), DOWN),
            MathTex("5", font_size=40).next_to(complex_plane.c2p(5, 0), DOWN),
            MathTex("6", font_size=40).next_to(complex_plane.c2p(6, 0), DOWN),
        )

        # Imaginary axis labels
        imaginary_labels = VGroup(
            MathTex("3i", font_size=40).next_to(complex_plane.c2p(0, 3), LEFT),
            MathTex("2i", font_size=40).next_to(complex_plane.c2p(0, 2), LEFT),
            MathTex("i", font_size=40).next_to(complex_plane.c2p(0, 1), LEFT),
            MathTex("-i", font_size=40).next_to(complex_plane.c2p(0, -1), LEFT),
            MathTex("-2i", font_size=40).next_to(complex_plane.c2p(0, -2), LEFT),
            MathTex("-3i", font_size=40).next_to(complex_plane.c2p(0, -3), LEFT)
        )

        # Step 3: Display the Complex Plane and Custom Labels
        self.play(Create(complex_plane))
        self.play(FadeIn(real_labels), FadeIn(imaginary_labels))
        self.wait(2)

        complex_number = 1 + 1j  # Change this to your desired point
        point_location = complex_plane.n2p(complex_number)
        point_label = "1 + i"  # Label for the point

        dot = Dot(point_location, color=YELLOW)
        label = MathTex(point_label, font_size=40, color=YELLOW).next_to(dot, RIGHT)

        # Step 6: Display the Point and Label
        self.play(FadeIn(dot), FadeIn(label))
        self.wait(2)

        dot_1_1 = 0+0j
        dot_2_1 = 1+0j

        # Create a line between these two points using the complex plane
        line_1 = Line(
            start=complex_plane.n2p(dot_1_1),  # convert complex number to point
            end=complex_plane.n2p(dot_2_1),    # convert complex number to point
            color=BLUE
        )
        
        # Add the line to the scene
        self.play(Create(line_1))
        self.wait(2)