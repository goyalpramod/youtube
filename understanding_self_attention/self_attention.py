from manim import *

class TextSelfAttention(Scene):
    def construct(self):
        text = Text("Self Attention", font_size=98)
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))

class TextWorkingOfSelfAttention(Scene):
    def construct(self):
        text = Text("Working of Self Attention")
        self.play(Write(text))
        self.play(text.animate.shift(UP*3))
        # Move this text up and below show some quick animations of matrix multiplication to calculate the attention scores
        self.play(FadeOut(text))

class ExampleText(Scene):
    def construct(self):
        # Create texts with proper arrangement
        text1 = Text("Pramod ", font_size=24)
        text2 = Text("loves to eat ", font_size=24)
        text3 = Text("pizza. ", font_size=24)
        text4 = Text("He ", font_size=24)
        text5 = Text("ate some last night", font_size=24)

        # Arrange texts horizontally
        text_group = VGroup(text1, text2, text3, text4, text5).arrange(RIGHT, buff=0.1)
        
        # Center the text group
        text_group.move_to(ORIGIN)

        # Write the text
        self.play(Write(text_group))
        self.wait(2)

        # Create and show the rectangle around "He"
        framebox = SurroundingRectangle(text4, buff=0.1, color=RED)
        self.play(Create(framebox))
        self.wait(2)

        # Animate opacity changes
        self.play(
            text1.animate.set_opacity(0.9),
            VGroup(text2, text5).animate.set_opacity(0.4),
            text3.animate.set_opacity(0.7)
        )
        self.wait(2)

class ThankYou(Scene):
    def construct(self):
        text = Text("Thank You", font_size=72)
        text2 = Text("(you are awesome)", font_size=24).next_to(text, DOWN, buff=0.2)
        self.play(Write(text), run_time=3)
        self.wait(2)
        self.play(FadeIn(text2))
        self.wait(1)

class LatexSelfAttention(Scene):
    def construct(self):
        # Break down the equation into parts for better control and animation
        self_attention_equation = MathTex(
            r"Attention(Q, K, V)", 
            r"=", 
            r"softmax",
            r"(",
            r"\frac{QK^T}{\sqrt{d_k}}",
            r")",
            r"V",
        )
        
        # Position the equation in the center
        self_attention_equation.move_to(ORIGIN)
        
        # Animate each part of the equation
        self.play(Write(self_attention_equation))
        
        # Wait at the end
        self.wait(2)
class TextAttentionIsAllYouNeed(Scene):
    def construct(self):
        text = Text("Attention Is All You Need", font_size=36)
        self.play(Write(text))
        # Move this text up and below show some quick animations of writing the Q, K, V
        self.play(FadeOut(text))

class TextWhyDoesAttentionWork(Scene):
    def construct(self):
        text = Text("Why does Attention work?")
        self.play(Write(text))
        self.play(text.animate.shift(UP*3))
        # Move this text up and below show some quick animations of writing the Q, K, V
        self.play(FadeOut(text))

class YoutubeThumbnailWithUnderline(Scene):
    def construct(self):
        text1 = Text("Understanding", font_size=72)
        line1 = Line(LEFT*3, RIGHT*3, color=WHITE).next_to(text1, DOWN, buff=0.2)
        text2 = Text("Self Attention", font_size=72).next_to(text1, DOWN*1.5, buff=0.2)
        line2 = Line(LEFT*3, RIGHT*3, color=WHITE).next_to(text2, DOWN, buff=0.2)
        self.play(Write(text1), Write(text2), Create(line1), Create(line2))
        self.wait(2)

class YoutubeThumbnailWithoutUnderline(Scene):
    def construct(self):
        text1 = Text("Understanding", font_size=72).set_color_by_gradient("#FFA500", "#FF4D00", "#FF0000")  # Bright orange -> Vivid orange-red -> Pure red
        text2 = Text("Self Attention", font_size=72).next_to(text1, DOWN*1.5, buff=0.2).set_color_by_gradient("#FFA500", "#FF4D00", "#FF0000")
        self.play(Write(text1), Write(text2))
        self.wait(2)

class TextToQKV(Scene):
    def construct(self):
        # Initial text setup (same until words split apart)
        delicious = Text("Self")
        new_text2 = Text("of").next_to(delicious, LEFT, buff=0.2)
        new_text1 = Text("Working").next_to(new_text2, LEFT, buff=0.2)
        pizza = Text("Attention").next_to(delicious, RIGHT, buff=0.2)
        text_group_new = VGroup(new_text1, new_text2 , delicious, pizza)
        text_group = VGroup(delicious, pizza)
        text_group_new.move_to(ORIGIN)
        
        self.play(Write(text_group_new), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(new_text1), FadeOut(new_text2))
        self.wait(0.5)
        self.play(text_group.animate.shift(ORIGIN + LEFT*2))   
        self.play(text_group.animate.shift(UP*2))
        self.play(
            delicious.animate.shift(LEFT*2),
            pizza.animate.shift(RIGHT*2)
        )
        
        # Step 1: Create and position x1 and x2 boxes
        x1_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        x2_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        
        # Align them directly under the words
        x1_squares.next_to(delicious, DOWN, buff=0.5)
        x2_squares.next_to(pizza, DOWN, buff=0.5)
        
        # Replace Text labels with MathTex
        x1_label = MathTex("x_1", font_size=36).next_to(x1_squares, LEFT, buff=0.3)
        x2_label = MathTex("x_2", font_size=36).next_to(x2_squares, LEFT, buff=0.3)
        
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
        w_q = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(matrix_size)
        ]).arrange(DOWN*0.25, buff=0)
        
        w_k = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(matrix_size)
        ]).arrange(DOWN*0.25, buff=0)
        
        w_v = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(matrix_size)
        ]).arrange(DOWN*0.25, buff=0)
        
        # Step 4: Position matrices with clear spacing
        # Start with W_Q at top right
        w_q.move_to(RIGHT*4 + UP*2)
        # Position W_K below W_Q with gap
        w_k.move_to(w_q.get_center() + DOWN*2.5)
        # Position W_V below W_K with gap
        w_v.move_to(w_k.get_center() + DOWN*2.5)
        
        # Add matrix labels
        w_q_label = MathTex("W_Q", font_size=36).next_to(w_q, LEFT, buff=0.5)
        w_k_label = MathTex("W_K", font_size=36).next_to(w_k, LEFT, buff=0.5)
        w_v_label = MathTex("W_V", font_size=36).next_to(w_v, LEFT, buff=0.5)
        
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
        
        w_k.move_to(w_q.get_center()) 
        w_v.move_to(w_q.get_center()) 

        # Add multiplication and equals signs
        mult_symbol = MathTex("\\times", font_size=36).next_to(x1_squares, RIGHT, buff=0.5)
        equals_sign = MathTex("=", font_size=36).next_to(w_q, RIGHT, buff=0.5)
        
        # Create result vector
        q_vector = VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        k_vector = VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v_vector = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        q_vector.next_to(equals_sign, RIGHT, buff=0.5)
        k_vector.next_to(equals_sign, RIGHT, buff=0.5)
        v_vector.next_to(equals_sign, RIGHT, buff=0.5)
        q_label = MathTex("q_1", font_size=36).next_to(q_vector, UP, buff=0.3)
        k_label = MathTex("k_1", font_size=36).next_to(q_vector, UP, buff=0.3)
        v_label = MathTex("v_1", font_size=36).next_to(q_vector, UP, buff=0.3)
        
        self.play(Write(mult_symbol), Write(equals_sign))
        self.play(Create(q_vector), Write(q_label))
        
        # For visualization of all columns
        column_boxes = []
        for i in range(3):  # assuming 3 columns
            column = VGroup(*[row[i] for row in w_q])
            box = SurroundingRectangle(column, buff=0)
            column_boxes.append(box)

        self.wait(1)
        framebox_x1 = SurroundingRectangle(x1_squares[:], buff = 0, color=RED)
        framebox1 = SurroundingRectangle(column_boxes[0], buff = 0, color=RED)
        framebox2 = SurroundingRectangle(q_vector[0], buff = 0, color=RED)
        framebox3 = SurroundingRectangle(column_boxes[1], buff = 0, color=RED)
        framebox4 = SurroundingRectangle(q_vector[1], buff = 0, color=RED)
        framebox5 = SurroundingRectangle(column_boxes[2], buff = 0, color=RED)
        framebox6 = SurroundingRectangle(q_vector[2], buff = 0, color=RED)
        self.play(
            Create(framebox_x1),
            Create(framebox1),
            Create(framebox2),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox3),
            ReplacementTransform(framebox2,framebox4),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox3,framebox5),
            ReplacementTransform(framebox4,framebox6),
        )
        self.wait()
        self.play(FadeOut(framebox5), FadeOut(framebox6), FadeOut(framebox_x1)) 
        
        self.wait(1)
        self.play(FadeOut(w_q_label), FadeOut(q_label), FadeOut(q_vector), FadeOut(w_q))
        self.play(FadeIn(w_k_label.next_to(w_q, UP)), FadeIn(k_label), FadeIn(k_vector), FadeIn(w_k))
        self.play(FadeOut(w_k_label), FadeOut(k_label), FadeOut(k_vector), FadeOut(w_k))
        self.play(FadeIn(w_v_label.next_to(w_q, UP)), FadeIn(v_label), FadeIn(v_vector), FadeIn(w_v))
        self.play(FadeOut(w_v_label), FadeOut(v_label), FadeOut(mult_symbol), FadeOut(equals_sign), FadeOut(x1_group), FadeOut(v_vector), FadeOut(w_v))
        self.wait(2)

