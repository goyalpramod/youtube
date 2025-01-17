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
        unique_encoding_text = Text("Unique encoding").scale(0.5).to_corner(UL, buff=0.4) 
        
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
        
        # Create a copy of "Unique encoding" part that will remain
        linear_relation_text = Text("Linear relation").scale(0.5).next_to(unique_encoding_text,DOWN, buff=0.2, aligned_edge=LEFT) 
        
        # Animate the transition
        self.play(
            Transform(text_rule_2[:14], linear_relation_text),  # Transform "Unique encoding" to new position
            FadeOut(text_rule_2[14:]),  # Fade out the rest of the text
            run_time=1.5
        )

        self.wait(1)

        text_rule_3 = Text("Generalizes to longer sequences than those encountered in training", font_size=24).shift(ORIGIN)

        self.play(Write(text_rule_3))
        self.play(Wait(1))
        self.play(text_rule_3.animate.shift(UP*2))

        # First sequence (up to 256)
        words1 = ["The", "cat", "sat", "sleeps"]
        word_mobjects1 = VGroup(*[Text(word, font_size=24) for word in words1[:3]])
        word_mobjects1.arrange(RIGHT, buff=0.5)
        
        dots1 = Text("...", font_size=24).next_to(word_mobjects1, RIGHT, buff=0.3)
        last_word1 = Text(words1[-1], font_size=24).next_to(dots1, RIGHT, buff=0.3)
        
        sequence1 = VGroup(word_mobjects1, dots1, last_word1).move_to(ORIGIN)
        
        # Numbers for first sequence
        numbers1 = ["1", "2", "3", "256"]
        number_mobjects1 = VGroup(*[
            Text(num, font_size=24).next_to(word_mobjects1[i], DOWN, buff=0.3)
            for i, num in enumerate(numbers1[:3])
        ])
        last_number1 = Text(numbers1[-1], font_size=24).next_to(last_word1, DOWN, buff=0.3)
        
        # Animate first sequence
        self.play(Write(word_mobjects1))
        self.play(Write(dots1))
        self.play(Write(last_word1))
        self.play(Write(number_mobjects1))
        self.play(Write(last_number1))
        
        self.wait(3)
        
        # Second sequence (up to 1024)
        words2 = ["My", "dog", "runs", "fast"]
        word_mobjects2 = VGroup(*[Text(word, font_size=24) for word in words2[:3]])
        word_mobjects2.arrange(RIGHT, buff=0.5)
        
        dots2 = Text("...", font_size=24).next_to(word_mobjects2, RIGHT, buff=0.3)
        last_word2 = Text(words2[-1], font_size=24).next_to(dots2, RIGHT, buff=0.3)
        
        sequence2 = VGroup(word_mobjects2, dots2, last_word2).next_to(sequence1, DOWN, buff=1)
        
        # Numbers for second sequence
        numbers2 = ["1", "2", "3", "1024"]
        number_mobjects2 = VGroup(*[
            Text(num, font_size=24).next_to(word_mobjects2[i], DOWN, buff=0.3)
            for i, num in enumerate(numbers2[:3])
        ])
        last_number2 = Text(numbers2[-1], font_size=24).next_to(last_word2, DOWN, buff=0.3)
        
        # Animate second sequence
        self.play(Write(word_mobjects2))
        self.play(Write(dots2))
        self.play(Write(last_word2))
        self.play(Write(number_mobjects2))
        self.play(Write(last_number2))
        
        self.wait(3)
        
        # Create a copy of "Generalize" part that will remain
        generalize_text = Text("Generalize").scale(0.5).next_to(linear_relation_text, DOWN, buff=0.2, aligned_edge=LEFT)
        
        # Animate the transition
        self.play(
            Transform(text_rule_3[:10], generalize_text),  # Transform "Generalize" to new position
            FadeOut(text_rule_3[10:]),  # Fade out the rest of the text
            FadeOut(VGroup(
                word_mobjects1, dots1, last_word1, number_mobjects1, last_number1,
                word_mobjects2, dots2, last_word2, number_mobjects2, last_number2
            )),
            run_time=1.5
        )

        text_rule_4 = Text("Generated by a deterministic process the model can learn", font_size=24).shift(ORIGIN)
        self.play(Write(text_rule_4))
        self.play(text_rule_4.animate.shift(UP*2))
        
        # Create simple formula explanation
        formula_text = Text("Formula: position → 2 × position + 1", font_size=28).next_to(text_rule_4, DOWN, buff=1)
        self.play(Write(formula_text))
        self.wait(1)
        
        # Create sequence showing the pattern
        positions = ["Position 1", "Position 2", "Position 3", "Position 4"]
        formulas = ["2(1) + 1", "2(2) + 1", "2(3) + 1", "2(4) + 1"]
        results = ["= 3", "= 5", "= 7", "= 9"]  # Simple arithmetic sequence
        
        # Create three rows of text
        position_mobjects = VGroup(*[Text(pos, font_size=24) for pos in positions]).arrange(RIGHT, buff=1)
        formula_mobjects = VGroup(*[Text(val, font_size=24) for val in formulas])
        result_mobjects = VGroup(*[Text(res, font_size=24) for res in results])
        
        # Arrange formulas and results under positions
        for i in range(len(positions)):
            formula_mobjects[i].next_to(position_mobjects[i], DOWN, buff=0.3)
            result_mobjects[i].next_to(formula_mobjects[i], DOWN, buff=0.3)
        
        # Group everything for positioning
        entire_sequence = VGroup(position_mobjects, formula_mobjects, result_mobjects)
        entire_sequence.next_to(formula_text, DOWN, buff=1)
        
        # Animate
        self.play(Write(position_mobjects))
        self.wait(0.5)
        
        # Show calculation process one by one
        for i in range(len(positions)):
            self.play(Write(formula_mobjects[i]))
            arrow = Arrow(
                formula_mobjects[i].get_bottom(),
                result_mobjects[i].get_top(),
                buff=0.1,
                color=YELLOW
            )
            self.play(
                Create(arrow),
                Write(result_mobjects[i])
            )
            self.wait(0.5)
        
        self.wait(2)
        
        # Highlight the pattern
        pattern_text = Text("Notice: Each position maps to a unique, predictable value", font_size=24)
        pattern_text.next_to(entire_sequence, DOWN, buff=1)
        self.play(Write(pattern_text))
        
        self.wait(2)
        
        # Final transition to corner
        deterministic_text = Text("Deterministic").scale(0.5).next_to(generalize_text, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(
            Transform(text_rule_4[:12], deterministic_text),
            FadeOut(text_rule_4[12:]),
            FadeOut(VGroup(entire_sequence, formula_text, pattern_text)),
            run_time=1.5
        )

        text_rule_5 = Text("Extensible to multiple dimensions", font_size=24).shift(ORIGIN)
        self.play(Write(text_rule_5))
        self.play(text_rule_5.animate.shift(UP*2))

        # Create 1D sequence
        one_d_text = Text("1D (Sequence)", font_size=20).to_edge(LEFT).shift(UP)
        one_d_boxes = VGroup(*[
            Square(side_length=0.5, fill_opacity=0.3, fill_color=BLUE)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.2).next_to(one_d_text, RIGHT, buff=1)
        
        # Add position numbers for 1D
        one_d_numbers = VGroup(*[
            Text(f"{i+1}", font_size=16).move_to(box)
            for i, box in enumerate(one_d_boxes)
        ])

        self.play(
            Write(one_d_text),
            *[Create(box) for box in one_d_boxes],
            *[Write(num) for num in one_d_numbers]
        )
        self.wait(1)

        # Create 2D grid
        two_d_text = Text("2D (Image)", font_size=20).to_edge(LEFT)
        grid_size = 3
        two_d_grid = VGroup(*[
            VGroup(*[
                Square(side_length=0.5, fill_opacity=0.3, fill_color=GREEN)
                for _ in range(grid_size)
            ]).arrange(RIGHT, buff=0.2)
            for _ in range(grid_size)
        ]).arrange(DOWN, buff=0.2).next_to(two_d_text, RIGHT, buff=1)

        # Add position numbers for 2D
        two_d_numbers = VGroup(*[
            Text(f"({i+1},{j+1})", font_size=12).move_to(
                two_d_grid[i][j]
            )
            for i in range(grid_size)
            for j in range(grid_size)
        ])

        self.play(
            Write(two_d_text),
            *[Create(cell) for row in two_d_grid for cell in row],
            *[Write(num) for num in two_d_numbers]
        )
        self.wait(1)


        # Create corner text
        multidim_text = Text("Multi-dimensional").scale(0.5).next_to(
            deterministic_text, DOWN, buff=0.2, aligned_edge=LEFT
        )

        # Final transition
        self.play(
            Transform(text_rule_5[:22], multidim_text),
            FadeOut(text_rule_5[22:]),
            FadeOut(VGroup(
                one_d_text, one_d_boxes, one_d_numbers,
                two_d_text, two_d_grid, two_d_numbers,
            )),
            run_time=1.5
        )