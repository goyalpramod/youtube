from manim import *

class CNNExplanation(Scene):
    def construct(self):
        # Colors
        BLUE_DARK = "#1F4788"
        GREEN_DARK = "#2C5A2B"
        RED_DARK = "#8B0000"
        
        # Create neural network layers
        input_layer = self.create_layer(6, BLUE_DARK, "Input Image\n(28x28)")
        conv_layer1 = self.create_layer(5, GREEN_DARK, "Conv Layer 1\n(3x3 Kernel)")
        relu_layer = self.create_layer(5, RED_DARK, "ReLU")
        pool_layer = self.create_layer(4, BLUE_DARK, "Max Pooling\n(2x2)")
        conv_layer2 = self.create_layer(3, GREEN_DARK, "Conv Layer 2\n(3x3 Kernel)")
        output_layer = self.create_layer(1, RED_DARK, "Output\n(10 Classes)")

        # Position layers
        layers = VGroup(input_layer, conv_layer1, relu_layer, pool_layer, conv_layer2, output_layer)
        layers.arrange(RIGHT, buff=1.5)
        layers.shift(UP * 0.5)

        # Create connections
        connections = VGroup()
        for l1, l2 in zip(layers[:-1], layers[1:]):
            connections.add(self.create_connections(l1, l2))

        # Animation sequence
        self.play(Write(input_layer))
        self.wait(0.5)
        
        # Animate Conv Layer 1
        self.play(
            input_layer.animate.set_fill(opacity=0.3),
            FadeIn(conv_layer1, shift=RIGHT),
            Create(connections[0]),
            run_time=2
        )
        self.show_conv_operation(input_layer, conv_layer1)
        
        # Animate ReLU
        self.play(
            conv_layer1.animate.set_fill(opacity=0.3),
            FadeIn(relu_layer, shift=RIGHT),
            Create(connections[1]),
            run_time=2
        )
        self.show_activation(conv_layer1, relu_layer)
        
        # Animate Pooling
        self.play(
            relu_layer.animate.set_fill(opacity=0.3),
            FadeIn(pool_layer, shift=RIGHT),
            Create(connections[2]),
            run_time=2
        )
        self.show_pooling(relu_layer, pool_layer)
        
        # Animate Conv Layer 2
        self.play(
            pool_layer.animate.set_fill(opacity=0.3),
            FadeIn(conv_layer2, shift=RIGHT),
            Create(connections[3]),
            run_time=2
        )
        
        # Animate Output
        self.play(
            conv_layer2.animate.set_fill(opacity=0.3),
            FadeIn(output_layer, shift=RIGHT),
            Create(connections[4]),
            run_time=2
        )
        self.wait(2)

    def create_layer(self, size, color, label_text):
        layer = VGroup()
        nodes = VGroup(*[Circle(radius=0.2, color=color, fill_opacity=0.7) for _ in range(size**2)])
        nodes.arrange_in_grid(rows=size, cols=size, buff=0.3)
        label = Text(label_text, font_size=18).next_to(nodes, DOWN)
        return VGroup(nodes, label)

    def create_connections(self, layer1, layer2):
        connections = VGroup()
        for node1 in layer1[0]:
            for node2 in layer2[0]:
                connections.add(Line(node1.get_center(), node2.get_center(), 
                                   color=GREY_B, stroke_width=0.7, 
                                   stroke_opacity=0.3))
        return connections

    def show_conv_operation(self, input_layer, conv_layer):
        # Create kernel visualization
        kernel = VGroup(*[Square(side_length=0.4, color=YELLOW, fill_opacity=0.3) 
                        for _ in range(9)]).arrange_in_grid(3, 3, buff=0)
        kernel.move_to(input_layer[0][0].get_center())
        
        # Create feature map
        feature_map = conv_layer[0].copy()
        feature_map.set_fill(opacity=0)
        
        self.play(Create(kernel))
        self.wait(0.5)
        
        # Animate kernel sliding
        for i, node in enumerate(conv_layer[0]):
            target_pos = input_layer[0][i].get_center() + RIGHT*0.5 + DOWN*0.5
            self.play(kernel.animate.move_to(target_pos), run_time=0.3)
            
            # Highlight corresponding feature map node
            self.play(
                feature_map[i].animate.set_fill(opacity=0.7),
                node.animate.set_fill(opacity=0.7),
                run_time=0.5
            )
        
        self.play(FadeOut(kernel))
        self.wait()

    def show_activation(self, input_layer, activation_layer):
        # Create ReLU graph
        axes = Axes(x_range=[-2, 2], y_range=[-1, 3], axis_config={"color": WHITE})
        relu_graph = axes.plot(lambda x: max(x, 0), color=RED)
        graph_group = VGroup(axes, relu_graph).scale(0.4).next_to(activation_layer, UP)
        
        self.play(Create(graph_group))
        self.wait(0.5)
        
        # Animate activation on nodes
        for node_in, node_out in zip(input_layer[0], activation_layer[0]):
            self.play(
                node_in.animate.set_fill(opacity=0.7),
                node_out.animate.set_fill(opacity=0.7),
                run_time=0.1
            )
        self.wait()
        self.play(FadeOut(graph_group))

    def show_pooling(self, input_layer, pool_layer):
        # Create pooling window
        pool_window = VGroup(*[Square(side_length=0.8, color=BLUE, fill_opacity=0.2) 
                             for _ in range(4)]).arrange_in_grid(2, 2, buff=0)
        pool_window.move_to(input_layer[0][0].get_center())
        
        self.play(Create(pool_window))
        self.wait(0.5)
        
        # Animate pooling operation
        for i, node in enumerate(pool_layer[0]):
            self.play(pool_window.animate.move_to(input_layer[0][i*2].get_center()))
            
            # Highlight max value
            max_node = input_layer[0][i*2]
            self.play(
                max_node.animate.set_fill(opacity=1),
                node.animate.set_fill(opacity=0.7),
                run_time=0.5
            )
        
        self.play(FadeOut(pool_window))
        self.wait()

