# ruff: noqa
from manim import *

# NEW: A mixin class to handle loading and styling of all SVG assets
class NNMediaMixin:
    def setup_svgs(self):
        """Loads, scales, and styles all SVG mobjects for the scenes."""
        self.complex_nn = SVGMobject(r"media/excalidraw_exports/complex_nn.svg").scale(3)
        self.simple_nn = SVGMobject(r"media/excalidraw_exports/simple_nn.svg").scale(3)
        self.simplest_nn = SVGMobject(r"media/excalidraw_exports/simplest_nn.svg")
        self.big_hidden_node = SVGMobject(r"media/excalidraw_exports/big_hidden_node.svg").scale(2.5)
        self.black_dot = SVGMobject(r"media/excalidraw_exports/black_dot.svg").scale(3)
        self.hidden_node = SVGMobject(r"media/excalidraw_exports/hidden_node.svg").scale(3)
        self.input_node = SVGMobject(r"media/excalidraw_exports/input_node.svg").scale(3)
        self.output_node = SVGMobject(r"media/excalidraw_exports/output_node.svg").scale(3)
        self.white_dot = SVGMobject(r"media/excalidraw_exports/white_dot.svg").scale(3)

        # Style all the mobjects in one go
        for mob in [self.complex_nn, self.simple_nn, self.simplest_nn, self.big_hidden_node, 
                    self.black_dot, self.hidden_node, self.input_node, self.output_node, self.white_dot]:
            mob.set_stroke(width=2)
            mob.set_fill(opacity=0.7)



# MODIFIED: The class now inherits from the mixin
class ComplexToSimpleNN(NNMediaMixin, Scene):
    def construct(self):
        # MODIFIED: Call the setup method from the mixin
        self.setup_svgs()
        
        # MODIFIED: Use the instance variables (self.complex_nn, etc.)
        self.play(DrawBorderThenFill(self.complex_nn))
        self.wait(1)

        self.play(ReplacementTransform(self.complex_nn, self.simple_nn))
        self.wait(2)
        
        self.play(ReplacementTransform(self.simple_nn, self.simplest_nn))
        self.wait(2)

        self.play(ReplacementTransform(self.simplest_nn, self.big_hidden_node))
        self.wait(2)


# MODIFIED: The class now inherits from the mixin
class ExplainingHiddenNodes(NNMediaMixin, Scene):
    def construct(self):
        # MODIFIED: Call the setup method from the mixin
        self.setup_svgs()
        
        # The scene starts with big_hidden_node already on screen
        self.add(self.big_hidden_node)

        # Label the Node Halves
        linear_label = Text("Linear\nFunction", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        activation_label = Text("Activation\nFunction", font="Virgil 3 YOFF", font_size=24, color=BLACK)

        linear_label.move_to(self.big_hidden_node.get_center() + LEFT * 1)
        activation_label.move_to(self.big_hidden_node.get_center() + RIGHT * 1)

        self.play(Write(linear_label))
        self.wait(1)
        self.play(Write(activation_label))
        self.wait(1)

        # Display the Linear Equation
        linear_eq = MathTex("y = w \\cdot x + b", color=BLACK).scale(1)
        linear_eq.next_to(self.big_hidden_node, LEFT, buff=1)
        self.play(Write(linear_eq))
        self.wait(1)

        acitvation_function = MathTex("Z(y)", color=BLACK).scale(1)

        acitvation_function.next_to(self.big_hidden_node, RIGHT, buff=1)
        self.play(Write(acitvation_function))
        self.wait(2)

        # # Display the Activation Rule
        # rule_text = Text(
        #     "if y > 127: out = 1\nelse: out = 0",
        #     font="Virgil 3 YOFF", font_size=24, line_spacing=1, color=BLACK
        # )
        # rule_text.next_to(self.big_hidden_node, RIGHT, buff=0.7)
        # self.play(Write(rule_text))
        # self.wait(1)

        # # Draw the Step Function Plot
        # axes = Axes(
        #     x_range=[0, 260, 50],
        #     y_range=[-0.2, 1.2, 1],
        #     x_length=4,
        #     y_length=2,
        #     # MODIFIED: Set axis and label colors to BLACK
        #     axis_config={"include_tip": False, "color": BLACK},
        #     x_axis_config={},
        #     y_axis_config={},
        # ).next_to(rule_text, UP, buff=0.5)

        # axis_labels = axes.get_axis_labels(x_label="y", y_label="out").set_color(BLACK)
        
        # # MODIFIED: Set color for Tex objects
        # t_127 = Tex("127", color=BLACK).next_to(axes.c2p(127, 0), DOWN, buff=0.1).scale(0.4)
        # t_1 = Tex("1", color=BLACK).next_to(axes.c2p(0, 1), LEFT, buff=0.1).scale(0.4)

        # step_function = axes.plot(
        #     lambda x: 1 if x >= 127 else 0, 
        #     x_range=[0, 255], 
        #     use_smoothing=False
        # )
        # step_function.set_color(YELLOW)

        # self.play(Create(axes), Write(axis_labels))
        # self.play(Write(t_127), Write(t_1))
        # self.play(Create(step_function))
        # self.wait(3)

class ExampleWithDots(NNMediaMixin, Scene):
    def construct(self):
        # MODIFIED: Call the setup method from the mixin
        self.setup_svgs()
        
        # The scene starts with simplest_nn already on screen
        self.add(self.simplest_nn)

        # Introduce Input Node
        input_node = self.input_node.copy().move_to(self.simplest_nn.get_left() + LEFT * 1)
        self.play(DrawBorderThenFill(input_node))
        self.wait(1)

        input_label = Text("Input Node", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        input_label.next_to(input_node, DOWN, buff=0.2)
        self.play(Write(input_label))
        self.wait(1)

        # Introduce Output Node
        output_node = self.output_node.copy().move_to(self.simplest_nn.get_right() + RIGHT * 1)
        self.play(DrawBorderThenFill(output_node))
        self.wait(1)

        output_label = Text("Output Node", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        output_label.next_to(output_node, DOWN, buff=0.2)
        self.play(Write(output_label))
        self.wait(1)

        # Introduce Hidden Node
        hidden_node = self.hidden_node.copy().move_to(self.simplest_nn.get_center())
        self.play(DrawBorderThenFill(hidden_node))
        self.wait(1)

        hidden_label = Text("Hidden Node", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        hidden_label.next_to(hidden_node, DOWN, buff=0.2)
        self.play(Write(hidden_label))
        self.wait(2)

        # Show Data Flow with Dots
        dot_path_1 = Line(input_node.get_right(), hidden_node.get_left(), stroke_width=2)
        dot_path_2 = Line(hidden_node.get_right(), output_node.get_left(), stroke_width=2)

        dot1 = self.black_dot.copy().scale(0.5).move_to(input_node.get_right())
        dot2 = self.white_dot.copy().scale(0.5).move_to(hidden_node.get_right())

        self.play(MoveAlongPath(dot1, dot_path_1), run_time=2)
        self.play(MoveAlongPath(dot2, dot_path_2), run_time=2)
        self.wait(2)


class Default(Scene):
    def construct(self):
        text = Text("Indian Explains Neural Networks", font_size=48, color=BLACK, font="Virgil 3 YOFF")
        self.play(Write(text))
        self.wait(2)