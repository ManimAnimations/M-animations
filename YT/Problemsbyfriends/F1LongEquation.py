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
    
                # Define main starting_equations of the equat

        starting_equation1 = MathTex("109 \\cdot (10 + 90 + 10) \\cdot 900 \\div 80 + 190 - 30 \\cdot (20 + 5 -(80 + 40)  ")#1st Line:Done!
        starting_equation2 = MathTex("+ 10 + 90 - 10  ) + 10 + 90 - 10) \\div 2 \\cdot (109 \\cdot (30 \\cdot 2 \\div 8) + 90)")#2nd Line:Done!
        starting_equation3 = MathTex(" \\cdot 300 \\cdot 4 \\cdot 5 \\div 826 \\cdot (100 \\cdot (8 \\cdot 9000 ) \\cdot (109 \\cdot 90)) + 1000 + 300 \\cdot")#3rd Line:Done!
        starting_equation4 = MathTex(" 100 \\div 2 \\cdot 10 \\div (10 \\cdot 90) - 2 \\div 8 \\cdot (19 \\div 8 - 10 - 10 + 10 \\div 10) \\cdot 10") #4th Line:Done!
        starting_equation5 = MathTex("+ 100 - 10 \\cdot 10 \\cdot 2 \\div 346 = (5 + 4 \\div 3 + (4 + n - 30 - 4) + 90 - 80)")#5th Line: Done!
        
        # Define the equality part and subsequent segments
        starting_equation6 = MathTex("\\cdot (30 + 10 + 60 - 10 \\div 3 + 4 - 5 + 6 \\div 7 + 8 - 9 \\cdot 10) - 11 \\div 12 \\cdot 14  ") #6th Line:Done!
        starting_equation7 = MathTex("\\div 15 \\cdot 16 + 17 + 18 + 19 + 20 - 30 + 40 + 50 \\cdot 10 \\div 80 \\cdot 10  + 10")#7th Line:Done!
        starting_equation8 = MathTex(" \\div 30 \\cdot 90 - 10 1100 \\div 190100 - 100 \\cdot (-12)+ 100 \cdot 200 \\div 2000 \\cdot")#8th line:Done!
        starting_equation9 = MathTex("100 +800 + 900 + 100 - 80 -800 \\div 90 +100 - 100 + 10 \\div 80 + 10 ") #9th line: Done!
        starting_equation10 = MathTex("  - 80 + 10 - 108 + 111111111111111111 - 111111111111111111 - 8 + 9 - 10 ")#10th line:Done!
        starting_equation11 =  MathTex("+ 0  - 9 \\div 8 \\cdot 9 - 9 \\cdot 9 \div 8 \\cdot 9 - 9 \\cdot 9 \\div 9 + 9 \\div \\frac{1}{2} + 12 \\cdot 9")#11th Line: Done!

        # Create a VGroup for each equation part and align them to maximize length
        starting_equation_full = VGroup(
            starting_equation1, starting_equation2, starting_equation3,
            starting_equation4, starting_equation5, starting_equation6,
            starting_equation7, starting_equation8, starting_equation9,
            starting_equation10,starting_equation11
        ).arrange(DOWN, buff=0.2)  # Arrange all parts vertically

        self.play(Write(starting_equation_full))

        