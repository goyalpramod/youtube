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

from manim import *

class WithoutPositionalEncoding(Scene):
    def construct(self):
        # Start with concatenated text
        initial_text = Text("Pramodlovestoeatpizza")
        
        # Create separated words
        words = ["Pramod", "loves", "to", "eat", "pizza"]
        word_mobjects = VGroup(*[Text(word) for word in words])
        word_mobjects.arrange(RIGHT, buff=0.3)
        
        # Create rounded rectangles around each word
        boxes = VGroup(*[
            SurroundingRectangle(
                word,
                corner_radius=0.2,
                buff=0.1,
                color=BLUE_B
            )
            for word in word_mobjects
        ])
        
        # Create encoder box
        encoder_box = Text("Encoder").move_to(UP * 2)
        encoder_rect = SurroundingRectangle(
            encoder_box,
            corner_radius=0.2,
            buff=0.3,
            color=YELLOW_B
        )
        
        # Create thinner straight connections
        connections = VGroup(*[
            Line(
                box.get_top(),
                encoder_rect.get_bottom(),
                stroke_width=3,  # Making lines thinner
                color=PURPLE_A
            ).set_opacity(0.6)
            for box in boxes
        ])
        
        # Animation sequence
        self.play(Write(initial_text))
        self.wait(0.5)
        
        self.play(
            TransformMatchingShapes(initial_text, word_mobjects),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(Create(boxes), run_time=1)
        self.wait(0.5)
        
        self.play(
            Write(encoder_box),
            Create(encoder_rect),
            run_time=1
        )
        
        self.play(Create(connections), run_time=1.5)
        
        self.wait()