class QKVtoAttentionScore(Scene):
    def construct(self):
        # Step 1: Create x1 and x2 vectors
        x1_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        x2_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        
        # Position x1 and x2 horizontally
        x1_squares.move_to(LEFT*3 + UP*2)
        x2_squares.move_to(RIGHT*3 + UP*2)
        
        # Add x labels
        x1_label = MathTex("x_1", font_size=36).next_to(x1_squares, LEFT, buff=0.3)
        x2_label = MathTex("x_2", font_size=36).next_to(x2_squares, LEFT, buff=0.3)
        
        # Create vectors for first word (q1, k1, v1)
        q1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        k1_squares = VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        
        # Position vectors for first word vertically
        q1_squares.next_to(x1_squares, DOWN, buff=1)
        k1_squares.next_to(q1_squares, DOWN, buff=1)
        v1_squares.next_to(k1_squares, DOWN, buff=1)
        
        # Add labels for first word vectors
        q1_label = MathTex("q_1", font_size=36).next_to(q1_squares, LEFT, buff=0.3)
        k1_label = MathTex("k_1", font_size=36).next_to(k1_squares, LEFT, buff=0.3)
        v1_label = MathTex("v_1", font_size=36).next_to(v1_squares, LEFT, buff=0.3)
        
        # Create vectors for second word (q2, k2, v2)
        q2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        k2_squares = VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        
        # Position vectors for second word vertically
        q2_squares.next_to(x2_squares, DOWN, buff=1)
        k2_squares.next_to(q2_squares, DOWN, buff=1)
        v2_squares.next_to(k2_squares, DOWN, buff=1)
        
        # Add labels for second word vectors
        q2_label = MathTex("q_2", font_size=36).next_to(q2_squares, LEFT, buff=0.3)
        k2_label = MathTex("k_2", font_size=36).next_to(k2_squares, LEFT, buff=0.3)
        v2_label = MathTex("v_2", font_size=36).next_to(v2_squares, LEFT, buff=0.3)
        
        # Create animations
        # First show x vectors
        self.play(
            Create(x1_squares), Write(x1_label),
            Create(x2_squares), Write(x2_label)
        )
        self.wait(2)
        
        # Then show q, k, v vectors for first word
        self.play(
            Create(q1_squares), Write(q1_label),
            Create(k1_squares), Write(k1_label),
            Create(v1_squares), Write(v1_label),
            Create(q2_squares), Write(q2_label),
            Create(k2_squares), Write(k2_label),
            Create(v2_squares), Write(v2_label),
        )
        
        self.wait(2)

        self.play(FadeOut(x1_squares), FadeOut(x2_squares), FadeOut(x1_label), FadeOut(x2_label), FadeOut(v2_label), FadeOut(v1_label), FadeOut(q2_label), FadeOut(v1_squares), FadeOut(v2_squares), FadeOut(q2_squares))
        
        self.wait(2)

        # Create surrounding rectangles
        rect_q1 = SurroundingRectangle(q1_squares, buff=0.1, color=BLUE)
        rect_k1 = SurroundingRectangle(k1_squares, buff=0.1, color=BLUE)
        rect_k2 = SurroundingRectangle(k2_squares, buff=0.1, color=BLUE)

        # Create score texts
        score1 = MathTex("score_1", font_size=36)
        score2 = MathTex("score_2", font_size=36)
        
        # Position scores
        score1.next_to(k1_squares, DOWN, buff=1)
        score2.next_to(k2_squares, DOWN, buff=1)

        # First multiplication animation (q1 · k1)
        self.play(Create(rect_q1))
        self.wait(0.5)
        self.play(ReplacementTransform(rect_q1.copy(), rect_k1))
        self.play(Write(score1))
        self.wait(1)

        # Move q1 to the right for second multiplication
        q1_target_pos = k2_squares.get_center() + UP*2
        self.play(
            q1_squares.animate.move_to(q1_target_pos),
            q1_label.animate.next_to(q1_target_pos, LEFT*4, buff=0.3),
            rect_q1.animate.move_to(q1_target_pos)
        )
        
        # Second multiplication animation (q1 · k2)
        self.play(ReplacementTransform(rect_q1.copy(), rect_k2))
        self.play(Write(score2))

        
        self.wait(2)

        # Optional: Fade out everything at the end
        self.play(
            *[FadeOut(mob) for mob in [
                q1_squares, k1_squares, k2_squares,
                q1_label, k1_label, k2_label,
                rect_q1, rect_k1, rect_k2,
            ]]
        )

        score_num1 = MathTex("92", font_size=36).move_to(LEFT)
        score_num2 = MathTex("80", font_size=36).move_to(RIGHT)
        self.play(ReplacementTransform(score1, score_num1), ReplacementTransform(score2, score_num2))

        # After showing score numbers
        dv = MathTex("\\sqrt{D_v}", font_size=36)

        dv1 = dv.copy().next_to(score_num1, DOWN + UP*0.25)
        dv2 = dv.copy().next_to(score_num2, DOWN + UP*0.25)
        division_line1 = Line(LEFT*0.4, RIGHT*0.4, color=WHITE)
        division_line2 = Line(LEFT*0.4, RIGHT*0.4, color=WHITE)
        division_line1.next_to(dv1, UP*0.3, buff=0.4)
        division_line2.next_to(dv2, UP*0.3, buff=0.4)

        self.play(Write(dv1), Write(dv2), Write(division_line1), Write(division_line2))
        self.wait(1)

        # Transform into actual values
        div_val1 = MathTex("11.5", font_size=36).move_to(dv1)
        div_val2 = MathTex("10", font_size=36).move_to(dv2)

        score_1_group = VGroup(score_num1, dv1, division_line1)
        score_2_group = VGroup(score_num2, dv2, division_line2)

        self.play(
            ReplacementTransform(score_1_group, div_val1),
            ReplacementTransform(score_2_group, div_val2)
        )
        self.wait(1)

        # Create Softmax boxes
        softmax_box1 = VGroup(
            Text("Softmax", font_size=24),
            SurroundingRectangle(VGroup(score_num1, div_val1), buff=0.3)
        )
        softmax_box2 = VGroup(
            Text("Softmax", font_size=24),
            SurroundingRectangle(VGroup(score_num2, div_val2), buff=0.3)
        )
        softmax_box1[0].next_to(softmax_box1[1], UP, buff=0.1)
        softmax_box2[0].next_to(softmax_box2[1], UP, buff=0.1)

        self.play(Create(softmax_box1, run_time=2, rate_func = linear), Create(softmax_box2, run_time=2, rate_func=linear))
        self.wait(1)

        # Fade out right score
        self.play(
            FadeOut(score_num2),
            FadeOut(div_val2),
            FadeOut(softmax_box2)
        )
        self.wait(1)

        # Move left score to center
        self.play(
            div_val1.animate.move_to(ORIGIN),
            softmax_box1.animate.move_to(ORIGIN + UP*0.25)
        )
        self.wait(1)

        # First show the general Softmax equation
        general_softmax = MathTex(
            "Softmax(x_i) = \\frac{e^{x_i}}{\\sum_{j=1}^n e^{x_j}}",
            font_size=36
        ).next_to(softmax_box1, DOWN, buff=1)

        self.play(Write(general_softmax))
        self.wait(1)

        # Then transform into the specific equation
        final_eq = MathTex(
            "Softmax(\\frac{score_1}{\\sqrt{D_v}}) = \\frac{e^{92/8}}{e^{92/8} + e^{80/8}} = 0.82",
            font_size=36
        ).next_to(softmax_box1, DOWN, buff=1)

        self.play(ReplacementTransform(general_softmax, final_eq))
        # After the final equation, let's organize the values and vectors
        self.wait(1)

        # Move 0.82 to center
        softmax_val1 = MathTex("0.82", font_size=36).move_to(ORIGIN)
        self.play(
            FadeOut(softmax_box1),
            FadeOut(div_val1),
            ReplacementTransform(final_eq, softmax_val1)
        )
        self.wait(1)

        # Create v1 and v2 vectors
        v1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)

        v1_label = MathTex("v_1", font_size=36)
        v2_label = MathTex("v_2", font_size=36)

        # Position v1 to the left of 0.82 and v2 to the right
        v1_group = VGroup(v1_label, v1_squares).arrange(RIGHT, buff=0.3)
        v2_group = VGroup(v2_label, v2_squares).arrange(RIGHT, buff=0.3)

        # Position the groups horizontally
        v1_group.next_to(softmax_val1, LEFT, buff=1)
        v2_group.next_to(softmax_val1, RIGHT, buff=1)

        self.play(
            Create(v1_squares), Write(v1_label),
            Create(v2_squares), Write(v2_label)
        )
        self.wait(1)

        # Create multiplication symbols
        times1 = MathTex("\\times", font_size=36).next_to(v1_squares, RIGHT, buff=0.3)
        times2 = MathTex("\\times", font_size=36).next_to(v2_squares, RIGHT, buff=0.3)

        # Position 0.18 to the right of v2
        softmax_val2 = MathTex("0.18", font_size=36).next_to(v2_group, RIGHT * 3, buff=0.3)


        # Create surrounding rectangles for multiplication visualization
        rect_val1 = SurroundingRectangle(softmax_val1, buff=0.1, color=BLUE)
        rect_v1 = SurroundingRectangle(v1_squares, buff=0.1, color=BLUE)
        rect_val2 = SurroundingRectangle(softmax_val2, buff=0.1, color=BLUE)
        rect_v2 = SurroundingRectangle(v2_squares, buff=0.1, color=BLUE)

        # Show first multiplication
        self.play(Create(rect_val1))
        self.play(Write(times1))
        self.play(ReplacementTransform(rect_val1.copy(), rect_v1))
        self.wait(1)

        # Show second multiplication
        self.play(
            Write(softmax_val2),
            Write(times2)
        )
        self.play(Create(rect_val2))
        self.play(ReplacementTransform(rect_val2.copy(), rect_v2))
        self.wait(1)

        # Create result vectors z1 and z2
        z1_squares = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.45) for _ in range(3)]).arrange(RIGHT, buff=0)
        z2_squares = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.15) for _ in range(3)]).arrange(RIGHT, buff=0)

        z1_label = MathTex("v_1", font_size=36)
        z2_label = MathTex("v_2", font_size=36)

        # Position z1 and z2 below v1 and v2
        z1_group = VGroup(z1_label, z1_squares).arrange(RIGHT, buff=0.3).next_to(v1_group, DOWN*2)
        z2_group = VGroup(z2_label, z2_squares).arrange(RIGHT, buff=0.3).next_to(v2_group, DOWN*2)

        # Show resulting vectors
        self.play(
            Create(z1_squares), Write(z1_label),
            Create(z2_squares), Write(z2_label)
        )
        self.wait(1)

        # Add plus symbol between z1 and z2 for final sum
        plus = MathTex("+", font_size=36).move_to(
            (z1_squares.get_center() + z2_squares.get_center()) / 2
        )
        self.play(Write(plus))

        # Create final sum rectangle
        sum_rect = SurroundingRectangle(VGroup(z1_squares, plus, z2_squares), buff=0.2, color=GREEN)
        self.play(Create(sum_rect))
        self.wait(2)

        final_z1_squares = VGroup(*[Square(side_length=0.5, fill_color="#90EE90", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        final_z1_label = MathTex("z_1", font_size=36)
        final_z1_group = VGroup(final_z1_label, final_z1_squares).arrange(RIGHT, buff=0.3).move_to(ORIGIN)

        self.play(
        FadeOut(v1_group),
        FadeOut(v2_group),
        FadeOut(rect_val1),
        FadeOut(rect_v1),
        FadeOut(rect_val2),
        FadeOut(rect_v2),
        FadeOut(softmax_val1),
        FadeOut(softmax_val2),
        FadeOut(times1),
        FadeOut(times2),
        )
        self.wait(2)
        group_1 = VGroup(z1_squares, z1_label, z2_squares, z2_label, plus, sum_rect)
        
        self.play(
            ReplacementTransform(group_1, final_z1_group),
        )
        self.wait(2)
        # Create the text "Attention value for 'Self'"
        attention_text = Text("Attention value for 'Self'", font_size=36)
        attention_text.move_to(UP*2)  # Position it above the vectors

        # Animate the text
        self.play(Write(attention_text))
        self.wait(1)

class QKVtoAttentionScore2(Scene):
    def construct(self):
        # Step 1: Create x1 and x2 vectors (unchanged)
        x1_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        x2_squares = VGroup(*[Square(side_length=0.5, fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        
        # Position x1 and x2 horizontally (unchanged)
        x1_squares.move_to(LEFT*3 + UP*2)
        x2_squares.move_to(RIGHT*3 + UP*2)
        
        # Add x labels (unchanged)
        x1_label = MathTex("x_1", font_size=36).next_to(x1_squares, LEFT, buff=0.3)
        x2_label = MathTex("x_2", font_size=36).next_to(x2_squares, LEFT, buff=0.3)
        
        # Create vectors for word 2 (since this is AttentionScore2)
        q2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        k2_squares = VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        
        # Position vectors for word 2 vertically under x2
        q2_squares.next_to(x2_squares, DOWN, buff=1)
        k2_squares.next_to(q2_squares, DOWN, buff=1)
        v2_squares.next_to(k2_squares, DOWN, buff=1)
        
        # Add labels for word 2 vectors
        q2_label = MathTex("q_2", font_size=36).next_to(q2_squares, LEFT, buff=0.3)
        k2_label = MathTex("k_2", font_size=36).next_to(k2_squares, LEFT, buff=0.3)
        v2_label = MathTex("v_2", font_size=36).next_to(v2_squares, LEFT, buff=0.3)
        
        # Create vectors for word 1
        q1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        k1_squares = VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        
        # Position vectors for word 1 vertically under x1
        q1_squares.next_to(x1_squares, DOWN, buff=1)
        k1_squares.next_to(q1_squares, DOWN, buff=1)
        v1_squares.next_to(k1_squares, DOWN, buff=1)
        
        # Add labels for word 1 vectors
        q1_label = MathTex("q_1", font_size=36).next_to(q1_squares, LEFT, buff=0.3)
        k1_label = MathTex("k_1", font_size=36).next_to(k1_squares, LEFT, buff=0.3)
        v1_label = MathTex("v_1", font_size=36).next_to(v1_squares, LEFT, buff=0.3)
        
        # First show x vectors
        self.play(
            Create(x1_squares), Write(x1_label),
            Create(x2_squares), Write(x2_label)
        )
        
        # Then show all q, k, v vectors
        self.play(
            Create(q2_squares), Write(q2_label),
            Create(k2_squares), Write(k2_label),
            Create(v2_squares), Write(v2_label),
            Create(q1_squares), Write(q1_label),
            Create(k1_squares), Write(k1_label),
            Create(v1_squares), Write(v1_label)
        )

        # Fade out unnecessary elements
        self.play(
            FadeOut(x1_squares), FadeOut(x2_squares),
            FadeOut(x1_label), FadeOut(x2_label),
            FadeOut(v1_label), FadeOut(v2_label),
            FadeOut(q1_label), FadeOut(v1_squares),
            FadeOut(v2_squares), FadeOut(q1_squares)
        )

        # Should be rect_q2 instead of rect_q1
        rect_q2 = SurroundingRectangle(q2_squares, buff=0.1, color=BLUE)
        rect_k1 = SurroundingRectangle(k1_squares, buff=0.1, color=BLUE)
        rect_k2 = SurroundingRectangle(k2_squares, buff=0.1, color=BLUE)

        # Position scores (unchanged)
        score1 = MathTex("score_1", font_size=36)
        score2 = MathTex("score_2", font_size=36)
        score1.next_to(k1_squares, DOWN, buff=1)
        score2.next_to(k2_squares, DOWN, buff=1)

        # First multiplication animation (q2 · k1)
        self.play(Create(rect_q2))
        self.play(ReplacementTransform(rect_q2.copy(), rect_k1))
        self.play(Write(score1))


        # Second multiplication animation (q2 · k2)
        self.play(ReplacementTransform(rect_q2.copy(), rect_k2))
        self.play(Write(score2))

        # Fade out with correct references
        self.play(
            *[FadeOut(mob) for mob in [
                q2_squares, k1_squares, k2_squares,
                q2_label, k1_label, k2_label,
                rect_q2, rect_k1, rect_k2,
            ]]
        )

        score_num1 = MathTex("76", font_size=36).move_to(LEFT)
        score_num2 = MathTex("98", font_size=36).move_to(RIGHT)
        self.play(ReplacementTransform(score1, score_num1), ReplacementTransform(score2, score_num2))

        # After showing score numbers
        dv = MathTex("\\sqrt{D_v}", font_size=36)
        dv1 = dv.copy().next_to(score_num1, DOWN + UP*0.25)
        dv2 = dv.copy().next_to(score_num2, DOWN + UP*0.25)
        division_line1 = Line(LEFT*0.4, RIGHT*0.4, color=WHITE)
        division_line2 = Line(LEFT*0.4, RIGHT*0.4, color=WHITE)
        division_line1.next_to(dv1, UP*0.3, buff=0.4)
        division_line2.next_to(dv2, UP*0.3, buff=0.4)

        self.play(Write(dv1), Write(dv2), Write(division_line1), Write(division_line2))

        # Transform into actual values
        div_val1 = MathTex("9.5", font_size=36).move_to(dv1)
        div_val2 = MathTex("12.25", font_size=36).move_to(dv2)

        score_1_group = VGroup(score_num1, dv1, division_line1)
        score_2_group = VGroup(score_num2, dv2, division_line2)

        self.play(
            ReplacementTransform(score_1_group, div_val1),
            ReplacementTransform(score_2_group, div_val2)
        )

        # Create Softmax boxes
        softmax_box1 = VGroup(
            Text("Softmax", font_size=24),
            SurroundingRectangle(VGroup(score_num1, div_val1), buff=0.3)
        )
        softmax_box2 = VGroup(
            Text("Softmax", font_size=24),
            SurroundingRectangle(VGroup(score_num2, div_val2), buff=0.3)
        )
        softmax_box1[0].next_to(softmax_box1[1], UP, buff=0.1)
        softmax_box2[0].next_to(softmax_box2[1], UP, buff=0.1)

        self.play(Create(softmax_box1, run_time=2, rate_func=linear), Create(softmax_box2, run_time=2, rate_func=linear))

        # Fade out right score
        self.play(
            FadeOut(score_num2),
            FadeOut(div_val2),
            FadeOut(softmax_box2)
        )

        # Move left score to center
        self.play(
            div_val1.animate.move_to(ORIGIN),
            softmax_box1.animate.move_to(ORIGIN + UP*0.25)
        )

        # First show the general Softmax equation
        general_softmax = MathTex(
            "Softmax(x_i) = \\frac{e^{x_i}}{\\sum_{j=1}^n e^{x_j}}",
            font_size=36
        ).next_to(softmax_box1, DOWN, buff=1)

        self.play(Write(general_softmax))

        # Then transform into the specific equation
        final_eq = MathTex(
            "Softmax(\\frac{score_1}{\\sqrt{D_v}}) = \\frac{e^{92/8}}{e^{92/8} + e^{80/8}} = 0.82",
            font_size=36
        ).next_to(softmax_box1, DOWN, buff=1)

        self.play(ReplacementTransform(general_softmax, final_eq))
        # After the final equation, let's organize the values and vectors

        softmax_val1 = MathTex("0.06", font_size=36).move_to(ORIGIN)
        self.play(
            FadeOut(softmax_box1),
            FadeOut(div_val1),
            ReplacementTransform(final_eq, softmax_val1)
        )

        # Create v1 and v2 vectors
        v1_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        v2_squares = VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)

        v1_label = MathTex("v_1", font_size=36)
        v2_label = MathTex("v_2", font_size=36)

        # Position v1 to the left of 0.82 and v2 to the right
        v1_group = VGroup(v1_label, v1_squares).arrange(RIGHT, buff=0.3)
        v2_group = VGroup(v2_label, v2_squares).arrange(RIGHT, buff=0.3)

        # Position the groups horizontally
        v1_group.next_to(softmax_val1, LEFT, buff=1)
        v2_group.next_to(softmax_val1, RIGHT, buff=1)

        self.play(
            Create(v1_squares), Write(v1_label),
            Create(v2_squares), Write(v2_label)
        )

        # Create multiplication symbols
        times1 = MathTex("\\times", font_size=36).next_to(v1_squares, RIGHT, buff=0.3)
        times2 = MathTex("\\times", font_size=36).next_to(v2_squares, RIGHT, buff=0.3)


        softmax_val2 = MathTex("0.94", font_size=36).next_to(v2_group, RIGHT * 3, buff=0.3)


        # Create surrounding rectangles for multiplication visualization
        rect_val1 = SurroundingRectangle(softmax_val1, buff=0.1, color=BLUE)
        rect_v1 = SurroundingRectangle(v1_squares, buff=0.1, color=BLUE)
        rect_val2 = SurroundingRectangle(softmax_val2, buff=0.1, color=BLUE)
        rect_v2 = SurroundingRectangle(v2_squares, buff=0.1, color=BLUE)

        # Show first multiplication
        self.play(Create(rect_val1))
        self.play(Write(times1))
        self.play(ReplacementTransform(rect_val1.copy(), rect_v1))

        # Show second multiplication
        self.play(
            Write(softmax_val2),
            Write(times2)
        )
        self.play(Create(rect_val2))
        self.play(ReplacementTransform(rect_val2.copy(), rect_v2))

        # Create result vectors z1 and z2
        z1_squares = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.45) for _ in range(3)]).arrange(RIGHT, buff=0)
        z2_squares = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.15) for _ in range(3)]).arrange(RIGHT, buff=0)

        z1_label = MathTex("v_1", font_size=36)
        z2_label = MathTex("v_2", font_size=36)

        # Position z1 and z2 below v1 and v2
        z1_group = VGroup(z1_label, z1_squares).arrange(RIGHT, buff=0.3).next_to(v1_group, DOWN*2)
        z2_group = VGroup(z2_label, z2_squares).arrange(RIGHT, buff=0.3).next_to(v2_group, DOWN*2)

        # Show resulting vectors
        self.play(
            Create(z1_squares), Write(z1_label),
            Create(z2_squares), Write(z2_label)
        )

        # Add plus symbol between z1 and z2 for final sum
        plus = MathTex("+", font_size=36).move_to(
            (z1_squares.get_center() + z2_squares.get_center()) / 2
        )
        self.play(Write(plus))

        # Create final sum rectangle
        sum_rect = SurroundingRectangle(VGroup(z1_squares, plus, z2_squares), buff=0.2, color=GREEN)
        self.play(Create(sum_rect))

        final_z1_squares = VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
        final_z1_label = MathTex("z_2", font_size=36)
        final_z1_group = VGroup(final_z1_label, final_z1_squares).arrange(RIGHT, buff=0.3).move_to(ORIGIN)

        self.play(
        FadeOut(v1_group),
        FadeOut(v2_group),
        FadeOut(rect_val1),
        FadeOut(rect_v1),
        FadeOut(rect_val2),
        FadeOut(rect_v2),
        FadeOut(softmax_val1),
        FadeOut(softmax_val2),
        FadeOut(times1),
        FadeOut(times2),
        )
        group_1 = VGroup(z1_squares, z1_label, z2_squares, z2_label, plus, sum_rect)
        
        self.play(
            ReplacementTransform(group_1, final_z1_group),
        )
        # Create the text "Attention value for 'Self'"
        attention_text = Text("Attention value for 'Attention'", font_size=36)
        attention_text.move_to(UP*2)  # Position it above the vectors

        # Animate the text
        self.play(Write(attention_text))

