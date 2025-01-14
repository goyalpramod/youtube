from manim import *

class TextPositionalEncoding(Scene):
    def construct(self):
        text = Text("Positional Encoding", font_size=98)
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))
        
class TextWhyPositionalEncoding(Scene):
    def construct(self):
        text = Text("Why do we need Positional Encoding?")
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.shift(UP*3))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class TextHowToMakeAPositionalEncoder(Scene):
    def construct(self):
        text = Text("How to make a Positional Encoder?")
        text.shift(UP*3)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class TextDifferentPositionalEncoding(Scene):
    def construct(self):
        text = Text("Different Positional Encoding")
        text.shift(UP*3)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class WithoutPositionalEncoding(Scene):
    def construct(self):
        text = Text("Pramod loves to eat pizza")
        