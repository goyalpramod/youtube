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
        initial_text = Text("Jack loves to eat pizza")
        
        # Create separated words
        words = ["Jack", "loves", "to", "eat", "pizza"]
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

        text_Jack_pizza = Text("Jack loves to eat pizza").shift(UP*2)
        text_pizza_Jack = Text("pizza loves to eat Jack").shift(DOWN*2)

        self.play(Write(text_Jack_pizza), Write(text_pizza_Jack))

        self.wait(2)

        text_random = Text("to loves Jack pizza eat").shift(ORIGIN)

        self.play(FadeOut(encoder_box, encoder_rect), FadeOut(text_Jack_pizza), FadeOut(text_pizza_Jack),)
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
        words = ["Jack", "loves", "to", "eat", "pizza"]
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

        words = ["Jack", "loves", "to", "eat", "pizza"]
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
                two_d_text, two_d_grid, two_d_numbers, arrow,
            )),
            run_time=1.5
        )
        all_properties = VGroup()
        # Collect all corner texts in a VGroup
        all_properties.add(
            unique_encoding_text,
            linear_relation_text,
            generalize_text,
            deterministic_text,
            multidim_text
        )

        # Combine the animations using a single .animate chain
        self.play(
            FadeOut(unique_encoding_text, linear_relation_text, generalize_text, deterministic_text, multidim_text),
            all_properties.animate.move_to(ORIGIN).scale(2),  # Scale by 2 to counter the initial 0.5
            run_time=2
        )        

        self.wait(3)

        # Final fadeout
        self.play(
            FadeOut(all_properties),
            run_time=1.5
        )

        self.wait(1)

class DifferentPositionalEncoding(Scene):
    def construct(self):
        integer_encoding = Text("Integer Encoding", font_size=48).shift(ORIGIN)

        self.play(Write(integer_encoding))
        self.wait(1)
        self.play(FadeOut(integer_encoding))

        # Create the sentence
        sentence = "Jack loves to eat pizza"
        text = Text(sentence, font_size=36).move_to(ORIGIN)
        self.wait(1)
        words = ["Jack", "loves", "to", "eat", "pizza"]
        word_starts = [0]  # Start positions of each word
        
        for i in range(len(words)-1):
            word_starts.append(word_starts[i] + len(words[i]) + 1)  # +1 for space

        word_mobjects = VGroup(*[
            Text(word, font_size=36) for word in words
        ]).arrange(RIGHT, buff=0.3)  # Arrange words horizontally with spacing
        word_mobjects.move_to(ORIGIN)

        # Create position numbers aligned with each word
        position_numbers = VGroup(*[
            Text(str(i+1), font_size=24) 
            for i in range(len(words))
        ])

        # Align each number with its corresponding word
        for number, word in zip(position_numbers, word_mobjects):
            number.move_to(word.get_top() + UP*0.3)

        # Animate everything
        self.play(Write(word_mobjects))
        self.wait(1)
        self.play(Write(position_numbers))
        self.wait(1)

        # Move everything up together
        self.play(
            word_mobjects.animate.shift(UP*2.5),
            position_numbers.animate.shift(UP*2.5)
        )

        # Color the word "loves" - fixed indexing
        self.play(
            word_mobjects[1].animate.set_color(YELLOW)
        )

        # Create embedding vector (8 boxes to represent the embedding)
        num_dimensions = 8
        embedding_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=GREEN
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)
        
        # Add random numbers inside boxes
        embedding_numbers = VGroup(*[
            Text(f"{random.uniform(-0.5, 0.5):.2f}", font_size=16)
            .move_to(box)
            for box in embedding_boxes
        ])
        
        embedding_group = VGroup(embedding_boxes, embedding_numbers)
        embedding_group.next_to(word_mobjects, DOWN, buff=1).align_to(word_mobjects[1], LEFT)
        embedding_text = Text("Embedding", font_size=24).next_to(embedding_group, LEFT, buff=0.5)
        
        self.play(
            Write(embedding_text),
            Create(embedding_boxes),
            Write(embedding_numbers)
        )
        self.wait(1)

        # Add position number (2 for "loves")
        position_text = Text("2", font_size=36).next_to(embedding_group, RIGHT*1.5, buff=0.5)
        self.play(Write(position_text))
        self.wait(1)

        # Create position boxes
        position_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=YELLOW
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)
        
        # Add "2" in each position box
        position_numbers = VGroup(*[
            Text("2", font_size=16).move_to(box)
            for box in position_boxes
        ])
        
        position_group = VGroup(position_boxes, position_numbers)
        position_group.next_to(position_text, RIGHT, buff=0.5)
        position_encoding_text = Text("Position Encoding", font_size=24).next_to(position_group, RIGHT, buff=0.5)
        
        self.play(
            Write(position_encoding_text),
            ReplacementTransform(position_text, position_group)
        )
        
        self.wait(2)

        # Modified addition animation
        plus_sign = Text("+", font_size=36).move_to(
            (embedding_group.get_right() + position_group.get_left()) / 2
        )
        
        self.play(Write(plus_sign))
        self.wait(1)

        # Create final sum boxes
        sum_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=BLUE
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)

        # Calculate sum numbers
        sum_numbers = VGroup(*[
            Text(
                f"{float(embedding_numbers[i].text) + float(position_numbers[i].text):.2f}",
                font_size=16
            ).move_to(box)
            for i, box in enumerate(sum_boxes)
        ])

        sum_group = VGroup(sum_boxes, sum_numbers)
        sum_group.move_to(
            (embedding_group.get_center() + position_group.get_center()) / 2
        )
        
        final_encoding_text = Text("Final Encoding", font_size=24).next_to(sum_group, RIGHT, buff=0.5)

        # New animation sequence
        self.play(
            FadeIn(plus_sign),
        )
        self.wait(1)
        
        self.play(
            FadeOut(embedding_text, position_encoding_text),
        )
        self.wait(1)
        self.play(
            FadeOut(plus_sign),
            ReplacementTransform(embedding_group, sum_group),
            ReplacementTransform(position_group, sum_group),
        )
        self.play(
        Write(final_encoding_text)
        )       
        self.wait(2)