class TextToMatrix(Scene):
    def construct(self):
        # Initial text setup
        word1 = Text("Self")
        word2 = Text("Attention").next_to(word1, RIGHT, buff=0.2)
        text_group = VGroup(word1, word2)
        text_group.move_to(ORIGIN)
        
        # Write the words and move them up
        self.play(Write(text_group), run_time=2)
        self.wait(0.5)
        self.play(text_group.animate.shift(UP*2))
        self.play(
            word1.animate.shift(LEFT*2),
            word2.animate.shift(RIGHT*2)
        )
        
        # Create x1 and x2 vectors (4×1 matrices)
        x1_squares = VGroup(*[Square(side_length=0.5,fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        x2_squares = VGroup(*[Square(side_length=0.5,fill_color=YELLOW, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
        
        # Position vectors under words
        x1_squares.next_to(word1, DOWN, buff=0.5)
        x2_squares.next_to(word2, DOWN, buff=0.5)
        
        # Add x1, x2 labels
        x1_label = MathTex("x_1", font_size=36).next_to(x1_squares, LEFT, buff=0.3)
        x2_label = MathTex("x_2", font_size=36).next_to(x2_squares, LEFT, buff=0.3)
        
        # Show vectors and labels
        self.play(
            Create(x1_squares),
            Create(x2_squares),
            Write(x1_label),
            Write(x2_label)
        )
        self.wait(0.5)
        
        # Group vectors into matrix X
        matrix_X = VGroup(x1_squares, x2_squares)
        x_label = MathTex("X", font_size=36)
        
        # Move vectors together to form matrix
        self.play(
            x2_squares.animate.next_to(x1_squares, DOWN, buff=0),
            FadeOut(x1_label),
            FadeOut(x2_label),
            FadeOut(word1),
            FadeOut(word2)
        )
        
        # Add X label
        x_label.next_to(matrix_X, LEFT, buff=0.3)
        self.play(Write(x_label))
        
        
        
        w_q = VGroup(*[
                VGroup(*[Square(side_length=0.5,fill_color="#FFB6C1", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
                for _ in range(4)
            ]).arrange(DOWN, buff=0)
        w_k = VGroup(*[
                VGroup(*[Square(side_length=0.5,fill_color="#E6E6FA", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
                for _ in range(4)
            ]).arrange(DOWN, buff=0)
        w_v = VGroup(*[
                VGroup(*[Square(side_length=0.5,fill_color="#FFDAB9", fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
                for _ in range(4)
            ]).arrange(DOWN, buff=0)
        
        # Position weight matrices
        w_q.move_to(RIGHT*4 + UP*2)
        w_k.next_to(w_q, DOWN, buff=0.5)
        w_v.next_to(w_k, DOWN, buff=0.5)
        
        # Add matrix labels
        w_q_label = MathTex("W_Q", font_size=36).next_to(w_q, LEFT, buff=0.5)
        w_k_label = MathTex("W_K", font_size=36).next_to(w_k, LEFT, buff=0.5)
        w_v_label = MathTex("W_V", font_size=36).next_to(w_v, LEFT, buff=0.5)
        
        # Show weight matrices
        self.play(
            FadeIn(w_q), Write(w_q_label),
            FadeIn(w_k), Write(w_k_label),
            FadeIn(w_v), Write(w_v_label)
        )
        
        # Setup multiplication scene
        self.play(
            FadeOut(w_k), FadeOut(w_k_label),
            FadeOut(w_v), FadeOut(w_v_label)
        )
        
        # Position for multiplication
        self.play(
            matrix_X.animate.move_to(LEFT*2 + UP*0.5),
            x_label.animate.move_to(LEFT*2 + UP*1.5),
            w_q.animate.move_to(RIGHT),
            w_q_label.animate.move_to(UP*1.5 + RIGHT)
        )
        
        w_k.move_to(w_q.get_center())
        w_v.move_to(w_q.get_center())

        # Add multiplication symbols
        mult_symbol = MathTex("\\times", font_size=36).next_to(matrix_X, RIGHT, buff=0.5)
        equals_sign = MathTex("=", font_size=36).next_to(w_q, RIGHT, buff=0.5)
        
        # Create result matrix Q (2×3)
        q_matrix = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#FFB6C1", fill_opacity=0.7) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(2)
        ]).arrange(DOWN, buff=0)
        k_matrix = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#E6E6FA", fill_opacity=0.7) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(2)
        ]).arrange(DOWN, buff=0)
        v_matrix = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color="#FFDAB9", fill_opacity=0.7) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(2)
        ]).arrange(DOWN, buff=0)
        
        q_matrix.next_to(equals_sign, RIGHT, buff=0.5)
        k_matrix.next_to(equals_sign, RIGHT, buff=0.5)
        v_matrix.next_to(equals_sign, RIGHT, buff=0.5)
        q_label = MathTex("Q", font_size=36).next_to(q_matrix, UP, buff=0.3)
        
        self.play(Write(mult_symbol), Write(equals_sign))
        self.play(Create(q_matrix), Write(q_label))
        
        # Highlight multiplication process
        # For each row in X (2 rows)
        for i in range(2):
            x_row = matrix_X[i]  # Get current row of X
            # For each column in W_Q (3 columns)
            for j in range(3):
                # Highlight current row from X
                input_box = SurroundingRectangle(x_row, buff=0, color=RED)
                
                # Highlight current column from W_Q
                w_q_column = VGroup(*[row[j] for row in w_q])
                column_box = SurroundingRectangle(w_q_column, buff=0, color=RED)
                
                # Highlight corresponding element in Q
                result_element = q_matrix[i][j]
                result_box = SurroundingRectangle(result_element, buff=0, color=RED)
                
                # Show the dot product operation
                self.play(
                    Create(input_box),
                    Create(column_box),
                    Create(result_box)
                )
                self.wait(0.5)
                self.play(
                    FadeOut(input_box),
                    FadeOut(column_box),
                    FadeOut(result_box)
                )
        # Show K and V calculations
        self.wait(1)
        
        # Switch to K
        self.play(
            FadeOut(w_q_label),
            FadeOut(q_label),
            FadeOut(q_matrix),
            FadeOut(w_q),
        )
        k_label = MathTex("K", font_size=36).next_to(q_matrix, UP, buff=0.3)
        w_k_label_new = w_k_label.copy().next_to(w_q, UP)
        self.play(
            FadeIn(w_k_label_new),
            FadeIn(k_label),
            FadeIn(w_k),
            FadeIn(k_matrix),
        )
        
        # Switch to V
        self.wait(1)
        self.play(
            FadeOut(w_k_label_new),
            FadeOut(k_label),
            FadeOut(w_k),
            FadeOut(k_matrix),
        )
        v_label = MathTex("V", font_size=36).next_to(q_matrix, UP, buff=0.3)
        w_v_label_new = w_v_label.copy().next_to(w_q, UP)
        self.play(
            FadeIn(w_v_label_new),
            FadeIn(v_label),
            FadeIn(w_v),
            FadeIn(v_matrix),
        )
        
        self.wait(1)
        
        # Clear multiplication elements but keep result matrix
        self.play(
            FadeOut(VGroup(
                matrix_X, x_label, w_v_label_new,
                mult_symbol, equals_sign, v_matrix, w_v, v_label
            ))
        )

        self.wait(2)

        # Move Q matrix to the left
    
        q_matrix.move_to(LEFT*2)
        q_label.next_to(q_matrix, UP, buff=0.3)

        # Create K matrix
        k_matrix.next_to(q_matrix, RIGHT, buff=1)
        k_label = MathTex("K", font_size=36).next_to(k_matrix, UP, buff=0.3)

        # Create V matrix
        v_matrix.next_to(k_matrix, RIGHT, buff=1)
        v_label_final = MathTex("V", font_size=36).next_to(v_matrix, UP, buff=0.3)

        # Show K and V matrices
        self.play(
            FadeIn(q_matrix),
            FadeIn(q_label),
            FadeIn(k_matrix),
            FadeIn(k_label),
            FadeIn(v_matrix),
            FadeIn(v_label_final),
        )

        self.wait(2)
        self.play(
            FadeOut(v_matrix),
            FadeOut(v_label_final)
        )

        k_transpose_label = MathTex("K^T", font_size=36).next_to(k_matrix, UP, buff=0.3)
        k_matrix_transpose = k_matrix.copy().rotate(PI/2).move_to(k_matrix.get_center())
        self.play(
            FadeOut(k_label),
            FadeOut(k_matrix),
        )

        self.wait(0.5)

        self.play(
            FadeIn(k_transpose_label.next_to(k_matrix_transpose, UP, buff=0.3)),
            FadeIn(k_matrix_transpose),
        )
        # After your matrix animations (keeping k_matrix and v_matrix_transpose in their positions)

        # First, let's create a VGroup with the existing matrices to help with positioning
        matrix_group = VGroup(q_matrix, k_matrix_transpose)

        # Create multiplication symbol between matrices
        mult_symbol = MathTex("\\times", font_size=36)
        mult_symbol.move_to(
            (q_matrix.get_right() + k_matrix_transpose.get_left())/2
        )

        # Calculate the width needed for the division line
        total_width = matrix_group.get_width()  # Add some padding
        division_line = Line(LEFT*total_width/2, RIGHT*total_width/2, color=WHITE)
        division_line.next_to(matrix_group.get_center(), DOWN*2, buff=0.5)

        # Create and position root_dk
        root_dk = MathTex("\\sqrt{d_k}", font_size=48)
        root_dk.next_to(division_line, DOWN, buff=0.3)

        # Create appropriately sized parentheses
        total_height = matrix_group.get_height() + division_line.get_height() + 1.5
        left_paren = MathTex("(", font_size=120).scale(total_height/2)
        right_paren = MathTex(")", font_size=120).scale(total_height/2)

        # Position parentheses to encompass matrices and division
        left_edge = matrix_group.get_left() + LEFT*0.5
        right_edge = matrix_group.get_right() + RIGHT*0.5 

        left_paren.next_to(left_edge, LEFT + DOWN*0.25, buff=0.2)
        right_paren.next_to(right_edge, RIGHT + DOWN*0.25, buff=0.2)


        # Create and position softmax
        softmax = Text("Softmax", font_size=36)
        softmax.next_to(left_paren, LEFT, buff=0.3)

        # Animate everything smoothly
        self.play(
            Write(mult_symbol),
            run_time=1
        )

        self.play(
            Create(division_line),
            Write(root_dk),
            run_time=1.5
        )

        self.play(
            Create(left_paren),
            Create(right_paren),
            run_time=1
        )

        self.play(
            Write(softmax),
            run_time=1
        )

        self.wait(2)

        # After your last self.wait(2)

        # Create V matrix with same dimensions as before
        v_final_matrix = v_matrix.copy()  # Using the original v_matrix dimensions
        v_final_matrix.next_to(right_paren, RIGHT, buff=1)
        v_label_new = MathTex("V", font_size=36).next_to(v_final_matrix, UP, buff=0.3)

        # Create multiplication symbol for V
        mult_symbol_v = MathTex("\\times", font_size=36)
        mult_symbol_v.next_to(right_paren, RIGHT, buff=0.5)

        # Show V matrix and multiplication symbol
        self.play(
            FadeIn(v_final_matrix),
            FadeIn(v_label_new),
            Write(mult_symbol_v),
            run_time=1
        )

        # Create equals sign
        equals_sign.next_to(v_final_matrix, RIGHT, buff=0.5)

        # Create Z matrix (should be same dimensions as Q)
        z_matrix = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0)
            for _ in range(2)
        ]).arrange(DOWN, buff=0)  # Using the dimensions from your q_matrix
        z_matrix.next_to(ORIGIN + LEFT, buff=0.5)
        z_label = MathTex("Z", font_size=36).next_to(z_matrix, UP, buff=0.3)

        self.wait(2)

        group_everything = VGroup(
            matrix_group, mult_symbol, division_line, root_dk,
            left_paren, right_paren, softmax, v_final_matrix,
            v_label_new, mult_symbol_v, k_transpose_label, q_label,
        )

        group_z_matrix = VGroup(z_matrix, z_label)

        # Show equals sign and Z matrix
        self.play(
            ReplacementTransform(group_everything, group_z_matrix),
        )

        self.wait(2)

        # After your last self.wait(2)

        # First, transform Z to Z1
        z1_label = MathTex("Z_1", font_size=36).next_to(z_matrix, UP, buff=0.3)
        self.play(
            ReplacementTransform(z_label, z1_label)
        )

        # Move Z1 to absolute left
        self.play(
            VGroup(z_matrix, z1_label).animate.shift(LEFT*4)
        )

        # Create Z2 through Z5 with labels
        z_matrices = []
        z_labels = []

        # Create 4 more Z matrices with labels
        for i in range(2, 5):
            new_z = z_matrix.copy()
            new_z_label = MathTex(f"Z_{i}", font_size=36)
            
            # Position each new Z matrix to the right of the previous one
            if i == 2:
                new_z.next_to(z_matrix, RIGHT, buff=1)
            else:
                new_z.next_to(z_matrices[-1], RIGHT, buff=1)
            
            new_z_label.next_to(new_z, UP, buff=0.3)
            
            z_matrices.append(new_z)
            z_labels.append(new_z_label)
            
            # Animate each new Z appearing
            self.play(
                FadeIn(new_z),
                FadeIn(new_z_label),
                run_time=0.5
            )

        self.wait(2)
        # After creating all Z matrices
        # First create a horizontal group of Z matrices with proper sizing
        all_z_matrices = VGroup(z_matrix, *z_matrices)
        all_z_labels = VGroup(z1_label, *z_labels)
        self.play(
            all_z_matrices.animate.arrange(RIGHT, buff=0),
            all_z_labels.animate.arrange(RIGHT, buff=1.2).next_to(all_z_matrices, UP, buff=0.2),
        )

        self.play(
            all_z_matrices. animate.move_to(ORIGIN + LEFT*2.75),
            all_z_labels.animate.move_to(ORIGIN + UP*0.85 + LEFT*2.75),
        )


        # Create WO matrix with smaller squares
        def create_wo_matrix():
            return VGroup(*[
                VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
                for _ in range(12)
            ]).arrange(DOWN, buff=0)

        wo_matrix = create_wo_matrix()

        # Position WO matrix to the right with proper spacing
        wo_matrix.next_to(all_z_matrices, RIGHT, buff=1)

        # Create multiplication symbol
        mult_symbol_wo = MathTex("\\times", font_size=36)
        mult_symbol_wo.move_to(
            (all_z_matrices.get_right() + wo_matrix.get_left())/2
        )

        # Create final Z matrix (2×4 dimension)
        final_z = VGroup(*[
            VGroup(*[Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.5) for _ in range(4)]).arrange(RIGHT, buff=0)
            for _ in range(2)
        ]).arrange(DOWN, buff=0)

        # Create equals sign and position final Z
        equals_sign = MathTex("=", font_size=36)
        equals_sign.next_to(wo_matrix, RIGHT, buff=0.5)
        final_z.next_to(equals_sign, RIGHT, buff=0.5)
        final_z_label = MathTex("Z", font_size=36).next_to(final_z, UP, buff=0.3)

        # Add text with better positioning
        text1 = Text("Join all the attention heads results", font_size=30)
        text1.next_to(all_z_matrices, UP, buff=1.5)
        wo_label = MathTex("W^O", font_size=36).next_to(wo_matrix, UP, buff=0.3)

        # Animate everything
        self.play(
            Write(text1)
        )

        self.play(
            FadeIn(wo_matrix),
            FadeIn(wo_label),
            Write(mult_symbol_wo)
        )

        self.play(
            Write(equals_sign),
            FadeIn(final_z),
            FadeIn(final_z_label)
        )

        self.wait(2)
        
        self.play(
            FadeOut(VGroup(
                all_z_matrices, all_z_labels, wo_matrix, wo_label, mult_symbol_wo,
                equals_sign, text1
            ))
        )
        self.wait(1)
        self.play(
            final_z.animate.move_to(ORIGIN),
            final_z_label.animate.move_to(ORIGIN + UP)
        )



class MatrixRepresentation(Scene):
    def construct(self):
        # Create the axes and grid with adjusted ranges
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 3],
            axis_config={
                "color": BLUE,
                "include_numbers": False,
                "include_ticks": False
            },
            x_length=7,
            y_length=7,
            tips=True
        )
        
        # Create the [Y,X] vector notation
        vector_notation = MathTex(r"\begin{bmatrix} Y \\ X \end{bmatrix}").to_corner(UR, buff=0.5)
        
        # Create PNG images and position them
        point_coords = [(1, 1), (2, 1), (1, 2), (2, 2)]
        image_files = ["assets/market.png", "assets/Apple_logo.png", "assets/apple.png", "assets/phone.png"]
        ImageMobject(image_files[1]).scale(0.3)
        
        # Use Group instead of VGroup for images
        points = Group()
        for coord, img_file in zip(point_coords, image_files):
            image = ImageMobject(img_file)
            if img_file == "assets/Apple_logo.png":
                image.scale(0.3)
            image.scale(0.4)
            image.move_to(axes.c2p(*coord))
            points.add(image)
        
        # Group axes and points using Group instead of VGroup
        everything = Group(axes, points)
        
        # Animation sequence
        self.play(Create(axes), run_time=2)
        self.wait(0.5)
        
        self.play(Write(vector_notation), run_time=1)
        self.wait(0.5)
        
        self.play(FadeIn(points), run_time=1)
        self.wait(0.5)
        
        # Scale and position everything
        self.play(
            everything.animate.scale(0.35).move_to(ORIGIN + UP*1.5),
        )
        
        # Create first copy
        copied_group = Group(axes.copy(), points.copy())
        text1 = Text("Representation 1", font_size=36).next_to(copied_group, DOWN*6.25 + LEFT*4, buff=0.5)
        self.play(
            copied_group.animate.shift(DOWN*3 + LEFT*5),
            Write(text1),
            run_time=2
        )

        # First transformation
        matrix1 = [[1, -1], [0, 1]]
        notation1 = MathTex(r"\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}").next_to(vector_notation, LEFT, buff=0.5)
        self.play(FadeIn(notation1))

        # Apply transformation to axes
        self.play(axes.animate.apply_matrix(matrix1), run_time=2)
        
        # Calculate new positions for all points
        animations = []
        for point in points:
            old_pos = axes.p2c(point.get_center())
            new_x = matrix1[0][0] * old_pos[0] + matrix1[0][1] * old_pos[1]
            new_y = matrix1[1][0] * old_pos[0] + matrix1[1][1] * old_pos[1]
            animations.append(point.animate.move_to(axes.c2p(new_x, new_y) + UP*1.2 + LEFT*0.5))
        
        # Move all points simultaneously
        self.play(*animations, run_time=2)

        # Create second copy
        copied_group2 = Group(axes.copy(), points.copy())
        text2 = Text("Representation 2", font_size=36).next_to(text1, RIGHT*2, buff=0.5)
        self.play(
            copied_group2.animate.shift(DOWN*3),
            Write(text2),
            run_time=2
        )

        # Second transformation
        matrix2 = [[1, 1.5], [0, 1]]
        notation2 = MathTex(r"\begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix}").next_to(vector_notation, LEFT, buff=0.5)
        self.play(
            FadeOut(notation1),
            FadeIn(notation2)
        )

        # Apply second transformation to axes
        self.play(axes.animate.apply_matrix(matrix2), run_time=2)
        
        # Calculate and apply second transformation to all points simultaneously
        animations = []
        for point in points:
            old_pos = axes.p2c(point.get_center())
            new_x = matrix2[0][0] * old_pos[0] + matrix2[0][1] * old_pos[1]
            new_y = matrix2[1][0] * old_pos[0] + matrix2[1][1] * old_pos[1]
            animations.append(point.animate.move_to(axes.c2p(new_x, new_y) + LEFT*0.7))
        
        self.play(*animations, run_time=2)

        # Create third copy
        copied_group3 = Group(axes.copy(), points.copy())
        text3 = Text("Representation 3", font_size=36).next_to(text2, RIGHT*2, buff=0.5)
        self.play(
            copied_group3.animate.shift(DOWN*3 + RIGHT*3.5),
            Write(text3),
            run_time=2
        )
        
        self.wait(2)

        self.play(
            FadeOut(Group(copied_group, copied_group2, copied_group3, text1, text2, text3, vector_notation, notation2, everything))
        )

        self.wait(1)

        question_1 = Text("Where can I buy an apple to eat?", font_size=24)
        question_2 = Text("Who makes the iphones?", font_size=24)
        question_3 = Text("Where can I buy an iphone?", font_size=24)

        question_1.move_to(ORIGIN + UP)
        question_2.move_to(ORIGIN + DOWN)

        self.play(Write(question_1))
        self.wait(1)
        self.play(Write(question_2))

        self.play(
            question_1.animate.shift(DOWN*2),
            question_2.animate.shift(DOWN)
        )
        self.play(FadeIn(copied_group3.move_to(ORIGIN + UP*2), text3.next_to(copied_group3, DOWN, buff=0.5)))

        self.wait(1)

        self.play(FadeOut(Group(question_1, question_2), copied_group3, text3))

        self.play(Write(question_3))
        self.wait(1)
        self.play(question_3.animate.shift(DOWN*2))
        self.play(FadeIn(copied_group2.move_to(ORIGIN + UP*2), text3.next_to(copied_group2, DOWN, buff=0.5)))

        self.wait(1)
        self.play(FadeOut(Group(question_3), text3))

        self.wait(2)
        self.play(ReplacementTransform(copied_group2, copied_group.move_to(ORIGIN)), run_time=3)
        self.wait(2)
        self.play(FadeOut(copied_group))