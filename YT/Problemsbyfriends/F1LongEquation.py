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
        #Developer's notes: This is going to be long... and good luck to you, manim and Andrei
    
                # Define main starting_starting_equation_full of the equat

        starting_equation1_0 = MathTex("109 \\cdot (10 + 90 + 10) \\cdot 900 \\div 80 + 190 - 30 \\cdot (20 + 5 -(80 + 40)  ").scale(0.65)#1st Line:Done!
        starting_equation2_0 = MathTex("+ 10 + 90 - 10  ) + 10 + 90 - 10) \\div 2 \\cdot (109 \\cdot (30 \\cdot 2 \\div 8) + 90)").scale(0.65)#2nd Line:Done!
        starting_equation3_0 = MathTex(" \\cdot 300 \\cdot 4 \\cdot 5 \\div 826 \\cdot (100 \\cdot (8 \\cdot 9000 ) \\cdot (109 \\cdot 90)) + 1000 + 300 \\cdot").scale(0.65)#3rd Line:Done!
        starting_equation4_0 = MathTex(" 100 \\div 2 \\cdot 10 \\div (10 \\cdot 90) - 2 \\div 8 \\cdot (19 \\div 8 - 10 - 10 + 10 \\div 10) \\cdot 10").scale(0.65) #4th Line:Done!
        starting_equation5_0 = MathTex("+ 100 - 10 \\cdot 10 \\cdot 2 \\div 346 = (5 + 4 \\div 3 + (4 + n - 30 - 4) + 90 - 80)").scale(0.65)#5th Line: Done!
        
        # Define the equality part and subsequent segments
        starting_equation6_0 = MathTex("\\cdot (30 + 10 + 60 - 10 \\div 3 + 4 - 5 + 6 \\div 7 + 8 - 9 \\cdot 10) - 11 \\div 12 \\cdot 14  ").scale(0.65) #6th Line:Done!
        starting_equation7_0 = MathTex("\\div 15 \\cdot 16 + 17 + 18 + 19 + 20 - 30 + 40 + 50 \\cdot 10 \\div 80 \\cdot 10  + 10").scale(0.65)#7th Line:Done!
        starting_equation8_0 = MathTex(" \\div 30 \\cdot 90 - 10 1100 \\div 190100 - 100 \\cdot (-12)+ 100 \cdot 200 \\div 2000 \\cdot").scale(0.65)#8th line:Done!
        starting_equation9_0 = MathTex("100 +800 + 900 + 100 - 80 -800 \\div 90 +100 - 100 + 10 \\div 80 + 10 ").scale(0.65) #9th line: Done!
        starting_equation10_0 = MathTex("  - 80 + 10 - 108 + 111111111111111111 - 111111111111111111 - 8 + 9 - 10 ").scale(0.65)#10th line:Done!
        starting_equation11_0 =  MathTex("+ 0  - 9 \\div 8 \\cdot 9 - 9 \\cdot 9 \div 8 \\cdot 9 - 9 \\cdot 9 \\div 9 + 9 \\div \\frac{1}{2} + 12 \\cdot 9").scale(0.65)#11th Line: Done!

        # Create a VGroup for each equation part and align them to maximize length




        # Stack the lines of the equation vertically with space between each line
        starting_equation_full0 = VGroup(
            starting_equation1_0, starting_equation2_0, starting_equation3_0,
            starting_equation4_0, starting_equation5_0, starting_equation6_0,
            starting_equation7_0, starting_equation8_0, starting_equation9_0,
            starting_equation10_0, starting_equation11_0
        ).arrange(DOWN, buff=0.1)

        # Create a bounding rectangle around the equations
        rectanglesef0 = SurroundingRectangle(starting_equation_full0, color = WHITE, buff=0)
        rectanglesef0.width = config.frame_width


        # Create "Procedure" and "Number" texts
        procedure0 = Text("Procedure", font_size=30,color=BLUE)
        counter0 = Text("Number", font_size=30,color=RED)

        rectanglepro0 = SurroundingRectangle(procedure0, color = BLUE, buff=0)
        rectanglecou0 = SurroundingRectangle(counter0, color = RED, buff=0)

        # Position "Procedure" and "Number" texts below the bounding rectangle
        procedure0.next_to(rectanglesef0, DOWN, buff=0.5)
        counter0.next_to(procedure0, RIGHT, buff=1)



        # Group everything together
        full_layout = VGroup(rectanglesef0, starting_equation_full0, procedure0, counter0,rectanglepro0,rectanglecou0)

        # Move everything to the left edge
        full_layout.move_to(UL*0.5)

        # Add animations
        # Add everything to the scene individually to prevent tracking
        self.add(rectanglesef0, starting_equation_full0)
        self.add(procedure0, rectanglepro0)
        self.add(counter0, rectanglecou0)
        
        # Add animations for clarity
        self.play(Create(rectanglesef0))
        self.play(Write(starting_equation_full0))
        self.play(Write(procedure0), Create(rectanglepro0))
        self.play(Write(counter0), Create(rectanglecou0))
        self.wait(2)
        