class DifferentPositionalEncoding2(Scene):
    def construct(self):
        # Create the sentence
        sentence = "... Joe has the best ..."
        text = Text(sentence, font_size=36).move_to(ORIGIN)
        self.wait(1)
        words = ["...","Joe", "has", "the", "best", "pizza", "..."]
        word_starts = [0]  # Start positions of each word
        
        for i in range(len(words)-1):
            word_starts.append(word_starts[i] + len(words[i]) + 1)  # +1 for space

        word_mobjects = VGroup(*[
            Text(word, font_size=36) for word in words
        ]).arrange(RIGHT, buff=0.3)  # Arrange words horizontally with spacing
        word_mobjects.move_to(ORIGIN)

        # Create position numbers aligned with each word
        position_numbers = VGroup(*[
            Text(str(pos), font_size=24) 
            for pos in range(253, 258)
        ])

        # Align each number with its corresponding word
        for number, word in zip(position_numbers, word_mobjects[1:6]):
            number.move_to(word.get_top() + UP*0.3)

        # Animate everything
        self.play(Write(word_mobjects))
        self.wait(1)
        self.play(Write(position_numbers))
        self.wait(1)

        # Move everything up together
        self.play(
            word_mobjects.animate.shift(UP*2.5),
            position_numbers.animate.shift(UP*2.5)
        )

        # Color the word "Joe"
        self.play(
            word_mobjects[1].animate.set_color(YELLOW)
        )

        # Create embedding vector (8 boxes to represent the embedding)
        num_dimensions = 8
        embedding_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=GREEN
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)
        
        # Add random numbers inside boxes
        embedding_numbers = VGroup(*[
            Text(f"{random.uniform(-0.5, 0.5):.2f}", font_size=16)
            .move_to(box)
            for box in embedding_boxes
        ])
        
        embedding_group = VGroup(embedding_boxes, embedding_numbers)
        embedding_group.next_to(word_mobjects, DOWN, buff=1).align_to(word_mobjects[0], LEFT)
        embedding_text = Text("Embedding", font_size=24).next_to(embedding_group, LEFT, buff=0.5)
        
        self.play(
            Write(embedding_text),
            Create(embedding_boxes),
            Write(embedding_numbers)
        )
        self.wait(1)

        # Add position number (253 for "Joe")
        position_text = Text("253", font_size=36).next_to(embedding_group, RIGHT*1.5, buff=0.5)
        self.play(Write(position_text))
        self.wait(1)

        # Create position boxes
        position_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=YELLOW
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)
        
        # Add "253" in each position box
        position_numbers = VGroup(*[
            Text("253", font_size=16).move_to(box)
            for box in position_boxes
        ])
        
        position_group = VGroup(position_boxes, position_numbers)
        position_group.next_to(position_text, RIGHT, buff=0.5)
        position_encoding_text = Text("Position Encoding", font_size=24).next_to(position_group, RIGHT, buff=0.5)
        
        self.play(
            Write(position_encoding_text),
            ReplacementTransform(position_text, position_group)
        )
        
        self.wait(2)

        # Modified addition animation
        plus_sign = Text("+", font_size=36).move_to(
            (embedding_group.get_right() + position_group.get_left()) / 2
        )
        
        # Create final sum boxes
        sum_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=BLUE
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)

        # Calculate sum numbers
        sum_numbers = VGroup(*[
            Text(
                f"{float(embedding_numbers[i].text) + 253:.2f}",
                font_size=16
            ).move_to(box)
            for i, box in enumerate(sum_boxes)
        ])

        sum_group = VGroup(sum_boxes, sum_numbers)
        sum_group.move_to(
            (embedding_group.get_center() + position_group.get_center()) / 2
        )
        
        final_encoding_text = Text("Final Encoding", font_size=24).next_to(sum_group, RIGHT, buff=0.5)

        # New animation sequence
        self.play(
            FadeIn(plus_sign),
        )
        self.wait(1)
        
        self.play(
            FadeOut(embedding_text, position_encoding_text),
        )
        self.wait(1)
        self.play(
            FadeOut(plus_sign),
            ReplacementTransform(embedding_group, sum_group),
            ReplacementTransform(position_group, sum_group),
        )
        self.play(
            Write(final_encoding_text)
        )
        
        self.wait(2)

