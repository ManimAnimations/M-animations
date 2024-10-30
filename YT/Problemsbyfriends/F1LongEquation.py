from manim import *

class Introduction(Scene):
    def construct(self):
        sentence1 = Text("Let's try to solve my friend's long equation!",color=BLUE)
        self.play(Write(sentence1))
        self.wait(2)
        self.play(Unwrite(sentence1))

class Solution(Scene):
    def construct(self):
        #Developer's notes: This is going to be long... and good luck to you, manim and Andrei
        starting_equation = MathTex("109\left( 10+90+10 \right) \times 900 \div 80+190-30 \left( 20+5-\left( 80+40 \right) + 10 + 90 - 10 \right) \div2 \left( 109\times \left( 30 \times 2\div8 \right) +90 \right) \newline \times 300 \times 4 \times 5 \div 826 \left( 100\left( 8\times9000 \right)\left( 109\times90 \right) \right)+1000+300 \times 100\div2 \times 10 \div \left( 10 \times 90 \right) - 2 \newline \div 8 \left( 19 \div 8 -10 - 10 +  10 \div 10\right) \times10 +100 - 10 \times 10 \times 2 \div 346) = (5+4\div3+\left( 4+n-30-4 \right)+90-80)\newline \left( 30+10+60-10\div3 +4-5+6\div7+8-9\times10-11\div12\times14\div15\times16+17+18+19+20 \newline -30 + 40 +50 \times 10 \div 80 \times 10 + 10 \div 30 \times 90 - 10 + 1100 \div \newline 190100 -100  \times \left( -12 \right)) + 100 \times 200 \div 2000 \times 100 + 800 + 900 + 100 - 80 - 800 \div 900 + 100 - 100 + 10 \div 80 \times 10 - 80+10 \right) \newline -108 + 11111111111111111 - 11111111111111111 - 8 + 9 - 9 \times 9 \div 9 + 9 \div \frac{1}{2} + 12 \times 9")