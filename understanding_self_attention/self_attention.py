from manim import *

class TextSelfAttention(Scene):
    def construct(self):
        text = Text("Self Attention")
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))

class TextWorkingOfSelfAttention(Scene):
    def construct(self):
        text = Text("Working of Self Attention")
        self.play(Write(text))
        # Move this text up and below show some quick animations of matrix multiplication to calculate the attention scores
        self.play(FadeOut(text))


class TextWhyDoesAttentionWork(Scene):
    def construct(self):
        text = Text("Why does Attention work?")
        self.play(Write(text))
        # Move this text up and below show some quick animations of writing the Q, K, V
        self.play(FadeOut(text))

class TextToAttentionScore(Scene):
    def construct(self):
        # Initial text setup (same until words split apart)
        delicious = Text("Self")
        pizza = Text("Attention").next_to(delicious, RIGHT, buff=0.2)
        text_group = VGroup(delicious, pizza)
        text_group.move_to(ORIGIN)
        
        self.play(Write(text_group), run_time=2)
        self.wait(0.5)
        self.play(text_group.animate.shift(UP*2))
        self.play(
            delicious.animate.shift(LEFT*2),
            pizza.animate.shift(RIGHT*2)
        )
        
        # Step 1: Create and position x1 and x2 boxes
        x1_squares = VGroup(*[Square(side_length=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        x2_squares = VGroup(*[Square(side_length=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        
        # Align them directly under the words
        x1_squares.next_to(delicious, DOWN, buff=0.5)
        x2_squares.next_to(pizza, DOWN, buff=0.5)
        
        # Replace Text labels with MathTex
        x1_label = MathTex("x_1", font_size=24).next_to(x1_squares, LEFT, buff=0.3)
        x2_label = MathTex("x_2", font_size=24).next_to(x2_squares, LEFT, buff=0.3)
        
        # Create vectors with labels
        self.play(
            Create(x1_squares),
            Create(x2_squares),
            Write(x1_label),
            Write(x2_label)
        )
        
        self.wait(0.5)
        
        # Step 2: Move x2 below x1 with proper alignment
        x2_target = x1_squares.get_center() + DOWN*2
        self.play(
            x2_squares.animate.move_to(x2_target),
            x2_label.animate.next_to(x2_target, LEFT*4, buff=0.3)
        )
        
        # Step 3: Create weight matrices with proper spacing
        matrix_size = 4
        single_matrix = VGroup(*[
            VGroup(*[Square(side_length=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(matrix_size)
        ]).arrange(DOWN*0.25, buff=0)
        
        # Create three identical matrices
        w_q = single_matrix.copy()
        w_k = single_matrix.copy()
        w_v = single_matrix.copy()
        
        # Step 4: Position matrices with clear spacing
        # Start with W_Q at top right
        w_q.move_to(RIGHT*4 + UP*2)
        # Position W_K below W_Q with gap
        w_k.move_to(w_q.get_center() + DOWN*2.5)
        # Position W_V below W_K with gap
        w_v.move_to(w_k.get_center() + DOWN*2.5)
        
        # Add matrix labels
        w_q_label = MathTex("W_Q", font_size=24).next_to(w_q, LEFT, buff=0.5)
        w_k_label = MathTex("W_K", font_size=24).next_to(w_k, LEFT, buff=0.5)
        w_v_label = MathTex("W_V", font_size=24).next_to(w_v, LEFT, buff=0.5)
        
        # Step 5: Show matrices after fading words
        self.play(FadeOut(delicious), FadeOut(pizza))
        
        self.play(
            FadeIn(w_q), Write(w_q_label),
            FadeIn(w_k), Write(w_k_label),
            FadeIn(w_v), Write(w_v_label)
        )
        
        # Step 6: Setup final multiplication scene
        # First fade out unnecessary elements
        self.play(
            FadeOut(w_k), FadeOut(w_k_label),
            FadeOut(w_v), FadeOut(w_v_label),
            FadeOut(x2_squares), FadeOut(x2_label)
        )
        
        # Group x1 and its label
        x1_group = VGroup(x1_squares, x1_label)
        
        # Move x1 to multiplication position
        self.play(
            x1_group.animate.move_to(LEFT*2 + UP*0.5),
            w_q.animate.move_to(RIGHT),
            w_q_label.animate.move_to(UP*1.5 + RIGHT)
        )
        
        # Add multiplication and equals signs
        mult_symbol = MathTex("\\times", font_size=36).next_to(x1_squares, RIGHT, buff=0.5)
        equals_sign = MathTex("=", font_size=36).next_to(w_q, RIGHT, buff=0.5)
        
        # Create result vector
        q_vector = VGroup(*[Square(side_length=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        q_vector.next_to(equals_sign, RIGHT, buff=0.5)
        q_label = MathTex("q_1", font_size=24).next_to(q_vector, UP, buff=0.3)
        
        self.play(Write(mult_symbol), Write(equals_sign))
        self.play(Create(q_vector), Write(q_label))
        
        self.wait(2)