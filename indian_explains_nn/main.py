from manim import *

class TestConfig(Scene):
    def construct(self):
        # This text will now automatically use "Virgil" because
        # it is set as the default in your manim.cfg
        test_text = Text("Success! This is in virgil!", color=BLACK, font="Virgil 3 YOFF")

        test_latex = MathTex(r"f(x) = x^2 + 2x + 1", color=BLACK, )

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # Group and arrange all objects vertically
        group = VGroup(test_text, test_latex, circle).arrange(DOWN, buff=0.8)

        # Animate the objects
        self.play(Write(test_text))
        self.play(Write(test_latex))
        self.play(Create(circle))
        self.wait(2)

