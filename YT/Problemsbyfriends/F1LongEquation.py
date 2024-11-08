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

from manim import *

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
        ).arrange(DOWN, buff=0.15)


        starting_equation_full0.move_to(RIGHT*20+DOWN*0.125)

        # Create a bounding rectangle around the equations

        rectangleeq0 = RoundedRectangle(corner_radius=0.5, 

                                        width=starting_equation_full0.width+0.3,
                                        height=starting_equation_full0.height +3,   

                                        color= WHITE) 
        rectangleeq0.surround(starting_equation_full0)


        # Create "Procedure" and "Number" texts
        procedure0 = Text("Procedure", font_size=30,color=BLUE)
        counter0 = Text("Number", font_size=30,color=RED)

        procedure_box0 = RoundedRectangle(corner_radius=0.15, color=BLUE, fill_opacity=0.1, 
                                         width=procedure0.width + 0.3, 
                                         height=procedure0.height + 0.3)
        counter_box0 = RoundedRectangle(corner_radius=0.15, color=RED, fill_opacity=0.1, 
                                      width=counter0.width + 0.3, 
                                      height=counter0.height + 0.3)

        #|----------------------------------------------------------------------|
        #|                               |                                      |
        #|                               |                                      |
        #|                               |     Procedure                        |
        #|                               |                                      |
        #|          equation             |--------------------------------------|
        #|                               |                                      |
        #|                               |                                      |
        #|                               |        Count                         |
        #|                               |                                      |
        #|----------------------------------------------------------------------|



        # Define BL and BR correctly
        TR = UP * config.frame_height / 2 + RIGHT * config.frame_width / 2
        BR = DOWN * config.frame_height / 2 + RIGHT * config.frame_width / 2

        # Position text at corners
        procedure0.move_to(TR+RIGHT*7)  # Bottom-left corner
        counter0.move_to(BR+RIGHT*7)  # Bottom-right corner

        # Align boxes to corners
        procedure_box0.move_to(procedure0)  # Bottom-left corner
        counter_box0.move_to(counter0)  # Bottom-right corner

        # Group everything together
        full_layout = VGroup(rectangleeq0, starting_equation_full0, procedure0, counter0,procedure_box0,counter_box0)

        # Move everything to the left edge
        full_layout.align_to(LEFT)
        # Move the entire group to the left edge, the boxes should be positioned correctly now
        full_layout.move_to(LEFT*3)

        # Add animations
        # Add everything to the scene individually to prevent tracking
        
        
        # Add animations for clarity

        self.play(Create(rectangleeq0))
        self.play(Write(starting_equation_full0))
        self.play(FadeIn(procedure_box0), FadeIn(procedure0))
        self.play(FadeIn(counter_box0), FadeIn(counter0))

        self.wait(2)