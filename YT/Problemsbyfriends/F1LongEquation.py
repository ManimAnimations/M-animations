from manim import *

class Introduction(Scene):
    def construct(self):
        sentence1 = Text("Let's try to solve my friend's long equation!",color=BLUE)
        self.play(Write(sentence1))
        self.wait(2)
        self.play(Unwrite(sentence1))

class Legend(Scene):
    def construct(self):
        WhiteText = Text("White Text is for the equation")
        BlueText = Text("Blue text is for Describing the step",color=BLUE)
        RedText = Text("Red Text is the amount of operators",color=RED)

        WhiteText.next_to(BlueText,UP)
        RedText.next_to(BlueText,DOWN)

        self.play(Write(WhiteText))
        self.wait(1)
        self.play(Write(BlueText))
        self.wait(1)
        self.play(Write(RedText))
        self.wait(1)
        self.play(FadeOut(WhiteText,BlueText,RedText))

class Solution(Scene):
    def construct(self):
        # Developer's notes: This is going to be long... and good luck to you, manim and Andrei.

        # Define the main starting equation
        starting_equation1_0 = MathTex("109 \\cdot (10 + 90 + 10) \\cdot 900 \\div 80 + 190 - 30 \\cdot (20 + 5 -(80 + 40)  ").scale(0.65)
        starting_equation2_0 = MathTex("+ 10 + 90 - 10  )  \\div 2 \\cdot (109 \\cdot (30 \\cdot 2 \\div 8) + 90)").scale(0.65)
        starting_equation3_0 = MathTex(" \\cdot 300 \\cdot 4 \\cdot 5 \\div 826 \\cdot (100 \\cdot (8 \\cdot 9000 ) \\cdot (109 \\cdot 90)) + 1000 + 300 \\cdot").scale(0.65)
        starting_equation4_0 = MathTex(" 100 \\div 2 \\cdot 10 \\div (10 \\cdot 90) - 2 \\div 8 \\cdot (19 \\div 8 - 10 - 10 + 10 \\div 10) \\cdot 10").scale(0.65)
        starting_equation5_0 = MathTex("+ 100 - 10 \\cdot 10 \\cdot 2 \\div 346 = (5 + 4 \\div 3 + (4 + n - 30 - 4) + 90 - 80)").scale(0.65)
        starting_equation6_0 = MathTex("\\cdot (30 + 10 + 60 - 10 \\div 3 + 4 - 5 + 6 \\div 7 + 8 - 9 \\cdot 10) - 11 \\div 12 \\cdot 14").scale(0.65)
        starting_equation7_0 = MathTex("\\div 15 \\cdot 16 + 17 + 18 + 19 + 20 - 30 + 40 + 50 \\cdot 10 \\div 80 \\cdot 10  + 10").scale(0.65)
        starting_equation8_0 = MathTex(" \\div 30 \\cdot 90 - 10 1100 \\div 190100 - 100 \\cdot (-12)+ 100 \\cdot 200 \\div 2000 \\cdot").scale(0.65)
        starting_equation9_0 = MathTex("100 +800 + 900 + 100 - 80 -800 \\div 90 +100 - 100 + 10 \\div 80 + 10 ").scale(0.65)
        starting_equation10_0 = MathTex(" - 80 + 10 - 108 + 111111111111111111 - 111111111111111111 - 8 + 9 - 10 ").scale(0.65)
        starting_equation11_0 = MathTex("+ 0 - 9 \\div 8 \\cdot 9 - 9 \\cdot 9 \\div 8 \\cdot 9 - 9 \\cdot 9 \\div 9 + 9 \\div \\frac{1}{2} + 12 \\cdot 9").scale(0.65)

        # Stack the lines of the equation vertically with spacing
        starting_equation_full0 = VGroup(
            starting_equation1_0, starting_equation2_0, starting_equation3_0,
            starting_equation4_0, starting_equation5_0,starting_equation6_0,
            starting_equation7_0, starting_equation8_0, starting_equation9_0,
            starting_equation10_0, starting_equation11_0 
        ).arrange(DOWN, buff=0.15)

        sef_pos = LEFT*2 +DOWN*0.125

        # Move the equations slightly to the left for layout balance
        starting_equation_full0.move_to(sef_pos)

        # Create a bounding rectangle around the equations
        rectangleeq0 = RoundedRectangle(
            corner_radius=0.5,
            width=starting_equation_full0.width + 0.5,
            height=starting_equation_full0.height + 3,
            color=WHITE
        )
        rectangleeq0.surround(starting_equation_full0)

        # Create "Procedure" and "Number" texts
        procedure_text0 = Text("Look for initial \n cancellations", font_size=30, color=BLUE)
        counter_text0 = MathTex("0", font_size=100, color=RED)

        # Create procedure and counter boxes
        procedure_box = RoundedRectangle(
            corner_radius=0.15,
            color=BLUE,
            fill_opacity=0.1,
            width =config.frame_width / 4.8,
            height=config.frame_height / 2.3
        ).to_edge(UP)

        counter_box = RoundedRectangle(
            corner_radius=0.15,
            color=RED,
            fill_opacity=0.1,
            width =config.frame_width / 4.8,
            height=config.frame_height / 2.3
        ).to_edge(DOWN)

        # Align the text inside their respective boxes
        procedure_text0.move_to(procedure_box.get_center()+RIGHT*5.5+UP*0.5)
        counter_text0.move_to(counter_box.get_center()+RIGHT*5.5+DOWN*0.5)

        procedure_box.move_to(procedure_text0)
        counter_box.move_to(counter_text0)

        # |----------------------------------------------------------------------|
        # |                               |                                      |
        # |                               |                                      |
        # |                               |     Procedure                        |
        # |                               |                                      |
        # |          equation             |--------------------------------------|
        # |                               |                                      |
        # |                               |                                      |
        # |                               |        Count                         |
        # |                               |                                      |
        # |----------------------------------------------------------------------|

        # Animations
        self.play(Create(rectangleeq0))  # Rectangle around the equations
        self.play(Write(starting_equation_full0))  # Equation animation
        self.play(FadeIn(procedure_box), Write(procedure_text0))  # Procedure box and text
        self.play(FadeIn(counter_box), Write(counter_text0))  # Counter box and text
        self.wait(2)

        starting_equation10_1 = MathTex(" - 80 + 10 - 108  - 8 + 9 - 10 ").scale(0.65) 
        counter_text1 = MathTex("1", font_size=100, color=RED)

        starting_equation_full1 = VGroup(
            starting_equation1_0, starting_equation2_0, starting_equation3_0,
            starting_equation4_0, starting_equation5_0,starting_equation6_0,
            starting_equation7_0, starting_equation8_0, starting_equation9_0,
            starting_equation10_1, starting_equation11_0 
        ).arrange(DOWN, buff=0.15)

        starting_equation_full1.move_to(sef_pos)

        counter_text1.move_to(counter_box)

        starting_equation_full0.move_to(LEFT * 2 + DOWN * 0.125)

        self.play(Transform(starting_equation10_0,starting_equation10_1),Transform(counter_text0,counter_text1))
        self.wait(2)

        starting_equation10_2 = MathTex(" - 80 - 108  - 8 + 9 ").scale(0.65) 
        counter_text2 = MathTex("2", font_size=100, color=RED)

        starting_equation_full2 = VGroup(
            starting_equation1_0, starting_equation2_0, starting_equation3_0,
            starting_equation4_0, starting_equation5_0,starting_equation6_0,
            starting_equation7_0, starting_equation8_0, starting_equation9_0,
            starting_equation10_2, starting_equation11_0 
        ).arrange(DOWN, buff=0.15)

        starting_equation_full2.move_to(sef_pos)

        counter_text2.move_to(counter_box)

        starting_equation_full2.move_to(LEFT * 2 + DOWN * 0.125)

        self.play(Transform(starting_equation10_1,starting_equation10_2),FadeToColor(counter_text1,BLACK),Write(counter_text2))
        self.wait(5)

        starting_equation2_1 = MathTex(" 90  )  \\div 2 \\cdot (109 \\cdot (30 \\cdot 2 \\div 8) + 90)").scale(0.65)
        counter_text3 = MathTex("3", font_size=100, color=RED)

        starting_equation_full3 = VGroup(
            starting_equation1_0, starting_equation2_1, starting_equation3_0,
            starting_equation4_0, starting_equation5_0,starting_equation6_0,
            starting_equation7_0, starting_equation8_0, starting_equation9_0,
            starting_equation10_2, starting_equation11_0 
        ).arrange(DOWN, buff=0.15)

        starting_equation_full3.move_to(sef_pos)

        counter_text3.move_to(counter_box)

        starting_equation_full3.move_to(LEFT * 2 + DOWN * 0.125)

        self.play(Transform(starting_equation2_0,starting_equation2_1),Transform(counter_text2,counter_text3),FadeToColor(starting_equation_full2,BLACK),Write(starting_equation_full3) ) 
        self.wait(5)