from manim import *
import numpy as np

class CNNExplanation2(Scene):
    def construct(self):
        # Configuration
        self.camera.background_color = "#2D3436"
        
        # Title
        title = Text("Convolutional Neural Networks", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait()

        # Input Image Representation
        input_image = self.create_pixel_grid(5, 5, color=BLUE)
        input_image.move_to(LEFT * 4)
        input_label = Text("Input", font_size=36).next_to(input_image, DOWN)
        
        self.play(
            Create(input_image),
            Write(input_label)
        )
        self.wait()

        # Convolution Kernel
        kernel = self.create_pixel_grid(3, 3, scale=0.5, color=YELLOW)
        kernel.next_to(input_image, RIGHT, buff=1)
        kernel_label = Text("Kernel", font_size=36).next_to(kernel, DOWN)
        
        self.play(
            Create(kernel),
            Write(kernel_label)
        )
        self.wait()

        # Convolution Animation
        conv_result = self.create_pixel_grid(3, 3, color=GREEN)
        conv_result.next_to(kernel, RIGHT, buff=1)
        conv_label = Text("Feature Map", font_size=36).next_to(conv_result, DOWN)
        
        # Animate convolution window
        highlight = Square(
            side_length=3 * input_image.height / 5,
            color=RED,
            stroke_width=2
        )
        highlight.move_to(input_image.get_center())
        
        self.play(Create(highlight))
        self.play(
            highlight.animate.shift(RIGHT * 0.4 + UP * 0.4),
            run_time=2
        )
        
        self.play(
            Create(conv_result),
            Write(conv_label)
        )
        self.wait()

        # ReLU Activation
        relu_arrow = Arrow(
            conv_result.get_right(),
            conv_result.get_right() + RIGHT * 2,
            color=WHITE
        )
        relu_text = Text("ReLU", font_size=36).next_to(relu_arrow, UP)
        
        relu_result = self.create_pixel_grid(3, 3, color=PURPLE)
        relu_result.next_to(relu_arrow, RIGHT)
        
        self.play(
            Create(relu_arrow),
            Write(relu_text)
        )
        self.play(Create(relu_result))
        self.wait()

        # Max Pooling
        pool_arrow = Arrow(
            relu_result.get_right(),
            relu_result.get_right() + RIGHT * 2,
            color=WHITE
        )
        pool_text = Text("Max Pooling", font_size=36).next_to(pool_arrow, UP)
        
        pool_result = self.create_pixel_grid(2, 2, color=RED)
        pool_result.next_to(pool_arrow, RIGHT)
        
        self.play(
            Create(pool_arrow),
            Write(pool_text)
        )
        self.play(Create(pool_result))
        self.wait(2)

        # Final fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def create_pixel_grid(self, rows, cols, scale=1.0, color=WHITE):
        """Create a grid of squares representing pixels"""
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                square = Square(
                    side_length=0.5 * scale,
                    stroke_width=2,
                    color=color
                )
                square.move_to([j * 0.5 * scale, -i * 0.5 * scale, 0])
                grid.add(square)
        return grid

class ConvolutionDetail(Scene):
    def construct(self):
        # Show detailed convolution operation
        title = Text("Convolution Operation", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create input matrix
        input_values = np.array([
            [1, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 2, 1],
            [0, 1, 1, 0]
        ])
        
        kernel_values = np.array([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])
        
        # Create and animate matrices
        input_matrix = self.create_matrix(input_values, color=BLUE)
        kernel_matrix = self.create_matrix(kernel_values, color=YELLOW, scale=0.7)
        
        input_matrix.move_to(LEFT * 4)
        kernel_matrix.next_to(input_matrix, RIGHT, buff=1)
        
        self.play(Create(input_matrix))
        self.play(Create(kernel_matrix))
        self.wait()
        
        # Show convolution calculation
        highlight = Rectangle(
            width=1.5,
            height=1.5,
            color=RED,
            stroke_width=2
        )
        highlight.move_to(input_matrix.get_center())
        
        calculation = MathTex(
            r"\sum_{i,j} (input_{i,j} \times kernel_{i,j})",
            font_size=36
        )
        calculation.next_to(kernel_matrix, RIGHT, buff=1)
        
        self.play(
            Create(highlight),
            Write(calculation)
        )
        self.wait(2)
        
        # Final fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def create_matrix(self, values, scale=1.0, color=WHITE):
        """Create a matrix visualization with numbers"""
        matrix = VGroup()
        rows, cols = values.shape
        
        for i in range(rows):
            for j in range(cols):
                square = Square(
                    side_length=0.5 * scale,
                    stroke_width=2,
                    color=color
                )
                square.move_to([j * 0.5 * scale, -i * 0.5 * scale, 0])
                number = Text(
                    str(values[i, j]),
                    font_size=24 * scale
                ).move_to(square.get_center())
                matrix.add(VGroup(square, number))
        
        return matrix

class CNNArchitecture(Scene):
    def construct(self):
        # Show full CNN architecture
        title = Text("CNN Architecture", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create layers
        layers = VGroup()
        
        # Input layer
        input_layer = Rectangle(height=4, width=0.5, color=BLUE)
        input_text = Text("Input", font_size=24).next_to(input_layer, DOWN)
        
        # Convolutional layers
        conv_layers = VGroup()
        for _ in range(2):
            layer = Rectangle(height=3.5, width=0.5, color=GREEN)
            conv_layers.add(layer)
        conv_layers.arrange(RIGHT, buff=1)
        conv_text = Text("Conv Layers", font_size=24).next_to(conv_layers, DOWN)
        
        # Pooling layers
        pool_layers = VGroup()
        for _ in range(2):
            layer = Rectangle(height=2.5, width=0.5, color=RED)
            pool_layers.add(layer)
        pool_layers.arrange(RIGHT, buff=1)
        pool_text = Text("Pool Layers", font_size=24).next_to(pool_layers, DOWN)
        
        # Fully connected layers
        fc_layers = VGroup()
        heights = [2, 1.5, 1]
        for h in heights:
            layer = Rectangle(height=h, width=0.5, color=PURPLE)
            fc_layers.add(layer)
        fc_layers.arrange(RIGHT, buff=1)
        fc_text = Text("FC Layers", font_size=24).next_to(fc_layers, DOWN)
        
        # Arrange all layers
        layers.add(input_layer, conv_layers, pool_layers, fc_layers)
        layers.arrange(RIGHT, buff=2)
        
        # Add connecting arrows
        arrows = VGroup()
        for i in range(len(layers) - 1):
            arrow = Arrow(
                layers[i].get_right(),
                layers[i + 1].get_left(),
                color=WHITE
            )
            arrows.add(arrow)
        
        # Animate
        self.play(Create(input_layer), Write(input_text))
        self.play(Create(conv_layers), Write(conv_text))
        self.play(Create(pool_layers), Write(pool_text))
        self.play(Create(fc_layers), Write(fc_text))
        self.play(Create(arrows))
        self.wait(2)
        
        # Final fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )