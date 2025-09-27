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
        self.black_dot = SVGMobject(r"media/excalidraw_exports/black_dot.svg")
        self.hidden_node = SVGMobject(r"media/excalidraw_exports/hidden_node.svg")
        self.input_node = SVGMobject(r"media/excalidraw_exports/input_node.svg")
        self.output_node = SVGMobject(r"media/excalidraw_exports/output_node.svg")
        self.white_dot = SVGMobject(r"media/excalidraw_exports/white_dot.svg")

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


class ExplainingInputNode(NNMediaMixin, Scene):
    def construct(self):
        # Call the setup method from the mixin to load SVGs
        self.setup_svgs()
        
        # --- Part 1: The Problem (Visual Input) ---

        # Create and position the initial objects
        input_node = self.input_node.copy().move_to(ORIGIN)
        black_dot = self.black_dot.copy().next_to(input_node, LEFT, buff=1.5)
        arrow = Arrow(black_dot.get_right(), input_node.get_left(), buff=0.2, color=BLACK)
        q_mark = Text("?", font="Virgil 3 YOFF", font_size=96, color=BLACK).next_to(input_node, RIGHT, buff=1.5)

        # Animate the appearance
        self.play(FadeIn(input_node), FadeIn(black_dot))
        self.play(GrowArrow(arrow))
        self.play(Write(q_mark))
        self.wait(2)

        # Clear the scene for the next part
        problem_group = VGroup(black_dot, arrow, input_node, q_mark)
        self.play(FadeOut(problem_group))
        self.wait(1)

        # --- Part 2: The Solution (Mapping to Numbers) ---
        
        title = Text("Pixels: Color to Number", font="Virgil 3 YOFF", color=BLACK).to_edge(UP)
        self.play(Write(title))

        # Black dot mapping
        black_dot_small = self.black_dot.copy().scale(0.5)
        num_255 = Text("255", color=BLACK, font="Virgil 3 YOFF").scale(1.5)
        arrow_b = Arrow(black_dot_small.get_right(), num_255.get_left(), buff=0.2, color=BLACK)
        black_mapping = VGroup(black_dot_small, arrow_b, num_255).arrange(RIGHT, buff=0.5)

        # White dot mapping
        white_dot_small = self.white_dot.copy().scale(0.5)
        num_0 = Text("0", color=BLACK, font="Virgil 3 YOFF").scale(1.5)
        arrow_w = Arrow(white_dot_small.get_right(), num_0.get_left(), buff=0.2, color=BLACK)
        white_mapping = VGroup(white_dot_small, arrow_w, num_0).arrange(RIGHT, buff=0.5)

        # Group and position the mappings
        mappings = VGroup(black_mapping, white_mapping).arrange(DOWN, buff=1).move_to(ORIGIN)
        
        # Animate the mappings
        self.play(FadeIn(black_dot_small))
        self.play(GrowArrow(arrow_b), FadeIn(num_255))
        self.wait(0.5)
        self.play(FadeIn(white_dot_small))
        self.play(GrowArrow(arrow_w), FadeIn(num_0))
        self.wait(2)

        # Clear the scene, but keep the number 255
        self.play(FadeOut(title, white_mapping, black_dot_small, arrow_b))
        self.wait(1)

        # --- Part 3: The Correct Input (Numerical Input) ---
        
        # Create the final input node
        input_node_final = self.input_node.copy().move_to(RIGHT * 2)

        # Animate the number moving into position and the node appearing
        self.play(num_255.animate.move_to(LEFT * 2))
        self.play(FadeIn(input_node_final))

        # Final arrow showing correct input
        final_arrow = Arrow(num_255.get_right(), input_node_final.get_left(), buff=0.2, color=BLACK)
        self.play(GrowArrow(final_arrow))
        self.wait(3)
        

class ExplainingHiddenNodes(NNMediaMixin, Scene):
    def construct(self):
        # Call the mixin to set up SVGs
        self.setup_svgs()
        
        # --- Phase 1: Setup ---
        
        node = self.big_hidden_node
        self.add(node)

        linear_label = Text("Linear\nFunction", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        activation_label = Text("Activation\nFunction", font="Virgil 3 YOFF", font_size=24, color=BLACK)
        linear_label.move_to(node.get_center() + LEFT * 1)
        activation_label.move_to(node.get_center() + RIGHT * 1)
        self.play(Write(linear_label))
        self.wait(1)
        self.play(Write(activation_label))
        self.wait(1)

        # Using Tex to avoid LaTeX issues
        generic_linear_eq = Tex("$y = w \\cdot x + b$", color=BLACK).next_to(node, LEFT, buff=1)
        generic_activation_eq = Tex("$Z(y)$", color=BLACK).next_to(node, RIGHT, buff=1)

        self.play(Write(generic_linear_eq))
        self.play(Write(generic_activation_eq))
        self.wait(1)

        # --- Phase 2: Animate the Linear Calculation ---

        # Introduce the input value
        input_text = Text("Input:\nx = 255\nw = 1\nb = 0", font="Virgil 3 YOFF", color=BLACK, font_size=36)
        input_text.next_to(generic_linear_eq, DOWN, buff=0.5)
        self.play(FadeIn(input_text))
        self.wait(1)
        self.play(FadeOut(input_text))
        
        # Create the specific equation and values
        specific_linear_eq = Tex("$y = 1 \\cdot 255 + 0$", color=BLACK).move_to(generic_linear_eq)
        
        # Transform the generic equation into the specific one
        self.play(ReplacementTransform(generic_linear_eq, specific_linear_eq))
        self.wait(1)

        # Simplify the equation
        result_linear_eq = Tex("$y = 255$", color=BLACK).move_to(specific_linear_eq)
        self.play(ReplacementTransform(specific_linear_eq, result_linear_eq))
        self.wait(2)

        # --- Phase 3: Animate the Activation Function ---

        # Extract the number 255 to move it
        y_value = Tex("$ Z(255) $",color=BLACK).move_to(generic_activation_eq)
        self.play(FadeOut(result_linear_eq), ReplacementTransform(generic_activation_eq, y_value))

        # Move the result to the activation side
        self.wait(1)

        # Define the activation rule
        rule_text = Text(
            "if y > 127: out = 1\nelse: out = 0",
            font="Virgil 3 YOFF", font_size=28, line_spacing=1, color=BLACK
        )
        rule_text.move_to(y_value.get_center() + RIGHT * 1)
        
        # Transform the generic function into the specific rule
        self.play(ReplacementTransform(y_value, rule_text))
        self.wait(1)

        # Show the result of the activation
        output_value = Text("1", font="Virgil 3 YOFF", color=BLACK, font_size=48)
        output_value.next_to(rule_text, DOWN, buff=0.5)
        self.play(FadeIn(output_value))
        self.wait(1)
        
        # --- Phase 4: Visualize the Result ---

        axes = Axes(
            x_range=[0, 260, 50], y_range=[-0.2, 1.2, 1],
            x_length=4, y_length=2,
            axis_config={"include_tip": False, "color": BLACK}
        ).next_to(rule_text, UP, buff=0.5)
        axis_labels = axes.get_axis_labels(x_label="y", y_label="out").set_color(BLACK)
        
        step_function = axes.plot(lambda x: 1 if x >= 127 else 0, x_range=[0, 255], use_smoothing=False)
        step_function.set_color(YELLOW)

        # Add a dot to show our specific example on the graph
        dot = Dot(axes.c2p(255, 1), color=RED)
        dot_label = Tex("(255, 1)", color=RED, font_size=36).next_to(dot, UR, buff=0.1)

        self.play(Create(axes), Write(axis_labels))
        self.play(Create(step_function))
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(2)


class ExplainingSimpleNN(NNMediaMixin, Scene):
    def construct(self):
        # Using Tex and Text to avoid LaTeX dependency issues.
        
        # --- Phase 1: Build the Network & Forward Pass Intuition ---

        # Create the network diagram natively
        nn = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 6)],
            layout={
                1: [-4, 1, 0], 2: [-4, -1, 0],
                3: [0, 2, 0], 4: [0, 0, 0], 5: [0, -2, 0],
                6: [4, 0, 0]
            },
            vertex_config={"radius": 0.4, "color": BLACK},
            edge_config={"color": GRAY, "stroke_width": 3}
        )
        
        # Labels for nodes
        inputs = VGroup(Tex("$x_1$", color=BLACK), Tex("$x_2$", color=BLACK))
        hidden = VGroup(Tex("$h_1$", color=BLACK), Tex("$h_2$", color=BLACK), Tex("$h_3$", color=BLACK))
        output = Tex("$\\hat{y}$", color=BLACK)

        for i, label in enumerate(inputs): label.next_to(nn.vertices[i+1], LEFT)
        for i, label in enumerate(hidden): label.next_to(nn.vertices[i+3], RIGHT)
        output.next_to(nn.vertices[6], RIGHT)
        
        self.play(Create(nn), Write(inputs), Write(hidden), Write(output))
        self.wait(1)

        # Focus on the first hidden node
        h1_group = VGroup(nn.vertices[1], nn.vertices[2], nn.vertices[3])
        h1_edges = VGroup(nn.edges[(1,3)], nn.edges[(2,3)])
        self.play(h1_group.animate.set_color(BLUE), h1_edges.animate.set_color(BLUE))

        w11 = Tex("$w_{11}$", color=BLUE, font_size=36).next_to(nn.edges[(1,3)], UP, buff=-0.6)
        w12 = Tex("$w_{12}$", color=BLUE, font_size=36).next_to(nn.edges[(2,3)], DOWN, buff=-0.7)
        b1 = Tex("$b_1$", color=BLUE, font_size=36).move_to(nn.vertices[3])
        self.play(Write(w11), Write(w12), Write(b1))
        self.wait(2)

        # --- Phase 2: From Single Equation to Matrix Form ---

        # Show single node equation
        single_eq = Tex("$h_1 = Z(w_{11}x_1 + w_{12}x_2 + b_1)$", color=BLACK)
        single_eq.to_edge(UP)
        self.play(Write(single_eq))
        self.wait(2)

        # Revert colors and fade weights
        self.play(
            h1_group.animate.set_color(BLACK), h1_edges.animate.set_color(GRAY),
            FadeOut(w11), FadeOut(w12), FadeOut(b1)
        )
        
        # Transform to matrix equation
        matrix_eq = Tex("$\\vec{h} = Z(W \\cdot \\vec{x} + \\vec{b})$", color=BLACK).to_edge(UP)
        self.play(ReplacementTransform(single_eq, matrix_eq))
        self.wait(1)

        # --- Phase 3: The Gist of Backpropagation ---


        # Show prediction vs target
        prediction = Tex("$\\hat{y}=0.2$", color=RED).next_to(nn.vertices[6], UP, buff=0.5)
        target = Tex("$y=1$", color=GREEN).next_to(prediction, RIGHT, buff=0.5)
        self.play(Write(prediction), Write(target))
        
        loss_text = Text("High Loss!", color=RED).next_to(VGroup(prediction, target), UP)
        self.play(Write(loss_text))
        self.wait(1)
        
        # Animate backward flow
        arrow1 = Arrow(loss_text.get_bottom(), output.get_top(), color=RED, buff=0.2)
        self.play(GrowArrow(arrow1))
        
        output_edges = VGroup(nn.edges[(3,6)], nn.edges[(4,6)], nn.edges[(5,6)])
        self.play(output_edges.animate.set_color(RED), Wiggle(output_edges))

        arrow2 = Arrow(output.get_left(), hidden.get_right(), color=RED, buff=0.2)
        self.play(ReplacementTransform(arrow1, arrow2))
        
        hidden_edges = VGroup(nn.edges[(1,3)], nn.edges[(1,4)], nn.edges[(1,5)], nn.edges[(2,3)], nn.edges[(2,4)], nn.edges[(2,5)])
        self.play(hidden_edges.animate.set_color(RED), Wiggle(hidden_edges))
        self.wait(1)
        
        # Show loss decreasing
        new_loss_text = Text("Weights Updated\nLoss Decreases", color=GREEN, font_size=36, line_spacing=1).move_to(loss_text)
        self.play(
            FadeOut(arrow2),
            ReplacementTransform(loss_text, new_loss_text),
            nn.animate.set_color(GREEN) # Make the whole network green to show it's "trained"
        )
        self.wait(3)

class HighLevelOverview(Scene, NNMediaMixin):
    def construct(self):
        self.setup_svgs()
        
        # MODIFIED: Use the instance variables (self.complex_nn, etc.)
        self.play(DrawBorderThenFill(self.complex_nn))
        self.wait(1)

        eight_text = Text("8", font="Virgil 3 YOFF", font_size=96, color=BLACK).next_to(self.complex_nn, LEFT, buff=0.5)
        self.play(FadeIn(eight_text))
        self.wait(1)

        text = Text("This is\na number", font="Virgil 3 YOFF", font_size=24, color=BLACK).next_to(self.complex_nn, RIGHT, buff=0.5)
        self.play(Write(text))

class NeuralNetworkArchitecture(Scene):
    def construct(self):
        # Title
        title = Text("Neural Network Architecture", color=BLACK, font="Virgil 3 YOFF").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Code block
        code = Code(
            code_string="""class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        # Input layer expects a flattened 28x28 image, which is 784
        self.fc1 = nn.Linear(28 * 28, 1024)
        self.fc2 = nn.Linear(1024, 1024)
        self.fc3 = nn.Linear(1024, 1024)
        self.fc4 = nn.Linear(1024, 1024)
        # Output layer for 10 classes (digits 0-9)
        self.fc5 = nn.Linear(1024, 10)""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.8).move_to(ORIGIN)
        
        # Animate code appearance line by line
        self.play(FadeIn(code))
        self.wait(2)
        
        # Architecture summary
        arch_text = Text(
            "784 -> 1024 -> 1024 -> 1024 -> 1024 -> 10",
            color=BLUE, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN, buff=0.5)
        
        self.play(Write(arch_text))
        self.wait(3)


class ForwardPassCode(Scene):
    def construct(self):
        # Title
        title = Text("Forward Pass", color=BLACK, font="Virgil 3 YOFF").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Code block
        code = Code(
            code_string="""def forward(self, x):
    # Flatten the input image from 28x28 to a 1D tensor of 784 elements
    x = torch.flatten(x, 1)
    
    # Pass through the hidden layers with ReLU activation
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = F.relu(self.fc4(x))
    
    # Pass through the output layer
    x = self.fc5(x)
    
    # Apply log_softmax for a classification problem
    return F.log_softmax(x, dim=1)""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.75).move_to(ORIGIN)
        
        self.play(FadeIn(code))
        self.wait(2)
        
        # Data flow annotation
        flow_text = Text(
            "28x28 -> 784 -> 1024 -> 1024 -> 1024 -> 1024 -> 10",
            color=GREEN, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN, buff=0.5)
        
        self.play(Write(flow_text))
        self.wait(3)


class TrainingCode(Scene):
    def construct(self):
        # Title
        title = Text("Training Function", color=BLACK, font="Virgil 3 YOFF").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Code block
        code = Code(
            code_string="""def train(model, train_loader, optimizer, criterion, device):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'Train Step: {batch_idx}\\tLoss: {loss.item():.6f}')""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.7).move_to(ORIGIN)
        
        self.play(FadeIn(code))
        self.wait(2)
        
        # Training steps annotation
        steps_text = Text(
            "Forward -> Loss -> Backward -> Update",
            color=RED, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN, buff=0.5)
        
        self.play(Write(steps_text))
        self.wait(3)


class TestingCode(Scene):
    def construct(self):
        # Title
        title = Text("Testing Function", color=BLACK, font="Virgil 3 YOFF").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Code block
        code = Code(
            code_string="""def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print(f'Test set: Average loss: {test_loss:.4f}, '
          f'Accuracy: {correct}/{len(test_loader.dataset)} '
          f'({100. * correct / len(test_loader.dataset):.0f}%)')""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.65).move_to(ORIGIN)
        
        self.play(FadeIn(code))
        self.wait(2)
        
        # Testing annotation
        eval_text = Text(
            "Evaluation Mode -> No Gradients -> Calculate Accuracy",
            color=BLUE, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN, buff=0.5)
        
        self.play(Write(eval_text))
        self.wait(3)


