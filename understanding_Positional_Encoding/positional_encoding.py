from manim import *
import random 


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
        # Start with concatenated text
        initial_text = Text("Pramod loves to eat pizza")
        
        # Create separated words
        words = ["Pramod", "loves", "to", "eat", "pizza"]
        word_mobjects = VGroup(*[Text(word) for word in words])
        word_mobjects.arrange(RIGHT, buff=1)
        word_mobjects.shift(DOWN*2)
        
        # Create embedding squares for each word
        embedding_groups = VGroup(*[
            VGroup(*[
                Square(side_length=0.3, stroke_width=2)
                for _ in range(4)
            ]).arrange(RIGHT, buff=0)
            for _ in range(len(words))
        ])
        
        # Position embedding groups above each word
        for i, group in enumerate(embedding_groups):
            group.move_to(word_mobjects[i]).shift(UP * 1.5)
        
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
        encoder_box = Text("Encoder").move_to(UP * 3)
        encoder_rect = SurroundingRectangle(
            encoder_box,
            corner_radius=0.2,
            buff=0.3,
            color=YELLOW_B
        )
        
        # Create connections from embeddings to encoder
        connections = VGroup(*[
            Line(
                group.get_top(),
                encoder_rect.get_bottom(),
                stroke_width=5,
                color=PURPLE_A
            ).set_opacity(0.6)
            for group in embedding_groups
        ])
        
        # Create lines from word boxes to embeddings
        word_to_embedding_lines = VGroup(*[
            Line(
                boxes[i].get_top(),
                embedding_groups[i].get_bottom(),
                stroke_width=5,
                color=PURPLE_A
            ).set_opacity(0.6)
            for i in range(len(words))
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
        
        # Create embeddings and connect them to words
        self.play(
            Create(embedding_groups),
            run_time=1
        )
        self.play(Create(word_to_embedding_lines), run_time=1)
        
        # Show encoder and connect embeddings to it
        self.play(
            Write(encoder_box),
            Create(encoder_rect),
            run_time=1
        )
        
        self.play(FadeIn(connections), run_time=1.5)
        
        self.wait()
        # convert into embeddings then pass to encoder
        # after passing to the encoder, state 

        self.play(FadeOut(VGroup(word_mobjects, boxes, embedding_groups, connections, word_to_embedding_lines)))

        self.play(VGroup(encoder_box, encoder_rect).animate.shift(DOWN*3))

        text_pramod_pizza = Text("Pramod loves to eat pizza").shift(UP*2)
        text_pizza_pramod = Text("pizza loves to eat Pramod").shift(DOWN*2)

        self.play(Write(text_pramod_pizza), Write(text_pizza_pramod))

        self.wait(2)

        text_random = Text("to loves Pramod pizza eat").shift(ORIGIN)

        self.play(FadeOut(encoder_box, encoder_rect), FadeOut(text_pramod_pizza), FadeOut(text_pizza_pramod),)
        self.wait(2)
        self.play(Write(text_random))
        self.play( FadeOut(text_random))

class HowToMakeAPositionalEncoder(Scene):
    def construct(self):
        # Create text
        text = Text("How to make a Positional Encoder?")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        text_rule_1 = Text("Unique encoding for each position (across sequences)", font_size=24).shift(ORIGIN)
        """
        Each position needs a unique encoding that remains consistent regardless of sequence length
        a token at position 5 should have the same encoding whether the current sequence is of length 10 or 10,000.
        """

        self.play(Write(text_rule_1))
        self.play(text_rule_1.animate.shift(UP*2))
        self.wait(1)
        
        
        """
        for example lets say we encode each word with an integer
        """
# Create the sample text with words
        words = ["Pramod", "loves", "to", "eat", "pizza"]
        word_mobjects = VGroup(*[Text(word) for word in words])
        word_mobjects.arrange(RIGHT, buff=0.5)  # Add some space between words
        word_mobjects.move_to(ORIGIN)

        # Generate random numbers (4 digits) for each word
        random_numbers = [str(_) for _ in [7,1,3,9,5]]
        number_mobjects = VGroup(*[
            Text(num, font_size=36)  # Smaller font size for numbers
            .next_to(word_mobjects[i], DOWN, buff=0.5)  # Position below each word
            for i, num in enumerate(random_numbers)
        ])

        # Animate words and numbers
        self.play(FadeIn(word_mobjects))
        self.play(FadeIn(number_mobjects))

        self.wait(3)

        self.play(ReplacementTransform(number_mobjects[0], Text("5", font_size=36).next_to(word_mobjects[0], DOWN, buff=0.5)))

        self.wait(3)

        to_rect = SurroundingRectangle(
            word_mobjects[0],
            corner_radius=0.2,
            buff=0.3,
            color=YELLOW_B
        )

        pizza_rect = SurroundingRectangle(
            word_mobjects[4],
            corner_radius=0.2,
            buff=0.3,
            color=YELLOW_B
        )

        self.play(Create(to_rect), Create(pizza_rect))

        self.wait(3)

        """
        now whatever words will be present in these locations, will be treated to be in the same place
        """
        self.play(FadeOut(VGroup(word_mobjects, number_mobjects, to_rect, pizza_rect)))
        self.wait(1)
        # Create a copy of "Unique encoding" part that will remain
        unique_encoding_text = Text("Unique encoding").scale(0.5).to_corner(UL, buff=0.5) 
        
        # Animate the transition
        self.play(
            Transform(text_rule_1[:14], unique_encoding_text),  # Transform "Unique encoding" to new position
            FadeOut(text_rule_1[14:]),  # Fade out the rest of the text
            run_time=1.5
        )

        self.wait(1)

        text_rule_2 = Text("Linear relation between two encoded positions", font_size=24).shift(ORIGIN)
        self.play(Write(text_rule_2))
        """
        from the following sequence we can infer that value for eat will be
        """
        self.play(text_rule_2.animate.shift(UP*2))

        words = ["Pramod", "loves", "to", "eat", "pizza"]
        word_mobjects = VGroup(*[Text(word) for word in words])
        word_mobjects.arrange(RIGHT, buff=0.5)  # Add some space between words
        word_mobjects.move_to(ORIGIN)

        # Generate random numbers (4 digits) for each word
        random_numbers = [str(_) for _ in [7,1,3,9,5]]
        number_mobjects = VGroup(*[
            Text(num, font_size=36)  # Smaller font size for numbers
            .next_to(word_mobjects[i], DOWN, buff=0.5)  # Position below each word
            for i, num in enumerate(random_numbers)
        ])

        # Animate words and numbers
        self.play(FadeIn(word_mobjects))
        self.play(FadeIn(number_mobjects))

        self.wait(3)


        self.wait(3)

        to_rect = SurroundingRectangle(
            word_mobjects[2],
            corner_radius=0.2,
            buff=0.3,
            color=YELLOW_B
        )

        self.play(Create(to_rect), Create(pizza_rect))

        self.wait(3)

        """
        now whatever words will be present in these locations, will be treated to be in the same place
        """
        self.play(FadeOut(VGroup(word_mobjects, number_mobjects, to_rect, pizza_rect)))
        self.wait(1)