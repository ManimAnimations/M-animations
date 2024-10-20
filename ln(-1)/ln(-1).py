from manim import *

class LNMINUS1(Scene): #ln(-1) scene
    def construct(self):
        #ln(-1)
        question = MathTex(r"\ln\left(-1\right)=", font_size=150)
        question.move_to(LEFT*3) 

        self.play(Write(question))
        self.wait(2)

        #Possible?
        LABELP= Tex("Possible?", color=GREEN, font_size=150).next_to(question,RIGHT)

        self.play(Write(LABELP))
        self.wait(3)

        #Yes!
        Affirm = Tex("Yes!",color=GREEN,font_size=150).next_to(question,RIGHT+DOWN)

        self.play(FadeIn(Affirm))
        self.wait(4)

        self.play(FadeOut(question),FadeOut(LABELP),FadeOut(Affirm)) 

class SOLUTION(Scene): #solution scene
    def construct(self):
        #The Starting Equation
        startingequation = MathTex(r"\ln\left(-1\right)", font_size=150)
        self.play(Write(startingequation))

        equationex1 = MathTex(r"-1 = e^{i\pi}", color = GREEN)
        equationex1.move_to(UP*3,LEFT*2)
        self.play(Write(equationex1))

        #ln(e^iπ)
        equatione = MathTex(r"\ln", r"\left(", r"e^",r"{i\pi}", r"\right)", font_size=150)
        self.play(Transform(startingequation,equatione))

        self.play(Unwrite(equationex1))

        self.play(equatione[0][0:2].animate.set_color(RED),
                  equatione[2][0].animate.set_color(RED))

        #ln(e^x)=x
        equationex2 = MathTex(r"\ln\left( e^{x} \right) = x",color=BLUE)
        equationex2.move_to(UP * 3 + LEFT * 2)

        self.play(Write(equationex2))
        self.wait(1)

        self.play(Unwrite(equationex2))

        self.play(equatione[0][0:2].animate.set_color(WHITE), 
                  equatione[2][0].animate.set_color(WHITE)) 

        self.play(FadeToColor(equatione,color=BLACK)) # Fade out the entire equatione

        equationipi = MathTex(r"i\pi", font_size=150)
        equationipi.move_to(equatione)  # Position it where equatione was

        self.play(FadeIn(equationipi))

        self.wait(2)

        self.play(FadeOut(equationipi))

        finalequation = MathTex(r"\ln\left( -1 \right) = i\pi", font_size = 150)
        self.play(FadeIn(finalequation))

        self.wait(2)

class More(Scene):
    def construct(self):
        more = Tex("But Wait! There's more!", font_size=100, color=RED)

        self.play(FadeIn(more))
        self.wait(2)
        self.play(FadeOut(more))

class SOLUTIONn(Scene): #solution scene
    def construct(self):
        #The Starting Equation
        startingequation = MathTex(r"\ln\left(-n\right)", font_size=150)
        self.play(Write(startingequation))

        equationex1 = MathTex(r"\ln\left( ab \right) = \ln\left( a \right) + \ln\left( b \right)", color = GREEN)
        equationex1.move_to(UP*3,LEFT*2)
        self.play(Write(equationex1))

        #ln(e^iπ)
        equationplus1 = MathTex(r"\ln\left( n \right) + ",r"\ln\left( -1 \right)", font_size=150)
        self.play(Transform(startingequation,equationplus1))

        self.play(Unwrite(equationex1))

        self.play(equationplus1[1].animate.set_color(RED))

        #ln(e^x)=x
        equationex2 = MathTex(r"\ln\left(-1 \right) = i\pi",color=BLUE)
        equationex2.move_to(UP * 3 + LEFT * 2)

        self.play(Write(equationex2))
        self.wait(1)

        self.play(Unwrite(equationex2))

        self.play(equationplus1[1].animate.set_color(WHITE)) 

        self.play(FadeToColor(equationplus1, color=BLACK)) # Fade out the entire equatione

        equationipi = MathTex(r"\ln\left(n \right) +" , r"i\pi", font_size=150)
        equationipi.move_to(equationplus1)  # Position it where equatione was

        self.play(FadeIn(equationipi))

        self.wait(2)

        self.play(FadeOut(equationipi))

        finalequation = MathTex(r"\ln\left( -n \right) = \ln\left(n \right) + i\pi", font_size = 150)
        self.play(FadeIn(finalequation))

        self.wait(2)

class TFW(Scene):
    def construct(self):
        tyfw = Tex("Thanks for Watching!", font_size=100, color=BLUE)

        self.play(FadeIn(tyfw))
        self.wait(2)
        self.play(FadeOut(tyfw))