class ActivationCode(Scene):
    def construct(self):
        # Title
        title = Text("Generate Activations", color=BLACK, font="Virgil 3 YOFF").scale(0.7).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Code block (showing key parts)
        code = Code(
            code_string="""def generate_activations(model, dataset, device, num_samples=100):
    model.eval().to(device)
    activations = {
        'input': [], 'fc1': [], 'fc2': [], 'fc3': [], 'fc4': [], 'output': []
    }
    
    with torch.no_grad():
        for i in range(num_samples):
            x, y = dataset[i]
            x = x.to(device).unsqueeze(0)
            
            # Record activations at each layer
            activations['input'].append(np.abs(x.cpu().squeeze().numpy()))
            x = torch.flatten(x, 1)
            
            x = F.relu(model.fc1(x))
            activations['fc1'].append(np.abs(x.cpu().squeeze().numpy()))
            # ... (repeat for other layers)
            
    np.savez('activity.npz', **activations)""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.65).move_to(ORIGIN)
        
        self.play(FadeIn(code))
        self.wait(2)
        
        # Purpose annotation
        purpose_text = Text(
            "Record neuron activations for visualization",
            color=PURPLE, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN, buff=0.5)
        
        self.play(Write(purpose_text))
        self.wait(3)


class MainExecutionCode(Scene):
    def construct(self):
        # Title
        title = Text("Main Execution", color=BLACK, font="Virgil 3 YOFF").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)
        
        # Code block
        code = Code(
            code_string="""if __name__ == "__main__":
    # Setup
    epochs = 10
    lr = 0.01
    batch_size = 64
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Data Loading
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_dataset = datasets.MNIST('./data', train=True, 
                                   download=True, transform=transform)
    
    # Model Setup
    model = NeuralNetwork().to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = F.nll_loss
    
    # Training and Evaluation
    # for epoch in range(1, epochs + 1):
    #     train(model, train_loader, optimizer, criterion, device)
    #     test(model, test_loader, criterion, device)""",
            tab_width=4,
            language="python",
            background="rectangle",
            background_config = {
                "fill_color": WHITE,
                "fill_opacity": 1,
                "stroke_width": 2,
            },
            paragraph_config={
                "font": "Monospace",
                "font_size": 28,
                "line_spacing": 0.5,
            }
        ).scale(0.6).move_to(ORIGIN)
        
        self.play(FadeIn(code))
        self.wait(2)
        
        # Pipeline annotation
        pipeline_text = Text(
            "Setup -> Data -> Model -> Train -> Test",
            color=ORANGE, font="Virgil 3 YOFF"
        ).scale(0.5).next_to(code, DOWN*0.5, buff=0.5)
        
        self.play(Write(pipeline_text))
        self.wait(3)