class SinusoidalEncoding(Scene):
    def construct(self):
        # Create the title
        sine_encoding = Text("Sinusoidal Encoding", font_size=48).shift(ORIGIN)
        self.play(Write(sine_encoding), run_time=3)
        
        # Move title up to make space for equations
        self.play(sine_encoding.animate.shift(UP * 3))
        
        # Create equations as a single MathTex object with parts we want to isolate
        eq1 = MathTex(
            r"\text{PE}(",
            r"\text{pos}",
            r",",
            r"2i",
            r") = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)"
        ).shift(UP)
        
        eq2 = MathTex(
            r"\text{PE}(",
            r"\text{pos}",
            r",",
            r"2i+1",
            r") = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)"
        ).shift(ORIGIN)
        
        # Display equations
        self.play(Write(eq1), run_time=2)
        self.play(Write(eq2), run_time=2)
        
        # Create explanation texts
        explanations = VGroup(
            Text("pos = position of the token in the sequence", font_size=24),
            Text("i = dimension index (ranges from 0 to d_model/2)", font_size=24),
            Text("d_model = dimension of the embedding vector", font_size=24),
            Text("10000 = scaling factor to control frequency variation", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(DOWN * 2.5)
        
        # Use index-based highlighting for precise control
        # Highlight pos
        self.play(eq1[1].animate.set_color(YELLOW))
        self.play(Write(explanations[0]))
        self.wait(1)
        self.play(eq1[1].animate.set_color(WHITE))
        
        # Highlight 2i
        self.play(eq1[3].animate.set_color(YELLOW))
        self.play(Write(explanations[1]))
        self.wait(1)
        self.play(eq1[3].animate.set_color(WHITE))
        
        # Show d_model explanation
        self.play(Write(explanations[2]))
        self.wait(1)
        
        # Show scaling factor explanation
        self.play(Write(explanations[3]))
        self.wait(2)

        self.play(FadeOut(VGroup(eq1, eq2, explanations, sine_encoding)))

        # Write the simplified equation
        simple_eq = MathTex(r"PE(pos) = \sin(pos)").move_to(UP * 3.5)
        self.play(Write(simple_eq))
        
        # Create the axes
        axes = Axes(
            x_range=[0, 10, 2],  # From 0 to 10 with step size 2
            y_range=[-1, 1, 0.5],  # From -1 to 1 with step size 0.5
            tips=False,
            axis_config={"color": WHITE}
        ).scale(0.8)
        
        # Create the sine graph
        sine_graph = axes.plot(
            lambda x: np.sin(x),
            color=BLUE
        )
        
        # Create dots for specific positions
        dots = VGroup()
        dot_values = [0, 2, 4, 6, 8]  # x positions for markers
        
        for x in dot_values:
            y = np.sin(x)
            dot = Dot(axes.coords_to_point(x, y), color=YELLOW)
            # Add label showing position and value
            label = MathTex(
                r"\begin{array}{c}" + 
                f"pos={x}" + r"\\" +  # \\ creates a new line in array environment
                f"PE(pos) = {y:.2f}" + 
                r"\end{array}"
            ).scale(0.5)
            label.next_to(dot, UP)
            dots.add(VGroup(dot, label))
        
        # Play animations
        self.play(
            Create(axes),
            run_time=1
        )
        self.play(
            Create(sine_graph),
            run_time=2
        )
        self.play(
            AnimationGroup(
                *[GrowFromCenter(dot) for dot in dots],
                lag_ratio=0.3
            )
        )
        
        self.wait(2)


        words = ["Jack", "loves", "to", "eat", "pizza"]
        word_starts = [0]  # Start positions of each word
        
        for i in range(len(words)-1):
            word_starts.append(word_starts[i] + len(words[i]) + 1)  # +1 for space

        word_mobjects = VGroup(*[
            Text(word, font_size=36) for word in words
        ]).arrange(RIGHT, buff=0.3)  # Arrange words horizontally with spacing
        word_mobjects.move_to(DOWN*3.25)

        # Create position numbers aligned with each word
        position_numbers = VGroup(*[
            Text(str(i+1), font_size=24) 
            for i in range(len(words))
        ])

        # Align each number with its corresponding word
        for number, word in zip(position_numbers, word_mobjects):
            number.move_to(word.get_top() + UP*0.3)

        # Animate everything
        self.play(Write(word_mobjects), Write(position_numbers))
        self.wait(1)
        self.play(FadeOut(position_numbers, VGroup(simple_eq, axes, sine_graph, dots)))

        self.play(word_mobjects.animate.move_to(UP*2.5))
        # Color the word "Joe"
        self.play(
            word_mobjects[0].animate.set_color(YELLOW)
        )

        # Create embedding vector (8 boxes to represent the embedding)
        num_dimensions = 8
        embedding_boxes = VGroup(*[
            Square(
                side_length=0.6,
                fill_opacity=0.3,
                fill_color=GREEN
            ).set_stroke(WHITE, 2)
            for _ in range(num_dimensions)
        ]).arrange(DOWN, buff=0)
        
        # Add random numbers inside boxes
        embedding_numbers = VGroup(*[
            Text(f"{random.uniform(-0.5, 0.5):.2f}", font_size=16)
            .move_to(box)
            for box in embedding_boxes
        ])
        
        embedding_group = VGroup(embedding_boxes, embedding_numbers)
        embedding_group.next_to(word_mobjects, DOWN, buff=1).align_to(word_mobjects[0], LEFT)
        embedding_text = Text("Embedding", font_size=24).next_to(embedding_group, LEFT, buff=0.5)
        
        self.play(
            Write(embedding_text),
            Create(embedding_boxes),
            Write(embedding_numbers)
        )
        self.wait(1)

        # Create an arrow that will point to each box
        pointer_arrow = Arrow(
            start=embedding_group.get_right() + RIGHT,
            end=embedding_boxes[0].get_right(),
            color=YELLOW,
            buff=0.2
        )
        i_values_group = VGroup()  # Add this before the for loop
        # Create i value text template
        i_text = MathTex("i=", font_size=24)

        # Animate arrow moving to each box with corresponding i value
        for i in range(num_dimensions):
            # Create the specific i value for this iteration
            current_i = MathTex(str(i), font_size=24)
            i_value = VGroup(i_text.copy(), current_i)
            i_value.arrange(RIGHT, buff=0.1)
            i_value.next_to(embedding_boxes[i], RIGHT, buff=1)
            i_values_group.add(i_value) 

            if i == 0:
                # First position - create arrow and first i value
                self.play(
                    Create(pointer_arrow),
                    Write(i_value)
                )
            else:
                # Move arrow to next box and show new i value
                new_arrow = Arrow(
                    start=embedding_group.get_right() + RIGHT,
                    end=embedding_boxes[i].get_right(),
                    color=YELLOW,
                    buff=0.2
                )
                self.play(
                    Transform(pointer_arrow, new_arrow),
                    Write(i_value)
                )
            
            self.wait(0.5)

        self.wait(1)

        eq1.shift(RIGHT*3 + DOWN*2).scale(0.8)
        self.play(Write(eq1))

        self.wait(1)
        self.play(FadeOut(VGroup(embedding_text, embedding_group, pointer_arrow, word_mobjects, eq1, i_values_group)))
        self.wait(1)

        # Create axes with adjusted dimensions and no bottom axis
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 4, 1],
            axis_config={
                "color": WHITE,
                "include_numbers": False,
                "include_ticks": False  # Hide ticks
            },
            x_length=10,
            y_length=3,
        ).move_to(ORIGIN + UP)

        # Remove the bottom axis line
        axes.get_x_axis().set_opacity(0)

        def get_pe_function(dim, is_sine, offset):
            def pe_function(x):
                frequency = 1 / (2 ** (dim))
                amplitude = 0.5
                if is_sine:
                    return amplitude * np.sin(x * frequency) + offset
                else:
                    return amplitude * np.cos(x * frequency) + offset
            return pe_function

        # Create graphs with proper spacing
        graphs = VGroup()
        labels = VGroup()
        points_group = VGroup()

        # Configuration for the waves
        wave_configs = [
            (0, True, "i=0", BLUE, "sin"),    # i=0 sine
            (0, False, "i=0", RED, "cos"),    # i=0 cosine
            (1, True, "i=1", BLUE, "sin"),    # i=1 sine
            (2, True, "i=1", RED, "cos"),    # i=1 cos
        ]

        # Add equations on the right
        equations = VGroup(
            MathTex(r"PE(pos,2i) = \sin(\frac{pos}{10000^{2i/d}})", color=BLUE),
            MathTex(r"PE(pos,2i+1) = \cos(\frac{pos}{10000^{2i/d}})", color=RED)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(DOWN*2)

        # Create each wave
        for i, (dim, is_sine, label_text, color, trig_type) in enumerate(wave_configs):
            offset = 3 - i
            wave_function = get_pe_function(dim, is_sine, offset)
            wave = axes.plot(
                wave_function,
                x_range=[0, 20],
                color=color,
            )
            
            # Add dimension label
            label = MathTex(label_text, font_size=24)
            label.next_to(axes.c2p(0, offset), LEFT)
            
            # Add points for pos=1 and pos=4
            for pos in [1, 6]:
                point = Dot(axes.c2p(pos, wave_function(pos)), color=color)
                value = DecimalNumber(
                    wave_function(pos),
                    num_decimal_places=2,
                    include_sign=True,
                    font_size=20
                ).next_to(point, RIGHT, buff=0.1)
                value.add_background_rectangle(opacity=0.8, buff=0.1)
                points_group.add(VGroup(point, value))
            
            graphs.add(wave)
            labels.add(label)

        # Add title
        title = Text("Positional Encoding Components", font_size=32).next_to(axes, UP, buff=0.3)

        # Add label for position markers
        pos_labels = VGroup(
            Text("pos=1", font_size=24),
            Text("pos=6", font_size=24)
        )
        pos_labels[0].next_to(axes.c2p(1, 0), DOWN)
        pos_labels[1].next_to(axes.c2p(6, 0), DOWN)

        # Animate everything
        self.play(Create(axes))
        self.play(Write(title))

        # Animate graphs and labels one at a time
        for i in range(len(graphs)):
            self.play(
                Create(graphs[i]),
                Write(labels[i]),
                run_time=1
            )
            self.wait(0.3)

        # Show equations
        self.play(Write(equations))

        # Show position markers and values
        self.play(
            Write(pos_labels),
            *[GrowFromCenter(point) for point in points_group],
            run_time=1.5
        )

        self.wait(2)
        self.play(FadeOut(VGroup(axes, title, graphs, labels, equations, pos_labels, points_group)))

class ProofForSinusoidalEncoding(Scene):
    def construct(self):
        # Title
        title = Text("Proof: Sinusoidal Encoding Transformation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Initial equation showing what we want to prove
        initial_eq = MathTex(
            r"M \cdot \begin{bmatrix} \sin(\omega_i p) \\ \cos(\omega_i p) \end{bmatrix} = \begin{bmatrix} \sin(\omega_i(p+k)) \\ \cos(\omega_i(p+k)) \end{bmatrix}"
        ).scale(0.8)
        
        # Frequency definition
        freq_def = MathTex(
            r"\omega_i = \frac{1}{10000^{2i/d}}"
        ).scale(0.8)
        
        # Display initial equation and frequency definition
        VGroup(initial_eq, freq_def).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=1)
        self.play(Write(initial_eq))
        self.play(Write(freq_def))
        self.wait(2)
        
        # Fade out frequency definition to make space
        self.play(FadeOut(freq_def))
        
        # Move initial equation up
        self.play(initial_eq.animate.to_edge(UP, buff=1))
        
        # Show the transformation matrix with unknowns
        matrix_eq = MathTex(
            r"\begin{bmatrix} u_1 & v_1 \\ u_2 & v_2 \end{bmatrix}",
            r"\cdot",
            r"\begin{bmatrix} \sin(\omega_i p) \\ \cos(\omega_i p) \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} \sin(\omega_i(p+k)) \\ \cos(\omega_i(p+k)) \end{bmatrix}"
        ).scale(0.8)
        
        # Position the matrix equation
        matrix_eq.next_to(initial_eq, DOWN, buff=1)
        self.play(Write(matrix_eq))
        self.wait(2)
        
        # Show trigonometric expansion
        # Show trigonometric expansion 
        trig_expansion = MathTex(
            r"= \begin{bmatrix} \sin(\omega_i p)\cos(\omega_i k) + \cos(\omega_i p)\sin(\omega_i k) \\ \cos(\omega_i p)\cos(\omega_i k) - \sin(\omega_i p)\sin(\omega_i k) \end{bmatrix}"
        ).scale(0.7)

        trig_expansion.next_to(matrix_eq, DOWN, buff=0.5)
        self.play(Write(trig_expansion))
        self.wait(2)
        
        # Create system of equations
        system = MathTex(
            r"u_1\sin(\omega_i p) + v_1\cos(\omega_i p) &= \cos(\omega_i k)\sin(\omega_i p) + \sin(\omega_i k)\cos(\omega_i p) \\",
            r"u_2\sin(\omega_i p) + v_2\cos(\omega_i p) &= -\sin(\omega_i k)\sin(\omega_i p) + \cos(\omega_i k)\cos(\omega_i p)"
        ).scale(0.7)
        
        # Show the system of equations
        self.play(FadeOut(VGroup(matrix_eq, trig_expansion)))
        system.next_to(initial_eq, DOWN, buff=1)
        self.play(Write(system))
        self.wait(2)
        
        # Show final transformation matrix
        final_matrix = MathTex(
            r"M_k",                                   # [0]
            r"=",                                     # [1]
            r"\begin{bmatrix} \cos(\omega_i k) & \sin(\omega_i k) \\ -\sin(\omega_i k) & \cos(\omega_i k) \end{bmatrix}"  # [2]
        ).scale(0.8)

        # Create highlighting rectangles for specific parts of the matrix
        # We'll modify the highlighting to work with this structure
        highlights = VGroup()
        matrix = final_matrix[2]  # Get the matrix part

        # Add the matrix to scene first
        self.play(Write(final_matrix))
        self.wait(1)

        # Then create and animate highlights one by one
        for pos in [(0,0), (0,1), (1,0), (1,1)]:  # Positions in matrix to highlight
            highlight = SurroundingRectangle(matrix, color=YELLOW)
            highlights.add(highlight)
            self.play(
                Create(highlight),
                run_time=0.5
            )
            self.wait(0.5)
            self.play(FadeOut(highlight))
        
        # Create a box around the final result
        final_box = SurroundingRectangle(final_matrix, color=BLUE)
        self.play(Create(final_box))
        
        # Add a conclusion text
        conclusion = Text(
            "This rotation matrix allows position shifts\nin the encoding space",
            font_size=24,
            color=BLUE
        ).next_to(final_box, DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        
        # Optional: Create axes and show the transformation visually
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"include_tip": True},
        ).scale(0.5)
        
        # Create a unit vector to show transformation
        vector = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 0),
            buff=0,
            color=YELLOW
        )
        
        # Position the coordinate system
        coordinate_group = VGroup(axes, vector)
        coordinate_group.next_to(conclusion, DOWN, buff=0.5)
        
        self.play(
            Create(axes),
            Create(vector)
        )
        
        # Animate the rotation
        self.play(
            Rotate(
                vector,
                angle=PI/4,
                about_point=axes.coords_to_point(0, 0)
            ),
            run_time=2
        )
        
        self.wait(2)

"""
cons of absolute position encoding, polute that data, no way to know 
relative position
"""

class RoPE(Scene):
    def construct(self):
        # Part 1: Title and Introduction
        title = Text("Rotary Position Encoding (RoPE)", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(
            FadeOut(title)
        )
        question = Text("Why RoPE?")
        self.play(Write(question))
        self.wait(1)
        self.play(question.animate.shift(UP*3))
        text1 = Text("1. Absolute position polltes the data", font_size=36,  should_center=False)
        text2 = Text("2. No way to know relative position", font_size=36, should_center=False)
        text1.move_to(ORIGIN)
        text2.next_to(text1, DOWN)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(VGroup(question, text1, text2)))
        self.wait(1)

        words = ["Jack", "loves", "to", "eat", "pizza"]
        word_mobjects = VGroup(*[Text(word) for word in words])
        word_mobjects.arrange(RIGHT, buff=0.3)
        self.play(Write(word_mobjects))
        self.play(word_mobjects.animate.shift(UP*2))
        self.play(
            word_mobjects[0].animate.set_color(YELLOW),
            word_mobjects[4].animate.set_color(YELLOW),
        )

