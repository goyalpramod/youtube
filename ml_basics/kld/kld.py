from manim import *

class WobbleTransform(Animation):
    CONFIG = {
        "amplitude": 0.2,
        "wave_freq": 2,
    }
    
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        # Store original points for reference
        self.original_points = {
            mob: mob.get_points().copy() 
            for mob in self.mobject.family_members_with_points()
        }

    def interpolate_mobject(self, alpha):
        # Use a smooth transition for the wave effect
        time_var = alpha * 2 * PI
        
        for mob in self.mobject.family_members_with_points():
            original_points = self.original_points[mob]
            points = mob.get_points()
            
            for i in range(len(points)):
                x, y, z = original_points[i]
                
                # Create organic distortion using multiple sine waves
                dx = self.CONFIG["amplitude"] * np.sin(self.CONFIG["wave_freq"] * y + time_var)
                dy = self.CONFIG["amplitude"] * np.sin(self.CONFIG["wave_freq"] * x + time_var)
                
                # Add secondary wave for more organic feel
                dx += self.CONFIG["amplitude"] * 0.5 * np.sin(self.CONFIG["wave_freq"] * 2 * y - time_var)
                dy += self.CONFIG["amplitude"] * 0.5 * np.sin(self.CONFIG["wave_freq"] * 2 * x - time_var)
                
                # Apply distortion
                points[i] = [x + dx, y + dy, z]

class TextCrossEntropy(Scene):
    def construct(self):
        text = Text("Cross Entropy", font_size=72)
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))
        equation = MathTex(r"H(p, q) = -\sum_{x} p(x) \log q(x)", font_size=48)
        self.play(Write(equation))
        self.wait(5)
        self.play(FadeOut(equation))
        text_1 = Text("Understanding the math")
        text_2 = Text("Understanding Entropy")
        text_3 = Text("Understanding Cross Entropy")
        self.play(Write(text_1))
        self.wait(2)
        self.play(text_1.animate.shift(UP*3))
        self.play(FadeOut(text_1))
        text_2.move_to(UP*3)
        text_3.move_to(UP*3)
        self.play(FadeIn(text_2))
        self.wait(2)
        self.play(FadeOut(text_2))
        self.play(FadeIn(text_3))
        self.wait(2)
        self.play(FadeOut(text_3))

class IndependentProbabilityDistributions(Scene):
    def construct(self):
        # Constants for probabilities
        THIN_CRUST_PROB = 0.25
        THICK_CRUST_PROB = 0.75
        PAN_PROB = 0.60  # Corrected from 0.60 to 0.62
        OVEN_PROB = 0.40    # Corrected from 0.40 to 0.38

        # Create the first distribution (Weather)
        weather_rect = Rectangle(height=4, width=1, stroke_width=2)
        weather_parts = VGroup(
            # Sunny (bottom)
            Rectangle(height=4*THICK_CRUST_PROB, width=1)
            .set_fill(color=YELLOW_A, opacity=0.8),
            # Raining (top)
            Rectangle(height=4*THIN_CRUST_PROB, width=1)
            .set_fill(color=BLUE_D, opacity=1),
        ).arrange(UP, buff=0)
        
        weather_group = VGroup(weather_rect, weather_parts)
        
        # Weather labels
        weather_title = Text("Crust", font_size=24)
        weather_title.next_to(weather_group, UP, buff=0.3)
        
        weather_labels = VGroup(
            Text(f"Thin\n{int(THIN_CRUST_PROB*100)}%", font_size=20),
            Text(f"Thick\n{int(THICK_CRUST_PROB*100)}%", font_size=20)
        )
        weather_labels[0].next_to(weather_parts[1], LEFT, buff=0.3)
        weather_labels[1].next_to(weather_parts[0], LEFT, buff=0.3)
        
        weather_full_group = VGroup(weather_group, weather_title, weather_labels)
        weather_full_group.move_to(LEFT*3)

        # Create second distribution (Clothing)
        clothing_rect = Rectangle(height=4, width=1, stroke_width=2)
        clothing_parts = VGroup(
            # T-shirt (bottom)
            Rectangle(height=4*PAN_PROB, width=1)
            .set_fill(color=YELLOW_A, opacity=0.5),
            # Coat (top)
            Rectangle(height=4*OVEN_PROB, width=1)
            .set_fill(color=YELLOW_B, opacity=0.5),
        ).arrange(UP, buff=0)
        
        clothing_group = VGroup(clothing_rect, clothing_parts)
        
        # Clothing labels
        clothing_title = Text("Utensil", font_size=24)
        clothing_title.next_to(clothing_group, UP, buff=0.3)
        
        clothing_labels = VGroup(
            Text(f"Oven\n{int(OVEN_PROB*100)}%", font_size=20),
            Text(f"Pan\n{int(PAN_PROB*100)}%", font_size=20)
        )
        clothing_labels[0].next_to(clothing_parts[1], RIGHT, buff=0.3)
        clothing_labels[1].next_to(clothing_parts[0], RIGHT, buff=0.3)
        
        clothing_full_group = VGroup(clothing_group, clothing_title, clothing_labels)
        clothing_full_group.move_to(RIGHT*3)

        # Animation sequence
        # 1. Show weather distribution
        self.play(
            Create(weather_rect),
            FadeIn(weather_parts),
            Write(weather_title),
            Write(weather_labels)
        )
        self.wait()

        # 2. Show clothing distribution
        self.play(
            Create(clothing_rect),
            FadeIn(clothing_parts),
            Write(clothing_title),
            Write(clothing_labels)
        )
        self.wait()

        # Save initial positions for references
        clothing_initial = clothing_group.get_center()
        
        # 3. Rotate clothing and move to bottom (aligned left)
        self.play(
            Rotate(clothing_group, angle=-PI/2),
            FadeOut(clothing_title),
            FadeOut(clothing_labels),
            FadeOut(weather_title),
        )
        
        # Move to form square (align left edges)
        self.play(
            clothing_group.animate.next_to(weather_group.get_bottom(), UP*0.2, buff=0).align_to(weather_group, LEFT)  # Align left
        )
        # Create target rectangles for expansion
        expanded_weather = weather_rect.copy().stretch_to_fit_width(4)
        expanded_clothing = clothing_rect.copy().stretch_to_fit_height(4)

        # Create target parts with correct proportions
        expanded_weather_parts = VGroup(
            weather_parts[0].copy().stretch_to_fit_width(4),  # sunny
            weather_parts[1].copy().stretch_to_fit_width(4),   # raining
        ).arrange(UP, buff=0)

        expanded_clothing_parts = VGroup(
            clothing_parts[0].copy().stretch_to_fit_height(4),  # t-shirt
            clothing_parts[1].copy().stretch_to_fit_height(4),   # coat
        ).arrange(RIGHT, buff=0)

        # Set z-index for the rectangles too
        expanded_weather
        expanded_clothing

        # Fix positions precisely
        expanded_weather.move_to(weather_rect).align_to(weather_rect, LEFT)
        expanded_weather_parts.move_to(expanded_weather)
        expanded_weather_parts.align_to(weather_parts, LEFT)

        expanded_clothing.move_to(clothing_rect).align_to(clothing_rect, DOWN)
        expanded_clothing_parts.move_to(expanded_clothing)
        expanded_clothing_parts.align_to(clothing_parts, DOWN)

        # Ensure groups maintain relative positions
        weather_group = VGroup(weather_rect, weather_parts)
        clothing_group = VGroup(clothing_rect, clothing_parts)

        # Animate expansion with fixed positioning
        self.play(
            Transform(weather_rect, expanded_weather),
            Transform(weather_parts, expanded_weather_parts),
            Transform(clothing_rect, expanded_clothing),
            Transform(clothing_parts, expanded_clothing_parts),
            run_time=1.5,
            rate_func=smooth  # Ensures smooth transformation
        )
        self.wait()
        
        # 4. Create final square labels
        bottom_labels = VGroup(
            Text("Pan", font_size=20),
            Text("Oven", font_size=20)
        ).arrange(RIGHT, buff=1.5)
        bottom_labels.next_to(clothing_group, DOWN, buff=0.3)
        
        percentages = VGroup(
            Text(f"{int(PAN_PROB*100)}%", font_size=16),
            Text(f"{int(OVEN_PROB*100)}%", font_size=16)
        )
        percentages[0].next_to(bottom_labels[0], DOWN, buff=0.1)
        percentages[1].next_to(bottom_labels[1], DOWN, buff=0.1)
        clothing_title.next_to(percentages, DOWN, buff=0)
        weather_title.next_to(weather_labels, LEFT, buff=0)
        
        self.play(
            Write(bottom_labels),
            Write(percentages),
            Write(clothing_title),
            Write(weather_title),
        )
        
        # Final pause
        self.wait(2)

        def update_clothing_parts(parts, tshirt_prob):
            coat_prob = 1 - tshirt_prob
            original_center = parts.get_center()
            
            # Update t-shirt part (left)
            parts[0].stretch_to_fit_width(4 * tshirt_prob, about_edge=LEFT)
            
            # Update coat part (right) and position it next to t-shirt
            parts[1].stretch_to_fit_width(4 * coat_prob, about_edge=RIGHT)
            parts[1].next_to(parts[0], RIGHT, buff=0)
            
            # Move back to original center
            parts.move_to(original_center)
            return parts

        # Animate to 20-80 distribution
        self.play(
            UpdateFromAlphaFunc(
                clothing_parts,
                lambda m, a: update_clothing_parts(m, 0.60 + (0.20 - 0.60) * a)
            ),
            Transform(percentages[0], Text("20%", font_size=16).move_to(percentages[0])),
            Transform(percentages[1], Text("80%", font_size=16).move_to(percentages[1])),
            run_time=2
        )
        self.wait(2)

        # Animate back to 60-40 distribution
        self.play(
            UpdateFromAlphaFunc(
                clothing_parts,
                lambda m, a: update_clothing_parts(m, 0.20 + (0.60 - 0.20) * a)
            ),
            Transform(percentages[0], Text("60%", font_size=16).move_to(percentages[0])),
            Transform(percentages[1], Text("40%", font_size=16).move_to(percentages[1])),
            run_time=2
        )
        self.wait(2)

        # Group everything and move to center
        all_elements = VGroup(
            weather_rect, weather_parts, weather_labels,
            clothing_rect, clothing_parts,
            bottom_labels, percentages,
            clothing_title, weather_title
        )

        self.play(
            all_elements.animate.move_to(ORIGIN + LEFT*0.5 + DOWN*0.15),
            run_time=1
        )
        self.wait()

        self.play(
            FadeOut(bottom_labels, weather_labels, percentages)
        )

        # After moving to center
        wobble_group = VGroup(weather_rect, weather_parts, clothing_rect, clothing_parts)
        
        # Create the wobble effect
        wobble = WobbleTransform(
            wobble_group,
            run_time=5,
            rate_func=there_and_back_with_pause,  # This will create a nice wobble and hold
        )
        
        self.play(wobble)
        self.wait(2)

        self.play(
            FadeOut(wobble_group),
            FadeOut(clothing_title),
            FadeOut(weather_title),
        )

class ConditionalProbabilityDistributions(Scene):
    def construct(self):
        # Constants for probabilities
        THIN_CRUST_PROB = 0.25
        THICK_CRUST_PROB = 0.75
        
        # Initial distribution (left side)
        weather_height = 4
        weather_width = 1
        
        # Create the initial rectangle with its parts
        weather_group = VGroup(
            # Main container
            Rectangle(height=weather_height, width=weather_width, stroke_width=2),
            # Sunny part (bottom)
            Rectangle(height=weather_height*THICK_CRUST_PROB, width=weather_width)
            .set_fill(color="#D4D0AB", opacity=1),
            # Raining part (top)
            Rectangle(height=weather_height*THIN_CRUST_PROB, width=weather_width)
            .set_fill(color="#4FB3BF", opacity=1),
        )
        
        # Position the parts
        weather_group[1].move_to(weather_group[0].get_bottom(), aligned_edge=DOWN)
        weather_group[2].move_to(weather_group[0].get_top(), aligned_edge=UP)
        
        # Weather labels
        weather_labels = VGroup(
            Text("thin\n25%", font_size=20, color=WHITE),
            Text("thick\n75%", font_size=20, color=WHITE)
        )
        weather_labels[0].next_to(weather_group[2], LEFT, buff=0.3)
        weather_labels[1].next_to(weather_group[1], LEFT, buff=0.3)
        
        initial_group = VGroup(weather_group, weather_labels)
        initial_group.move_to(LEFT*3)

        # Joint probability square (right side)
        square_size = 4
        joint_square = Square(side_length=square_size, stroke_width=2)
        
        # Create the sections of the square
        # Calculate section sizes based on total square size
        tshirt_width = square_size * 0.75  # 75% of width for t-shirt
        coat_width = square_size * 0.25    # 25% of width for coat
        
        sections = VGroup(
            # Bottom left (sunny, tshirt) - 56%
            Rectangle(height=square_size * 0.75, width=tshirt_width)
            .set_fill(color="#D4D0AB", opacity=1),
            # Bottom right (sunny, coat) - 19%
            Rectangle(height=square_size * 0.75, width=coat_width)
            .set_fill(color="#D4D0AB", opacity=1),
            # Top left (rain, tshirt) - 6%
            Rectangle(height=square_size * 0.25, width=coat_width)
            .set_fill(color="#4FB3BF", opacity=1),
            # Top right (rain, coat) - 19%
            Rectangle(height=square_size * 0.25, width=tshirt_width)
            .set_fill(color="#4FB3BF", opacity=1),
        )

        # Position sections precisely
        sections[0].move_to(joint_square.get_bottom(), aligned_edge=DOWN).align_to(joint_square, LEFT)  # 56%
        sections[1].move_to(joint_square.get_bottom(), aligned_edge=DOWN).align_to(joint_square, RIGHT)  # 19%
        sections[2].move_to(joint_square.get_top(), aligned_edge=UP).align_to(joint_square, LEFT)  # 6%
        sections[3].move_to(joint_square.get_top(), aligned_edge=UP).align_to(joint_square, RIGHT)  # 19%
        
        joint_group = VGroup(joint_square, sections)
        joint_group.move_to(RIGHT*3)

        # Percentage labels inside sections
        percentage_labels = VGroup(
            Text("56%", font_size=36, color=WHITE).move_to(sections[0]),
            Text("19%", font_size=36, color=WHITE).move_to(sections[1]),
            Text("6%", font_size=36, color=WHITE).move_to(sections[2]),
            Text("19%", font_size=36, color=WHITE).move_to(sections[3]),
        )

        # Bottom labels for t-shirt and coat
        bottom_labels = VGroup(
            Text("75%", font_size=20, color=WHITE),
            Text("25%", font_size=20, color=WHITE),
            Text("pan", font_size=24, color=WHITE),
            Text("oven", font_size=24, color=WHITE),
        )
        
        # Position bottom labels
        bottom_labels[0].next_to(joint_square, DOWN, buff=0.3).shift(LEFT*0.5)
        bottom_labels[1].next_to(joint_square, DOWN, buff=0.3).shift(RIGHT*1.5)
        bottom_labels[2].next_to(bottom_labels[0], DOWN, buff=0.1)
        bottom_labels[3].next_to(bottom_labels[1], DOWN, buff=0.1)

        top_labels = VGroup(
            Text("25%", font_size=20, color=WHITE),
            Text("75%", font_size=20, color=WHITE),
            Text("pan", font_size=24, color=WHITE),
            Text("oven", font_size=24, color=WHITE),
        )

        top_labels[0].next_to(joint_square, UP, buff=0.3).shift(LEFT*1.5)
        top_labels[1].next_to(joint_square, UP, buff=0.3).shift(RIGHT*0.5)
        top_labels[2].next_to(top_labels[0], UP, buff=0.1)
        top_labels[3].next_to(top_labels[1], UP, buff=0.1)

        # Formula
        formula = MathTex(
            r"p(x,y) = p(x) \cdot p(y|x)",
            color=WHITE,
            font_size=36
        ).next_to(joint_square, DOWN, buff=2)

        # Animation sequence
        self.play(
            Create(weather_group, run_time = 3),
            Write(weather_labels, run_time = 3)
        )
        self.wait()
        
        self.play(
            Create(joint_square, run_time = 3),
            Create(sections, run_time = 3)
        )
        self.wait()


        self.play(Write(bottom_labels))
        self.wait()
        self.play(Write(top_labels))
        self.wait()

        self.play(
            weather_labels[0].animate.set_color(YELLOW),
            top_labels[0].animate.set_color(YELLOW),
            top_labels[2].animate.set_color(YELLOW),
        )
        self.wait(2)
        self.play(
            weather_labels[0].animate.set_color(WHITE),
            top_labels[0].animate.set_color(WHITE),
            top_labels[2].animate.set_color(WHITE),
        )

        self.play(Write(percentage_labels[2]))
        self.wait()

        self.play(
            weather_labels[0].animate.set_color(YELLOW),
            top_labels[1].animate.set_color(YELLOW),
            top_labels[3].animate.set_color(YELLOW),
        )
        self.wait(2)
        self.play(
            weather_labels[0].animate.set_color(WHITE),
            top_labels[1].animate.set_color(WHITE),
            top_labels[3].animate.set_color(WHITE),
        )

        self.play(Write(percentage_labels[3]))
        self.wait()

        self.play(
            weather_labels[1].animate.set_color(YELLOW),
            bottom_labels[0].animate.set_color(YELLOW),
            bottom_labels[2].animate.set_color(YELLOW),
        )
        self.wait(2)
        self.play(
            weather_labels[1].animate.set_color(WHITE),
            bottom_labels[0].animate.set_color(WHITE),
            bottom_labels[2].animate.set_color(WHITE),
        )

        self.play(Write(percentage_labels[0]))
        self.wait()
        
        self.play(
            weather_labels[1].animate.set_color(YELLOW),
            bottom_labels[1].animate.set_color(YELLOW),
            bottom_labels[3].animate.set_color(YELLOW),
        )
        self.wait(2)
        self.play(
            weather_labels[1].animate.set_color(WHITE),
            bottom_labels[1].animate.set_color(WHITE),
            bottom_labels[3].animate.set_color(WHITE),
        )

        self.play(Write(percentage_labels[1]))
        self.wait()


        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()

        # Create new visualization
        # Bottom bar (62% - 38% split)
        bottom_bar = Rectangle(height=0.5, width=4, stroke_width=2)
        bottom_sections = VGroup(
            # Left section (62%)
            Rectangle(height=0.5, width=4 * 0.60)
            .set_fill(color="#D4D0AB", opacity=1),
            # Right section (38%)
            Rectangle(height=0.5, width=4 * 0.40)
            .set_fill(color="#4FB3BF", opacity=1),
        ).arrange(RIGHT, buff=0)
        
        bottom_group = VGroup(bottom_bar, bottom_sections)
        bottom_group.move_to(DOWN*3)

        # Bottom percentages
        bottom_labels = VGroup(
            Text("60%", font_size=24, color=WHITE).move_to(bottom_sections[0]),
            Text("40%", font_size=24, color=WHITE).move_to(bottom_sections[1])
        )


        # Square with new proportions
        square_size = 4
        main_square = Square(side_length=square_size, stroke_width=2)
        
        # Create sections with new proportions
        sections = VGroup(
            # Bottom left (sunny, left) - 56%
            Rectangle(height=square_size * 0.80, width=square_size * 0.60)
            .set_fill(color="#D4D0AB", opacity=1),
            # Bottom right (sunny, right) - 19%
            Rectangle(height=square_size * 0.50, width=square_size * 0.40)
            .set_fill(color="#4FB3BF", opacity=1),
            # Top left (rain, left) - 6%
            Rectangle(height=square_size * (1 - 0.80), width=square_size * 0.60)
            .set_fill(color="#D4D0AB", opacity=1),
            # Top right (rain, right) - 19%
            Rectangle(height=square_size * 0.50, width=square_size * 0.40)
            .set_fill(color="#4FB3BF", opacity=1),
        )

        # Position sections
        sections[0].move_to(main_square.get_bottom(), aligned_edge=DOWN).align_to(main_square, LEFT)
        sections[1].move_to(main_square.get_bottom(), aligned_edge=DOWN).align_to(main_square, RIGHT)
        sections[2].move_to(sections[0].get_top(), aligned_edge=DOWN)
        sections[3].move_to(sections[1].get_top(), aligned_edge=DOWN)

        main_group = VGroup(main_square, sections)
        main_group.move_to(ORIGIN)

        # Percentage labels
        percentage_labels = VGroup(
            Text("54%", font_size=36, color=WHITE).move_to(sections[0]),
            Text("20%", font_size=36, color=WHITE).move_to(sections[1]),
            Text("6%", font_size=36, color=WHITE).move_to(sections[2]),
            Text("20%", font_size=36, color=WHITE).move_to(sections[3])
        )

        # Side labels for rain/sunny percentages
        side_labels = VGroup(
            Text("thin\n10%", font_size=24, color=WHITE).next_to(main_square, LEFT, buff=0.5).shift(UP*1.5),
            Text("thick\n90%", font_size=24, color=WHITE).next_to(main_square, LEFT, buff=0.5).shift(DOWN*0.5),
            Text("thin\n50%", font_size=24, color=WHITE).next_to(main_square, RIGHT, buff=0.5).shift(UP*1),
            Text("thick\n50%", font_size=24, color=WHITE).next_to(main_square, RIGHT, buff=0.5).shift(DOWN*1)
        )

        # Animation sequence for new visualization
        self.play(
            Create(bottom_bar),
            Create(bottom_sections),
            Write(bottom_labels)
        )
        self.wait()

        self.play(
            Create(main_square),
            Create(sections)
        )
        self.wait()

        self.play(Write(side_labels))
        self.wait(2)

        self.play(Write(percentage_labels))
        self.wait()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()


        # Title
        title = Text("Joint Probability", font_size=40).to_edge(UP)

        # Create the first equation with specific terms
        eq1 = MathTex(
        "p(thick,pan)", "=", "p(thick)", "\\cdot", "p(pan|thick)"
        ).scale(1.2)

        eq1.next_to(title, DOWN*3, buff=1)

        # Create the general equation
        eq2 = MathTex(
        "p(x,y)", "=", "p(x)", "\\cdot", "p(y|x)"
        ).scale(1.2)

        eq2.next_to(title, DOWN*3, buff=1)

        # Create underbraces and labels
        joint_label = Tex("Joint probability").scale(0.5)
        marginal_label = Tex("Marginal probability").scale(0.5)
        conditional_label = Tex("Conditional probability").scale(0.5)

        # Add underbraces for second equation
        joint_brace = Brace(eq2[0], DOWN)
        marginal_brace = Brace(eq2[2], UP)
        conditional_brace = Brace(eq2[4], DOWN)

        # Position labels under braces
        joint_label.next_to(joint_brace, DOWN)
        marginal_label.next_to(marginal_brace, UP)
        conditional_label.next_to(conditional_brace, DOWN)

        # Animation sequence
        self.play(Write(title))
        self.wait()

        # Show first equation
        self.play(Write(eq1))
        self.wait(2)

        # Transform to general equation
        self.play(
        ReplacementTransform(eq1, eq2)
        )
        self.wait()

        # Add braces and labels
        self.play(
        Create(joint_brace),
        Create(marginal_brace),
        Create(conditional_brace)
        )
        self.wait()

        self.play(
        Write(joint_label),
        Write(marginal_label),
        Write(conditional_label)
        )
        self.wait(2)

        # Save the conditional part
        conditional_group = VGroup(eq2[4])

        # Fade out everything except conditional
        self.play(
            FadeOut(title),
            FadeOut(eq2[0:4]),  # Fade out everything except conditional part
            FadeOut(joint_brace),
            FadeOut(marginal_brace),
            FadeOut(joint_label),
            FadeOut(marginal_label),
            FadeOut(conditional_brace),
            FadeOut(conditional_label),
        )
        self.wait()

        # Move conditional to center
        self.play(
        conditional_group.animate.move_to(ORIGIN + UP*2)
        )
        self.wait()

        # Create Bayes equation
        bayes_eq = MathTex(
        "p(y|x)", "=", "\\frac{p(x|y)p(y)}{p(x)}"
        ).scale(1.2)

        bayes_eq.next_to(conditional_group, DOWN*1.5, buff=1)

        # Create label
        bayes_label = Text("Bayes' Rule", font_size=36)
        bayes_label.next_to(bayes_eq, UP, buff=0.5)

        # Show Bayes equation and label
        self.play(
        Write(bayes_label),
        Write(bayes_eq)
        )
        self.wait(2)

        # Fade everything out
        self.play(
        *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()

class SimpleEncoding(Scene):
    def construct(self):
        # Constants for consistent styling
        SYMBOL_COLOR = "#C19EE0"  # Light purple
        CODE_COLOR = "#98FB98"    # Light green
        
        # Create the binary string at top
        binary_string = Text("1 0 0 1 1 0...", color=CODE_COLOR)
        binary_string.move_to(ORIGIN)
        
        # Create the mapping diagram
        # Left side - symbols with food items
        symbols = VGroup(
            Text("Flour", font_size=36),
            Text("Cheese", font_size=36), 
            Text("Tomato", font_size=36),
            Text("Oil", font_size=36)
        ).arrange(DOWN, buff=0.5).set_color(SYMBOL_COLOR)
        
        symbols_box = RoundedRectangle(
            height=symbols.height + 1,
            width=symbols.width + 1,
            corner_radius=0.2,
            color=SYMBOL_COLOR
        )
        symbols_box.move_to(symbols)
        symbols_label = Text("symbols", color=SYMBOL_COLOR).next_to(symbols_box, DOWN)
        symbols_group = VGroup(symbols_box, symbols, symbols_label).shift(LEFT * 3)
        
        # Right side - codewords
        codewords = VGroup(
            Text("00", font_size=36),
            Text("01", font_size=36),
            Text("10", font_size=36),
            Text("11", font_size=36)
        ).arrange(DOWN, buff=0.5).set_color(CODE_COLOR)
        
        codewords_box = RoundedRectangle(
            height=codewords.height + 1,
            width=codewords.width + 1,
            corner_radius=0.2,
            color=CODE_COLOR
        )
        codewords_box.move_to(codewords)
        codewords_label = Text("codewords", color=CODE_COLOR).next_to(codewords_box, DOWN)
        codewords_group = VGroup(codewords_box, codewords, codewords_label).shift(RIGHT * 3)
        
        # Arrow and "code" text
        arrow = Arrow(
            symbols_box.get_right(),
            codewords_box.get_left(),
            buff=0.5,
            color=WHITE
        )
        code_text = Text("code", color=WHITE).next_to(arrow, UP, buff=0.2)
        
        # Bottom part - example encoding
        # Create texts first
        encoded_string = Text("0 0 0 1 0 0 1 1", font_size=40,  color=CODE_COLOR)
        codewords_text = Text("00  01  00  11", font_size=42 , color=CODE_COLOR)
        source_text = Text("Flour Cheese Flour Oil",font_size=24 ,color=SYMBOL_COLOR)
        
        # Create boxes
        encoded_box = RoundedRectangle(
            height=encoded_string.height + 0.5,
            width=encoded_string.width + 1,
            corner_radius=0.2,
            color=CODE_COLOR
        )
        codewords_box_bottom = RoundedRectangle(
            height=codewords_text.height + 0.5,
            width=codewords_text.width + 1,
            corner_radius=0.2,
            color=CODE_COLOR
        )
        source_box = RoundedRectangle(
            height=source_text.height + 0.5,
            width=source_text.width + 1,
            corner_radius=0.2,
            color=SYMBOL_COLOR
        )
        
        # Move texts to their boxes
        encoded_string.move_to(encoded_box)
        codewords_text.move_to(codewords_box_bottom)
        source_text.move_to(source_box)
        
        # Create groups
        encoded_group = VGroup(encoded_box, encoded_string)
        codewords_group_bottom = VGroup(codewords_box_bottom, codewords_text)
        source_group = VGroup(source_box, source_text)
        
        # Position the bottom elements
        encoded_group.move_to(ORIGIN).to_edge(UP, buff=2)
        codewords_group_bottom.next_to(encoded_group, DOWN, buff=0.75)
        source_group.next_to(codewords_group_bottom, DOWN, buff=0.75)
        
        # Create labels for bottom elements
        encoded_label = Text("encoded string", font_size=30, color=WHITE).next_to(encoded_group, RIGHT, buff=0.5)
        codewords_label_bottom = Text("codewords", font_size=30, color=WHITE).next_to(codewords_group_bottom, RIGHT, buff=0.5)
        source_label = Text("source symbols", font_size=30, color=WHITE).next_to(source_group, RIGHT, buff=0.5)
        
        # Create final groups for animation
        bottom_group = VGroup(
            VGroup(encoded_group, encoded_label),
            VGroup(codewords_group_bottom, codewords_label_bottom),
            VGroup(source_group, source_label)
        )
        
        # Animation sequence
        self.play(FadeIn(binary_string))
        self.wait()
        self.play(FadeOut(binary_string))
        
        self.play(
            FadeIn(symbols_group),
            FadeIn(codewords_group),
            Create(arrow),
            Write(code_text)
        )
        self.wait()
        self.play(
            FadeOut(symbols_group),
            FadeOut(codewords_group),
            FadeOut(arrow),
            FadeOut(code_text)
        )
        self.wait()
       
        self.play(
            FadeIn(bottom_group[0])
        )
        self.wait()
        self.play(
            FadeIn(bottom_group[1])
        )
        self.wait()
        self.play(
            FadeIn(bottom_group[2])
        )
        self.wait(2)

"""
Fix structure of the stuff, also make everything smooth.
"""

class VariableLengthEncoding(Scene):
   def construct(self):
        # Constants
        SYMBOL_COLOR = "#C19EE0"  # Light purple
        BAR_COLORS = ["#C19EE0", "#FFB6C1", "#98FB98", "#87CEEB"]  # Different colors for bars
        BAR_WIDTH = 4  # Constant width for all bars
        
        # Create bars and labels
        base_height = 0.5
        heights = [2, 1, 0.5, 0.5]  # Heights corresponding to probabilities
        
        # Create probability labels on left
        prob_labels = VGroup(
            MathTex("{1/2}", font_size=30),
            MathTex("{1/4}", font_size=30),
            MathTex("{1/8}", font_size=30),
            MathTex("{1/8}", font_size=30)
        )
        
        # Create food word labels
        food_labels = VGroup(
            Text("Flour", font_size=30),
            Text("Cheese", font_size=30),
            Text("Tomato", font_size=30),
            Text("Oil", font_size=30)
        )
        
        # Create rectangles (bars)
        bars = VGroup()
        for i in range(4):
            rect = Rectangle(
                height=heights[i],
                width=BAR_WIDTH,
                fill_color=BAR_COLORS[i],
                fill_opacity=0.8,
                stroke_color=WHITE
            )
            bars.add(rect)
        
        # Position the first bar
        bars[0].move_to(ORIGIN)
        
        # Position subsequent bars relative to the previous one
        for i in range(1, 4):
            bars[i].next_to(bars[i-1], DOWN, buff=0)
            
        # Position labels inside bars
        for label, bar in zip(food_labels, bars):
            label.move_to(bar)
            
        # Position probability labels
        for label, bar in zip(prob_labels, bars):
            label.next_to(bar, LEFT, buff=0.5)
            
        # Group everything
        entire_group = VGroup(bars, food_labels, prob_labels)
        entire_group.move_to(ORIGIN)
        
        # Animation sequence
        # Animate probability labels
        
        # Animate bars and food labels together
        for i in range(len(bars)):
            self.play(
                Create(bars[i]),
            )
            self.wait(0.2)
            self.play(
                Write(food_labels[i]),
            )
            self.wait(0.5)
            
        for label in prob_labels:
            self.play(Write(label))
        self.wait()
        
        self.wait(2)

       # Create title for the new encoding
        title = Text("Old Code", font_size=36)
        title.to_edge(UP)
        bits_label = Text("2 bits", font_size=30)
        bits_label.next_to(title, RIGHT)
        
        # Create the vertical dividing line
        vertical_line = Line(
            start=bars.get_top(),
            end=bars.get_bottom(),
            stroke_width=2
        ).set_opacity(0.5)
        vertical_line.move_to(bars.get_center())
        
        # Binary numbers
        binary_numbers = VGroup()
        positions = [(0,0), (0,1), (1,0), (1,1)]  # Binary values for each bar
        
        for i, bar in enumerate(bars):
            left_num = Text("0" if positions[i][0] == 0 else "1", font_size=36)
            right_num = Text("0" if positions[i][1] == 0 else "1", font_size=36)
            
            # Position numbers in left and right halves of each bar
            left_num.move_to(bar.get_left() + RIGHT * bar.width/4)
            right_num.move_to(bar.get_left() + RIGHT * bar.width * 3/4)
            
            binary_numbers.add(left_num, right_num)
        
        # Create L(x) label at bottom
        l_x_label = MathTex("L(x)", font_size=36)
        l_x_label.next_to(bars, DOWN*2, buff=0.5)
        
        # Create bit labels
        bit1_label = Text("1 bit", font_size=24)
        bit2_label = Text("2 bit", font_size=24)
        bit1_label.next_to(vertical_line, DOWN, buff=0.1)
        bit2_label.next_to(bit1_label, RIGHT, buff=1)
        
        # Animation sequence
        # Fade out food labels
        self.play(FadeOut(food_labels))
        
        # Add title and move everything up slightly
        self.play(
            Write(title),
            Write(bits_label),
        )
        
        # Add vertical line
        self.play(Create(vertical_line))
        
        # Add binary numbers one by one
        for num in binary_numbers:
            self.play(Write(num), run_time=0.5)
        
        # Add bottom labels
        self.play(
            Write(l_x_label),
            Write(bit1_label),
            Write(bit2_label)
        )
        
        self.wait(2)

        symbols_rect = RoundedRectangle(
            height=3, width=2,
            corner_radius=0.2,
            fill_color="#E6E6FA",
            fill_opacity=0.4,
            stroke_color=WHITE
        )
        
        codewords_rect = RoundedRectangle(
            height=3, width=2,
            corner_radius=0.2,
            fill_color="#90EE90",
            fill_opacity=0.4,
            stroke_color=WHITE
        )
        
        # Position rectangles
        symbols_rect.shift(LEFT * 2)
        codewords_rect.shift(RIGHT * 2)
        
        # Create labels
        symbols_label = Text("symbols", font_size=30).next_to(symbols_rect, DOWN)
        codewords_label = Text("codewords", font_size=30).next_to(codewords_rect, DOWN)
        
        # Create arrow
        arrow = Arrow(symbols_rect.get_right(), codewords_rect.get_left())
        code_text = Text("code", font_size=30).next_to(arrow, UP, buff=0.1)
        
        # Create symbol texts
        symbols = VGroup(
            Text("Flour", font_size=30),
            Text("Cheese", font_size=30),
            Text("Tomato", font_size=30),
            Text("Oil", font_size=30)
        ).arrange(DOWN, buff=0.2).move_to(symbols_rect)
        
        # Create codewords
        codewords = VGroup(
            Text("0", font_size=30),
            Text("10", font_size=30),
            Text("110", font_size=30),
            Text("111", font_size=30)
        ).arrange(DOWN, buff=0.2).move_to(codewords_rect)
        
        # Fade out previous scene
        everything = VGroup(bars, prob_labels, binary_numbers, vertical_line, 
                          title, bits_label, l_x_label, bit1_label, bit2_label)
        
        self.play(FadeOut(everything))
        
        # Animate new scene
        self.play(
            Create(symbols_rect),
            Create(codewords_rect),
            Write(symbols_label),
            Write(codewords_label)
        )
        
        self.play(
            Create(arrow),
            Write(code_text)
        )
        
        self.play(Write(symbols))
        self.play(Write(codewords))
        
        self.wait(2)
        
        # Fade out first transition
        everything_new = VGroup(symbols_rect, codewords_rect, symbols_label, 
                              codewords_label, arrow, code_text, symbols, codewords)
        
        self.play(FadeOut(everything_new))
        
        # Constants for the bars
        BAR_HEIGHT = 0.75
        BAR_WIDTH = 4
        
        # Title
        new_title = Text("New Code", font_size=36)
        title_group = VGroup(new_title).arrange(RIGHT, buff=0.5)
        title_group.to_edge(UP)
        
        # Create bars
        bars = VGroup()
        heights = [BAR_HEIGHT * 3, BAR_HEIGHT * 1.5, BAR_HEIGHT * 0.75, BAR_HEIGHT * 0.75]
        colors = ["#C19EE0", "#FFB6C1", "#98FB98", "#87CEEB"]
        
        for height, color in zip(heights, colors):
            rect = Rectangle(
                height=height,
                width=BAR_WIDTH,
                fill_color=color,
                fill_opacity=1,
                stroke_color=WHITE
            )
            bars.add(rect)
        
        # Stack bars vertically
        bars.arrange(DOWN, buff=0)
        bars.next_to(title_group, DOWN, buff=1)
        
        # Calculate the exact coordinates for the lines
        bar_top = bars.get_top()
        bar_bottom = bars.get_bottom()
        bar_left = bars.get_left()
        bar_right = bars.get_right()
        
        # Create vertical lines that stay within the boxes
        v_lines = VGroup()
        line_positions = [BAR_WIDTH/3, 2*BAR_WIDTH/3]  # Positions for solid lines
        
        for x_pos in line_positions:
            line = Line(
                start=bar_top,
                end=bar_bottom,
                stroke_width=2
            ).set_opacity(0.5)
            line.move_to(bar_left + RIGHT * x_pos)
            v_lines.add(line)
        
        # Add dotted line at the right edge
        dotted_line = DashedLine(
            start=bar_top,
            end=bar_bottom,
            stroke_width=2,
            dash_length=0.1
        ).set_opacity(0.5)
        dotted_line.move_to(bar_right)
        
        # Binary numbers positioning - only put numbers where shown in the image
        binary_numbers = VGroup()
        
        # Define which cells should have numbers (1-based indexing for cell and bar)
        number_positions = [
            (1, 1, "0"),           # First bar, first cell: "0"
            (1, 2, "1"), (2, 2, "0"),  # Second bar: "1" in first cell, "0" in second cell
            (1, 3, "1"), (2, 3, "1"), (3, 3, "0"),  # Third bar
            (1, 4, "1"), (2, 4, "1"), (3, 4, "1")   # Fourth bar
        ]

        for cell, bar_idx, value in number_positions:
            number = Text(value, font_size=36, color=WHITE)
            section_width = BAR_WIDTH / 3
            
            # Calculate proper positioning
            x_pos = bars[bar_idx-1].get_left() + RIGHT * ((cell-1) * section_width + section_width/2)
            y_pos = bars[bar_idx-1].get_center()[1]
            
            number.move_to([x_pos[0], y_pos, 0])
            binary_numbers.add(number)
        
        # Add labels at bottom
        bottom_labels = VGroup(
            Text("1 bit", font_size=24),
            Text("2 bit", font_size=24),
            Text("3 bit", font_size=24)
        )
        
        # Position bottom labels
        for i, label in enumerate(bottom_labels):
            x_pos = bar_left[0] + (i + 0.5) * BAR_WIDTH/3
            label.move_to([x_pos, bar_bottom[1] - 0.5, 0])
        
        # Add probability labels on left
        prob_labels = VGroup(
            MathTex("{1/2}", font_size=30),
            MathTex("{1/4}", font_size=30),
            MathTex("{1/8}", font_size=30),
            MathTex("{1/8}", font_size=30)
        )
        
        for label, bar in zip(prob_labels, bars):
            label.next_to(bar, LEFT, buff=0.5)
        
        # Add L(x) label
        l_x_label = MathTex("L(x)", font_size=36)
        l_x_label.next_to(bottom_labels[1], DOWN, buff=0.5)
        
        # Animation sequence
        self.play(
            Write(title_group)
        )
        
        self.play(
            Create(bars),
            Write(prob_labels)
        )
        
        self.play(
            Create(v_lines),
            Create(dotted_line)
        )
        
        self.play(Write(binary_numbers))
        
        self.play(
            Write(VGroup(bottom_labels, l_x_label))
        )
        
        self.wait()

        # Create entropy labels with better positioning and size
        entropy_title = Text("Entropy", font_size=32)
        entropy_title_2 = Text("= Optimal Average Length", font_size=30)
        entropy_equals = Text("= Area", font_size=32)
        entropy_equation = MathTex("= \sum_{i=1}^{n} p(x_i) \cdot L(x_i)", font_size=40)
        entropy_equation_values = MathTex("= 1/2 \cdot 1 + 1/4 \cdot 2 + 1/8 \cdot 3 + 1/8 \cdot 3", font_size=28)
        entropy_value = Text("= 1.75 bits", font_size=32)

        entropy_group = VGroup(entropy_title, entropy_title_2, entropy_equals, entropy_equation, entropy_equation_values ,entropy_value)
        entropy_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Position it more carefully to avoid being cut off
        entropy_group.next_to(bars, RIGHT*0.1, buff=0.1)

        self.play(
            FadeOut(VGroup(l_x_label, title_group)),
        )

        # Shift the bars less to the left to make more room for entropy text
        self.play(
            VGroup(bars, prob_labels, bottom_labels, v_lines, dotted_line, binary_numbers).animate.shift(LEFT*2)
        )

        self.play(
            Write(entropy_group, run_time=4)
        )

        self.wait(2)

        self.play(
            FadeOut(VGroup(entropy_group, bars, v_lines, dotted_line, binary_numbers)),
        )
        self.wait(2)


class CodeWords(Scene):
    def construct(self):
        # Constants
        cell_height = 0.5
        cell_widths = [1.5, 1, 1]  # Different widths for each column
        
        # Create the base grid
        rows = 8  # Total rows needed
        cols = 3  # Three columns: bit 1, bit 2, bit 3
        
        # Create all cells
        grid = VGroup()
        bit_values = VGroup()
        
        # First column (2 large cells)
        for i in range(2):
            cell = Rectangle(
                width=cell_widths[0],
                height=cell_height * 4,
                stroke_color=WHITE
            )
            if i > 0:
                cell.next_to(grid[-1], DOWN, buff=0)
            grid.add(cell)
            
            # Add 0 for first cell, 1 for second cell
            value = Text(str(i), font_size=24)
            value.move_to(cell.get_center() + LEFT*1.25 + UP*1.25)
            bit_values.add(value)
        
        # Second column (4 cells)
        second_col = VGroup()
        for i in range(4):
            cell = Rectangle(
                width=cell_widths[1],
                height=cell_height * 2,
                stroke_color=WHITE
            )
            if i > 0:
                cell.next_to(second_col[-1], DOWN, buff=0)
            second_col.add(cell)
            
            # Add alternating 0 and 1
            value = Text(str(i % 2), font_size=24)
            value.move_to(cell.get_center() + UP*1.75)
            bit_values.add(value)
            
        second_col.next_to(grid, RIGHT, buff=0)
        grid.add(second_col)
        
        # Third column (8 cells)
        third_col = VGroup()
        for i in range(8):
            cell = Rectangle(
                width=cell_widths[2],
                height=cell_height,
                stroke_color=WHITE
            )
            if i > 0:
                cell.next_to(third_col[-1], DOWN, buff=0)
            third_col.add(cell)
            
            # Add alternating 0 and 1
            value = Text(str(i % 2), font_size=24)
            value.move_to(cell.get_center() + RIGHT + UP*2)
            bit_values.add(value)
            
        third_col.next_to(second_col, RIGHT, buff=0)
        grid.add(third_col)
        
        # Add column labels
        labels = VGroup(
            Text("bit 1", font_size=24),
            Text("bit 2", font_size=24),
            Text("bit 3", font_size=24)
        )
        
        # Position labels under each column
        for i, label in enumerate(labels):
            if i == 0:
                label.next_to(grid[:2], DOWN)
            elif i == 1:
                label.next_to(second_col, DOWN)
            else:
                label.next_to(third_col, DOWN)

        # Center everything on the screen
        entire_scene = VGroup(grid, labels)
        entire_scene.move_to(ORIGIN)
        
        # Animations
        self.play(Create(grid))
        self.play(Write(bit_values))
        self.play(Write(labels))
        
        self.wait(2)

        self.play(
            FadeOut(entire_scene),
            FadeOut(bit_values),
        )

        encoded_string = Text("0 0 0 1 0 0 1 1", font_size=38)
        codewords_text = Text("0  10  0  111", font_size=50)
        source_text = Text("Flour Cheese Tomato Oil", font_size=22)
        
        # Create rounded rectangles
        def create_rounded_rect(text, color):
            return RoundedRectangle(
                width=text.width + 0.5,
                height=text.height + 0.3,
                corner_radius=0.2,
                fill_color=color,
                fill_opacity=0.3,
                stroke_color=WHITE
            )
        
        # Create boxes with colors
        encoded_box = create_rounded_rect(encoded_string, "#98FB98")  # Light green
        codewords_box = create_rounded_rect(codewords_text, "#98FB98")
        source_box = create_rounded_rect(source_text, "#C19EE0")  # Light purple
        
        # Create labels
        encoded_label = Text("encoded string", font_size=30)
        codewords_label = Text("codewords", font_size=30)
        source_label = Text("source symbols", font_size=30)
        
        # Create groups and position text in boxes
        encoded_group = VGroup(encoded_box, encoded_string)
        codewords_group = VGroup(codewords_box, codewords_text)
        source_group = VGroup(source_box, source_text)
        
        encoded_string.move_to(encoded_box)
        codewords_text.move_to(codewords_box)
        source_text.move_to(source_box)
        
        # Arrange boxes vertically with proper spacing
        boxes_group = VGroup(encoded_group, codewords_group, source_group).arrange(DOWN, buff=0.5)
        
        # Position labels to the right
        encoded_label.next_to(encoded_box, RIGHT, buff=0.5)
        codewords_label.next_to(codewords_box, RIGHT, buff=0.5)
        source_label.next_to(source_box, RIGHT, buff=0.5)
        
        # Group everything together
        entire_visualization = VGroup(
            encoded_group, encoded_label,
            codewords_group, codewords_label,
            source_group, source_label
        )
        
        # Position the visualization
        entire_visualization.next_to(grid, DOWN, buff=1)  # Assuming 'grid' is your code words table
        
        encoding_group = VGroup(encoded_group, codewords_group, source_group, encoded_label, codewords_label, source_label).move_to(ORIGIN)

        # Animate
        self.play(FadeIn(encoded_group), FadeIn(encoded_label))
        self.wait(0.5)
        self.play(FadeIn(codewords_group), FadeIn(codewords_label))
        self.wait(0.5)
        self.play(FadeIn(source_group), FadeIn(source_label))
        self.wait(2)
        self.play(FadeOut(encoding_group))

        # Create shaded grid with same dimensions as before
        shaded_grid = VGroup()
        shaded_values = VGroup()
        
        # First column (2 large cells)
        for i in range(2):
            cell = Rectangle(
                width=cell_widths[0],
                height=cell_height * 4,
                stroke_color=WHITE,
                fill_opacity=0
            )
            if i > 0:
                cell.next_to(shaded_grid[-1], DOWN, buff=0)
            shaded_grid.add(cell)
            
            value = Text(str(i), font_size=24)
            value.move_to(cell.get_center())
            shaded_values.add(value)
        
        # Second column (4 cells)
        second_col = VGroup()
        for i in range(4):
            cell = Rectangle(
                width=cell_widths[1],
                height=cell_height * 2,
                stroke_color=WHITE,
                fill_opacity=0
            )
            if i > 0:
                cell.next_to(second_col[-1], DOWN, buff=0)
            second_col.add(cell)
            
            value = Text(str(i % 2), font_size=24)
            value.move_to(cell.get_center() + RIGHT*1.25 + UP*0.5)
            shaded_values.add(value)
            
        second_col.next_to(shaded_grid, RIGHT, buff=0)
        shaded_grid.add(second_col)
        
        # Third column (8 cells)
        third_col = VGroup()
        for i in range(8):
            cell = Rectangle(
                width=cell_widths[2],
                height=cell_height,
                stroke_color=WHITE,
                fill_opacity=0
            )
            if i > 0:
                cell.next_to(third_col[-1], DOWN, buff=0)
            third_col.add(cell)
            
            value = Text(str(i % 2), font_size=24)
            value.move_to(cell.get_center() + RIGHT*2.25 + UP*0.75)
            shaded_values.add(value)
            
        third_col.next_to(second_col, RIGHT, buff=0)
        shaded_grid.add(third_col)

        # entire_scene = VGroup(shaded_grid, shaded_values)
        shaded_grid.move_to(ORIGIN)
        shaded_values.move_to(ORIGIN)


        # For the first column (shade the second large cell)
        first_col_fill = Rectangle(
            width=cell_widths[0],
            height=cell_height * 4,
            fill_color=GREY,
            fill_opacity=0.3,
            stroke_opacity=0
        )
        first_col_fill.move_to(shaded_grid[0].get_center())

        # For the second column (shade cells 0 and 2)
        second_col_fills = VGroup()
        for i in [1]:
            fill = Rectangle(
                width=cell_widths[1],
                height=cell_height * 2,
                fill_color=GREY,
                fill_opacity=0.3,
                stroke_opacity=0
            )
            fill.move_to(second_col[i].get_center())
            second_col_fills.add(fill)

        # For the third column (shade cells 2 and 3 with darker color)
        third_col_fills = Rectangle(
            width=cell_widths[2],
            height=cell_height * 2,
            fill_color=DARK_GREY,
            fill_opacity=0.9,
            stroke_opacity=0
        )
        # Position to cover cells 2 and 3
        # third_col_fills.move_to(third_col[2].get_center() + DOWN * cell_height/2)

        # Group all fills for animation
        all_fills = VGroup(first_col_fill, second_col_fills, third_col_fills)

        # Add fraction on the right
        side_values = VGroup()
        for i in range(8):
            side_value = Text(str(i % 2), font_size=24)
            side_value.next_to(third_col[i], RIGHT, buff=0.5)
            side_values.add(side_value)

        # Add fraction
        fraction = MathTex("\\frac{1}{2^L} = \\frac{1}{4}", font_size=36)
        third_col_fills.move_to(third_col.get_center() + UP*0.5)
        fraction.next_to(third_col_fills, RIGHT, buff=0.5)
        
        # Add labels
        labels = VGroup(
            Text("bit 1", font_size=24),
            Text("bit 2", font_size=24),
            Text("bit 3", font_size=24)
        )
        
        for i, label in enumerate(labels):
            if i == 0:
                label.next_to(shaded_grid[:2], DOWN)
            elif i == 1:
                label.next_to(second_col, DOWN)
            else:
                label.next_to(third_col, DOWN)
        
        
        # Animate
        self.play(FadeIn(shaded_grid))
        self.play(Write(shaded_values))
        self.play(Write(labels))
        self.play(FadeIn(first_col_fill), FadeIn(second_col_fills))
        self.wait(3)
        self.play(FadeIn(third_col_fills))  # Add fills after labels
        self.play(
            Write(fraction)
        )
        
        self.wait(2)

class OptimalEncoding(Scene):
    def construct(self):
        # Set background to black
        self.camera.background_color = BLACK
        
        # Create larger axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 1.2, 0.2],
            x_length=12,  # Increased length
            y_length=6,   # Increased height
            axis_config={
                "include_tip": False,
                "include_numbers": False,
                "stroke_color": WHITE
            }
        )

        # Labels
        x_label = MathTex("L(x)", color=WHITE).next_to(axes.x_axis, RIGHT)
        
        # Create left vertical line and 1 label
        left_line = Line(
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            color=WHITE
        )
        one_label = MathTex("1", color=WHITE).next_to(left_line, LEFT)

        # Create single cost function curve
        cost_curve = axes.plot(lambda x: 1/(2**x), x_range=[0, 8], color=WHITE)

        # Create rectangle that fits the curve
        # Width is L(x) = 1 unit, height is p(x) = 0.5 units
        rect = Rectangle(
            width=axes.x_length/8,  # 1 unit in x-axis
            height=axes.y_length/4,  # 0.5 units in y-axis
            fill_color="#9370DB",
            fill_opacity=1,
            stroke_color=WHITE
        )
        
        # Position rectangle to start at x=1
        rect.move_to(axes.c2p(0.5, 0.15))  # Center at (1, 0.25)
        
        # Box text
        box_text_p = MathTex("p(x)", color=WHITE).scale(0.7)
        box_text_length = Text("Average\nLength\nContribution", color=WHITE, font_size=15)
        box_group = VGroup(box_text_p, box_text_length).arrange(DOWN, buff=0.1)
        box_group.move_to(rect)

        # Get areas under different parts of the curve
        first_area = axes.get_area(
            graph=cost_curve,
            x_range=[0, 1],
            color=GREY,
            opacity=0.3
        )

        second_area = axes.get_area(
            graph=cost_curve,
            x_range=[1, 8],
            color="#9370DB",
            opacity=0.4
        )

        # Add Cost = 1/2^L(x) label
        cost_label = MathTex("Cost = \\frac{1}{2^{L(x)}}", color=WHITE).scale(0.8)
        cost_label.move_to(
            axes.c2p(3, 0.8)
        )

        # Rectangle starting position (top right)
        starting_rect = rect.copy()
        starting_text = box_group.copy()
        starting_group = VGroup(starting_rect, starting_text)
        starting_group.to_corner(UR, buff=0.5)

        # Animation sequence
        self.play(Create(axes))
        self.play(
            Create(left_line),
            Write(one_label),
            Write(x_label)
        )
        self.play(Create(cost_curve))
        self.play(FadeIn(first_area))
        self.play(FadeIn(second_area))
        self.play(Write(cost_label))
        
        # Animate the box
        self.play(Create(starting_rect), Write(starting_text))
        self.wait()
        self.play(
            Transform(starting_group, VGroup(rect, box_group))
        )
        
        self.wait(2)
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Create two smaller axes for the split view
        left_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 1.2, 0.2],
            x_length=5,
            y_length=3,  # Changed from y_height to y_length
            axis_config={
                "include_tip": False,
                "include_numbers": False,
                "stroke_color": WHITE
            }
        ).shift(LEFT * 3)

        right_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 1.2, 0.2],
            x_length=5,
            y_length=3,  # Changed from y_height to y_length
            axis_config={
                "include_tip": False,
                "include_numbers": False,
                "stroke_color": WHITE
            }
        ).shift(RIGHT * 3)

        # Create curves
        left_curve = left_axes.plot(lambda x: 1/(2**x), x_range=[0, 4], color=WHITE)
        right_curve = right_axes.plot(lambda x: 1/(2**x), x_range=[0, 4], color=WHITE)

        # Create vertical lines on left axis
        left_vertical_line = Line(
            left_axes.c2p(0, 0),
            left_axes.c2p(0, 1),
            color=WHITE
        )
        left_one_label = MathTex("1", color=WHITE).next_to(left_vertical_line, LEFT)

        # Create vertical lines on right axis
        right_vertical_line = Line(
            right_axes.c2p(0, 0),
            right_axes.c2p(0, 1),
            color=WHITE
        )
        right_one_label = MathTex("1", color=WHITE).next_to(right_vertical_line, LEFT)

        # Areas under the curve - modified for partial shading
        left_area = left_axes.get_area(
            left_curve,
            x_range=[0.5, 4],  # Grey area starts after purple rectangle
            color=GREY,
            opacity=0.5
        )

        right_area = right_axes.get_area(
            right_curve,
            x_range=[3, 4],  # Grey area starts after purple rectangle
            color=GREY,
            opacity=0.5
        )

        left_rect = Rectangle(
            width=0.5 * left_axes.x_length / 4,  # 0.5 units in x direction
            height=left_axes.y_length*0.5,  # Full height
            fill_color="#9370DB",
            fill_opacity=0.4,
            stroke_color=WHITE
        ).move_to(left_axes.c2p(0.25, 0.3))  # Position at x=0.25 (half of width)
        left_rect.align_to(left_axes.c2p(0, 0), LEFT)  # Align to left edge

        right_rect = Rectangle(
            width=0.75*right_axes.x_length,  # 0.5 units in x direction
            height=right_axes.y_length / 8,  # 0.25 height
            fill_color="#9370DB",
            fill_opacity=0.4,
            stroke_color=WHITE
        ).move_to(right_axes.c2p(0.4, 0.125))  # Position at x=2.75

        # Labels
        left_title = Text("Short Codeword,\nHigh Cost", 
                         color=WHITE, 
                         font_size=24).next_to(left_axes, UP)
        right_title = Text("Long Codeword,\nSmall Cost", 
                          color=WHITE, 
                          font_size=24).next_to(right_axes, UP)

        # x-axis labels
        left_x_label = MathTex("L(x)", color=WHITE).next_to(left_axes.x_axis, RIGHT)
        right_x_label = MathTex("L(x)", color=WHITE).next_to(right_axes.x_axis, RIGHT)

        # Animation sequence
        self.play(
            Create(left_axes),
            Create(right_axes)
        )
        self.play(
            Create(left_vertical_line),
            Create(right_vertical_line),
            Write(left_one_label),
            Write(right_one_label),
            Write(left_x_label),
            Write(right_x_label)
        )
        self.play(
            Create(left_curve),
            Create(right_curve)
        )
        self.play(
            FadeIn(left_area),
            FadeIn(right_area)
        )
        self.play(
            FadeIn(left_rect),
            FadeIn(right_rect)
        )
        self.play(
            Write(left_title),
            Write(right_title)
        )
        
        self.wait(2)
# Fade out previous scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Create axis
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-1.2, 1.2, 0.2],  # Modified to include negative y-values
            x_length=12,
            y_length=6,
            axis_config={
                "include_tip": False,
                "include_numbers": False,
                "stroke_color": WHITE
            }
        )

        # Create the two mirrored curves
        upper_curve = axes.plot(lambda x: 1/(2**x), x_range=[0, 8], color=WHITE)
        lower_curve = axes.plot(lambda x: -1/(2**x), x_range=[0, 8], color=WHITE)

        # Create rectangles for length contributions
        upper_length = Rectangle(
            width=2,
            height=0.5,
            fill_color="#9370DB",  # Purple
            fill_opacity=1,
            stroke_color=WHITE
        ).move_to(axes.c2p(1, 0.25))

        lower_length = Rectangle(
            width=4,
            height=0.5,
            fill_color="#DEB887",  # Tan
            fill_opacity=1,
            stroke_color=WHITE
        ).move_to(axes.c2p(2, -0.25))

        # Create shaded cost areas - modified approach
        upper_cost_points = [
            *[axes.c2p(x, 1/(2**x)) for x in np.linspace(2, 8, 100)],
            axes.c2p(8, 0),
            axes.c2p(2, 0)
        ]
        upper_cost = Polygon(
            *upper_cost_points,
            fill_color=GREY,
            fill_opacity=0.5,
            stroke_width=0
        )

        lower_cost_points = [
            *[axes.c2p(x, -1/(2**x)) for x in np.linspace(4, 8, 100)],
            axes.c2p(8, 0),
            axes.c2p(4, 0)
        ]
        lower_cost = Polygon(
            *lower_cost_points,
            fill_color=GREY,
            fill_opacity=0.3,
            stroke_width=0
        )

        # Labels
        pa_label = MathTex("p(a)", color=WHITE).next_to(axes.c2p(0, 0.5), LEFT)
        pb_label = MathTex("p(b)", color=WHITE).next_to(axes.c2p(0, -0.5), LEFT)

        upper_length_label = Text("Length\nContribution", color=WHITE, font_size=20).move_to(upper_length)
        upper_cost_label = Text("Cost", color=WHITE, font_size=20).move_to(axes.c2p(4, 0.5))

        lower_length_label = Text("Length\nContribution", color=WHITE, font_size=20).move_to(lower_length)
        lower_cost_label = Text("Cost", color=WHITE, font_size=20).move_to(axes.c2p(6, -0.5))

        # Animation sequence
        self.play(Create(axes))
        self.play(
            Create(upper_curve),
            Create(lower_curve)
        )
        
        # Animate upper curve elements
        self.play(
            Write(pa_label),
            Create(upper_length),
            Write(upper_length_label)
        )
        self.play(
            FadeIn(upper_cost),
            Write(upper_cost_label)
        )
        
        # Animate lower curve elements
        self.play(
            Write(pb_label),
            Create(lower_length),
            Write(lower_length_label)
        )
        self.play(
            FadeIn(lower_cost),
            Write(lower_cost_label)
        )
        
        self.wait(2)

        """
        Add all the necessary things after fixing the above
        """

class Entropy(Scene):
    def construct(self):
        # Create main rectangle and bars
        BAR_WIDTH = 4
        BAR_HEIGHT = 4
        
        # Create the first distribution (Weather)
        rect = Rectangle(height=BAR_HEIGHT, width=BAR_WIDTH, stroke_width=2)
        
        # Create bars with different heights and colors
        bars = VGroup(
            # 1/2
            Rectangle(height=BAR_HEIGHT/2, width=BAR_WIDTH)
            .set_fill(color="#C19EE0", opacity=1),
            # 1/4
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#FFB6C1", opacity=1),
            # 1/8
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#FFFFE0", opacity=1),
            # 1/8
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#98FB98", opacity=1),
        ).arrange(DOWN, buff=0)
        
        bars_group = VGroup(rect, bars)
        
        # Create vertical lines
        v_lines = VGroup()
        line_positions = [BAR_WIDTH/3, 2*BAR_WIDTH/3]  # Positions for solid lines
        
        for x_pos in line_positions:
            line = Line(
                start=UP * BAR_HEIGHT/2,
                end=DOWN * BAR_HEIGHT/2,
                stroke_width=2
            )
            line.move_to(LEFT * BAR_WIDTH/2 + RIGHT * x_pos)
            v_lines.add(line)
        
        # Add dotted line at the end
        dotted_line = DashedLine(
            start=UP * BAR_HEIGHT/2,
            end=DOWN * BAR_HEIGHT/2,
            stroke_width=2,
            dash_length=0.1
        )
        dotted_line.move_to(LEFT * BAR_WIDTH/2 + RIGHT * BAR_WIDTH)
        v_lines.add(dotted_line)
        
        # Probability labels
        prob_labels = VGroup(
            MathTex("\\frac{1}{2}", font_size=36),
            MathTex("\\frac{1}{4}", font_size=36),
            MathTex("\\frac{1}{8}", font_size=36),
            MathTex("\\frac{1}{8}", font_size=36)
        )
        
        for label, bar in zip(prob_labels, bars):
            label.next_to(bar, LEFT, buff=0.5)
        
        # Create bit labels
        bit_labels = VGroup(
            Text("1 bit", font_size=24),
            Text("2 bit", font_size=24),
            Text("3 bit", font_size=24)
        )
        
        # Position bit labels
        bit_positions = [-BAR_WIDTH/6, BAR_WIDTH/6, BAR_WIDTH/2]
        for label, x_pos in zip(bit_labels, bit_positions):
            label.move_to(LEFT * BAR_WIDTH/2 + RIGHT * x_pos)
            label.shift(DOWN * (BAR_HEIGHT/2 + 0.5))
        
        # p(x) label
        p_x_label = MathTex("p(x)", font_size=36).next_to(prob_labels, LEFT, buff=0.5)
        
        # L(x) formula
        l_x_formula = MathTex(
            "L(x) = \\log_2 \\left(\\frac{1}{p(x)}\\right)",
            font_size=36
        )
        l_x_formula.next_to(bars_group, RIGHT, buff=2)
        
        # Align everything to center and shift left
        full_viz = VGroup(bars_group, v_lines, prob_labels, bit_labels, p_x_label)
        full_viz.move_to(LEFT * 2)
        
        # Animation sequence
        self.play(
            Create(rect),
            FadeIn(bars),
            Create(v_lines)
        )
        self.play(
            Write(prob_labels),
            Write(p_x_label)
        )
        self.play(Write(bit_labels))
        self.play(Write(l_x_formula))
        
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Write entropy equation
        entropy_eq = MathTex(
            "H(p) = \\sum_{x} p(x) \\log_2 \\left(\\frac{1}{p(x)}\\right)",
            font_size=48
        ).move_to(ORIGIN)
        
        self.play(Write(entropy_eq))
        self.wait(2)

        # Fade out the entropy equation first
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)

        # Create title text
        dog_title = Text("Dog Lover's\nWord Frequency", font_size=24).to_edge(DOWN)
        cat_title = Text("Cat Lover's\nWord Frequency", font_size=24).to_edge(DOWN)
        
        # Constants for consistent styling
        BAR_HEIGHT = 4
        BAR_WIDTH = 1.5
        LEFT_SHIFT = 3
        
        # Create dog lover's distribution (keeping order: dog, cat, fish, bird)
        dog_rect = Rectangle(height=BAR_HEIGHT, width=BAR_WIDTH, stroke_width=2)
        dog_parts = VGroup(
            # Dog (1/2)
            Rectangle(height=BAR_HEIGHT/2, width=BAR_WIDTH)
            .set_fill(color="#C19EE0", opacity=1),
            # Cat (1/4) 
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#FFB6C1", opacity=1),
            # Fish (1/8)
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#FFFFE0", opacity=1),
            # Bird (1/8)
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#98FB98", opacity=1),
        ).arrange(DOWN, buff=0)
        
        dog_group = VGroup(dog_rect, dog_parts)
        
        # Dog labels in same order
        dog_labels = VGroup(
            Text('"dog"', font_size=20),
            Text('"cat"', font_size=20),
            Text('"fish"', font_size=20),
            Text('"bird"', font_size=20)
        )
        
        dog_prob_labels = VGroup(
            Text("1/2", font_size=20),
            Text("1/4", font_size=20), 
            Text("1/8", font_size=20),
            Text("1/8", font_size=20)
        )
        
        for label, prob, part in zip(dog_labels, dog_prob_labels, dog_parts):
            label.move_to(part)
            prob.next_to(part, LEFT, buff=0.3)
            
        p_x_label = MathTex("p(x)", font_size=36).next_to(dog_prob_labels, LEFT, buff=0.5)
        
        dog_full_group = VGroup(dog_group, dog_labels, dog_prob_labels, p_x_label, dog_title)
        dog_full_group.move_to(LEFT * LEFT_SHIFT)
        
        # Create cat lover's distribution (keeping same order: dog, cat, fish, bird)
        cat_rect = Rectangle(height=BAR_HEIGHT, width=BAR_WIDTH, stroke_width=2)
        cat_parts = VGroup(
            # Dog (1/8)
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#C19EE0", opacity=1),
            # Cat (1/2)
            Rectangle(height=BAR_HEIGHT/2, width=BAR_WIDTH)
            .set_fill(color="#FFB6C1", opacity=1),
            # Fish (1/4)
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#FFFFE0", opacity=1),
            # Bird (1/8)
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)
            .set_fill(color="#98FB98", opacity=1),
        ).arrange(DOWN, buff=0)
        
        cat_group = VGroup(cat_rect, cat_parts)
        
        # Cat labels in same order
        cat_labels = VGroup(
            Text('"dog"', font_size=20),
            Text('"cat"', font_size=20),
            Text('"fish"', font_size=20),
            Text('"bird"', font_size=20)
        )
        
        cat_prob_labels = VGroup(
            Text("1/8", font_size=20),
            Text("1/2", font_size=20),
            Text("1/4", font_size=20),
            Text("1/8", font_size=20)
        )
        
        for label, prob, part in zip(cat_labels, cat_prob_labels, cat_parts):
            label.move_to(part)
            prob.next_to(part, LEFT, buff=0.3)
            
        q_x_label = MathTex("q(x)", font_size=36).next_to(cat_prob_labels, LEFT, buff=0.5)
        
        cat_full_group = VGroup(cat_group, cat_labels, cat_prob_labels, q_x_label, cat_title)
        cat_full_group.move_to(RIGHT * LEFT_SHIFT)

        # Add KL divergence equation in the middle
        kl_eq = MathTex(
            "\\sum_x p(x) \\log_2 \\left(\\frac{1}{p(x)}\\right)",
            font_size=36
        ).move_to(ORIGIN)
        
        # Animation sequence
        self.play(
            Create(dog_rect),
            Create(cat_rect)
        )
        self.play(
            FadeIn(dog_parts),
            FadeIn(cat_parts)
        )
        self.play(
            Write(dog_labels),
            Write(cat_labels)
        )
        self.play(
            Write(dog_prob_labels),
            Write(cat_prob_labels),
            Write(p_x_label),
            Write(q_x_label)
        )
        self.play(
            Write(dog_title),
            Write(cat_title)
        )
        
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)

        # Write cross entropy equation
        cross_entropy_eq = MathTex(
            "H_p(q) = \\sum_x q(x) \\log_2 \\left(\\frac{1}{p(x)}\\right)",
            font_size=48
        ).move_to(ORIGIN)
        
        self.play(Write(cross_entropy_eq))
        self.wait(2)

        # Fade out equation
        self.play(FadeOut(cross_entropy_eq))
        
        # Constants for the bars
        BAR_HEIGHT = 4
        BAR_WIDTH = 1.5
        
        # Create p(x) distribution with different heights
        p_rect = Rectangle(height=BAR_HEIGHT, width=BAR_WIDTH, stroke_width=2)
        p_parts = VGroup(
            Rectangle(height=BAR_HEIGHT/2, width=BAR_WIDTH)  # x1 - 1/2
            .set_fill(color="#C19EE0", opacity=1),
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)  # x2 - 1/4
            .set_fill(color="#FFB6C1", opacity=1),
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)  # x3 - 1/8
            .set_fill(color="#FFFFE0", opacity=1),
            Rectangle(height=BAR_HEIGHT/8, width=BAR_WIDTH)  # x4 - 1/8
            .set_fill(color="#98FB98", opacity=1),
        ).arrange(DOWN, buff=0)
        
        p_group = VGroup(p_rect, p_parts)

        # Create x labels for p(x)
        p_labels = VGroup(
            MathTex("x_1", font_size=24),
            MathTex("x_2", font_size=24),
            MathTex("x_3", font_size=24),
            MathTex("x_4", font_size=24)
        )
        
        for label, part in zip(p_labels, p_parts):
            label.move_to(part)

        p_x_label = MathTex("p(x)", font_size=36).next_to(p_rect, UP, buff=0.3)
        p_full_group = VGroup(p_group, p_labels, p_x_label)
        p_full_group.move_to(LEFT * 4)  # Move more to the left

        # Create q(x) distribution with equal heights
        q_rect = Rectangle(height=BAR_HEIGHT, width=BAR_WIDTH, stroke_width=2)
        q_parts = VGroup(
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)  # Equal parts
            .set_fill(color="#C19EE0", opacity=1),
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#FFB6C1", opacity=1),
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#FFFFE0", opacity=1),
            Rectangle(height=BAR_HEIGHT/4, width=BAR_WIDTH)
            .set_fill(color="#98FB98", opacity=1),
        ).arrange(DOWN, buff=0)
        
        q_group = VGroup(q_rect, q_parts)

        # Create x labels for q(x)
        q_labels = VGroup(
            MathTex("x_1", font_size=24),
            MathTex("x_2", font_size=24),
            MathTex("x_3", font_size=24),
            MathTex("x_4", font_size=24)
        )
        
        for label, part in zip(q_labels, q_parts):
            label.move_to(part)

        q_x_label = MathTex("q(x)", font_size=36).next_to(q_rect, UP, buff=0.3)
        q_full_group = VGroup(q_group, q_labels, q_x_label)
        q_full_group.next_to(p_full_group, RIGHT, buff=1)

        # Create title and explanation on the right
        title = Text("Cross-Entropy: Hp(q)", font_size=36)
        explanation = VGroup(
            Text("Average Length", font_size=30),
            Text("of message from q(x)", font_size=30),
            Text("using code for p(x).", font_size=30)
        ).arrange(DOWN, buff=0.2)
        
        text_group = VGroup(title, explanation).arrange(DOWN, buff=0.5)
        text_group.next_to(q_full_group, RIGHT, buff=2)  # Position text on the right

        # Animation sequence
        self.play(
            Create(p_rect),
            Create(q_rect)
        )
        self.play(
            FadeIn(p_parts),
            FadeIn(q_parts)
        )
        self.play(
            Write(p_labels),
            Write(q_labels)
        )
        self.play(
            Write(p_x_label),
            Write(q_x_label)
        )
        self.play(
            Write(title),
            Write(explanation)
        )
        
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)

        # Create the header text
        header = Text("So, now we have four possibilities:", font_size=36)
        header.to_edge(UP)

        # Create bullet points
        bullets = VGroup(
            # First bullet
            Text(
                "• Bob using his own code (H(p) = 1.75 bits)",
                font_size=30,
                t2c={"H(p)": BLUE} # Color the equation
            ),
            # Second bullet
            Text(
                "• Alice using Bob's code (Hp(q) = 2.25 bits)", 
                font_size=30,
                t2c={"Hp(q)": BLUE}
            ),
            # Third bullet
            Text(
                "• Alice using her own code (H(q) = 1.75 bits)",
                font_size=30,
                t2c={"H(q)": BLUE}
            ),
            # Fourth bullet
            Text(
                "• Bob using Alice's code (Hq(p) = 2.375 bits)",
                font_size=30,
                t2c={"Hq(p)": BLUE}
            )
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        bullets.next_to(header, DOWN, buff=0.75)

        # Position everything slightly up
        entire_group = VGroup(header, bullets)
        entire_group.move_to(ORIGIN)
        entire_group.shift(UP * 0.5)

        # Animation sequence
        self.play(Write(header))
        self.play(Write(bullets[0]))
        self.wait(0.3)
        self.play(Write(bullets[1]))
        self.wait(0.3)
        self.play(Write(bullets[2]))
        self.wait(0.3)
        self.play(Write(bullets[3]))
        
        self.wait(2)

        # After showing the bullets, instead of fading them out, transform them directly

        # Create equations
        hp_eq = MathTex("H(p) = H_p(p) = 1.75 \\text{ bits}", font_size=36)
        hpq_eq = MathTex("H_p(q) = 2.25 \\text{ bits}", font_size=36)
        hqp_eq = MathTex("H_q(p) = 2.375 \\text{ bits}", font_size=36)
        hq_eq = MathTex("H(q) = H_q(q) = 1.75 \\text{ bits}", font_size=36)

        # Position equations in corners
        hp_eq.to_corner(UL)
        hpq_eq.to_corner(DL) 
        hqp_eq.to_corner(UR)
        hq_eq.to_corner(DR)

        # Transform bullets to equations and fade out header
        self.play(
            Transform(bullets[0], hp_eq),
            Transform(bullets[1], hpq_eq),
            Transform(bullets[2], hq_eq),
            Transform(bullets[3], hqp_eq),
            FadeOut(header)
        )
        self.wait(0.5)

        """
        FIX BARS
        """

        # Constants for bars - scaled down
        BAR_WIDTH = 2  # Reduced from 4 to 2
        BAR_HEIGHT = 0.25  # Reduced from 0.5 to 0.25
        LEFT_SHIFT = 3

        # Function to create the bars with left alignment
        def create_length_bars(colors, lengths, label, eq_text, position):
            bars = VGroup()
            max_width = max(lengths) * BAR_WIDTH  # For alignment reference
            
            for color, length in zip(colors, lengths):
                bar = Rectangle(
                    width=length * BAR_WIDTH,
                    height=BAR_HEIGHT,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_color=WHITE
                )
                # Ensure all bars start from the same left position
                if len(bars) == 0:
                    bars.add(bar)
                else:
                    bar.next_to(bars[-1], DOWN, buff=0.1)
                    bar.align_to(bars[0], LEFT)  # Align each bar to the first bar's left edge
            
            p_label = Text(label, font_size=24).next_to(bars, LEFT)
            l_label = Text(eq_text, font_size=24).next_to(bars, DOWN, buff=0.3)
            
            group = VGroup(bars, p_label, l_label)
            group.move_to(position)
            return group

        # Colors for the bars
        colors = ["#C19EE0", "#FFB6C1", "#FFFFE0", "#98FB98"]

        # Create the four visualizations with accurate lengths
        hp = create_length_bars(
            colors,
            [1, 2, 2.5, 2.5],  # Hp(p)
            "p(x)", 
            "Lp(x)",
            UP * 1.5 + LEFT * LEFT_SHIFT
        )

        hpq = create_length_bars(
            colors,
            [1, 2.5, 3, 3],  # Hp(q)
            "q(x)",
            "Lp(x)", 
            DOWN * 1.5 + LEFT * LEFT_SHIFT
        )

        hqp = create_length_bars(
            colors, 
            [3, 1.5, 2, 2.5],  # Hq(p)
            "p(x)",
            "Lq(x)",
            UP * 1.5 + RIGHT * LEFT_SHIFT
        )

        hq = create_length_bars(
            colors,
            [2.5, 1.5, 2, 2.5],  # Hq(q)
            "q(x)",
            "Lq(x)",
            DOWN * 1.5 + RIGHT * LEFT_SHIFT
        )

        # Animation sequence
        for viz in [hp, hpq, hqp, hq]:
            self.play(
                Create(viz[0]),  # bars
                Write(viz[1]),   # p(x)/q(x) label
                Write(viz[2])    # L(x) label
            )
            self.wait(0.3)

        self.wait(2)

class KLDivergence(Scene):
    def construct(self):
        # First set of boxes
        h_p = Rectangle(width=3, height=0.8, color=RED_A)
        h_q_p = Rectangle(width=4, height=0.8, color=RED_B)
        d_q_p = Rectangle(width=1.2, height=0.8, color=PURPLE_A)
        
        # Labels for first set
        h_p_label = MathTex("H(p)").move_to(h_p).shift(UP * 0.1)
        h_q_p_label = MathTex("H_q(p)").move_to(h_q_p).shift(DOWN * 0.1)
        d_q_p_label = MathTex("D_q(p)").move_to(d_q_p).shift(UP * 0.1)
        
        # Position first set - adjacent
        h_p.to_edge(LEFT, buff=3)
        h_q_p.next_to(h_p, RIGHT, buff=0, aligned_edge=LEFT)
        d_q_p.next_to(h_q_p, RIGHT, buff=0)
        
        # Second set of boxes
        h_q = Rectangle(width=3, height=0.8, color=BLUE_A)
        h_p_q = Rectangle(width=4, height=0.8, color=BLUE_B)
        d_p_q = Rectangle(width=1.2, height=0.8, color=PURPLE_A)
        
        # Labels for second set
        h_q_label = MathTex("H(q)").move_to(h_q).shift(UP * 0.1)
        h_p_q_label = MathTex("H_p(q)").move_to(h_p_q).shift(DOWN * 0.1)
        d_p_q_label = MathTex("D_p(q)").move_to(d_p_q).shift(UP * 0.1)
        
        # Position second set - adjacent
        second_group = VGroup(h_q, h_p_q, d_p_q)
        second_group.arrange(RIGHT, buff=0, aligned_edge=LEFT)
        second_group.next_to(h_q_p, DOWN, buff=2)
        
        # Animations
        self.play(
            Create(h_p),
            Create(h_q_p),
            Create(d_q_p),
            Write(h_p_label),
            Write(h_q_p_label),
            Write(d_q_p_label)
        )
        self.wait()
        
        self.play(
            Create(h_q),
            Create(h_p_q),
            Create(d_p_q),
            Write(h_q_label),
            Write(h_p_q_label),
            Write(d_p_q_label)
        )
        self.wait(2)

"""
Below this not required for KLD or cross entropy
"""

# class EntropyAndMultiVariables(Scene):
#     def construct(self):
#         # Create main square
#         square_size = 4
#         main_square = Square(side_length=square_size, stroke_width=2)
        
#         # Create sections with proportions
#         sections = VGroup(
#             # Bottom left (sunny, t-shirt) - 56%
#             Rectangle(height=square_size * 0.92, width=square_size * 0.62)
#             .set_fill(color="#E8E8AA", opacity=1),
#             # Bottom right (sunny, coat) - 19%
#             Rectangle(height=square_size * 0.50, width=square_size * 0.38)
#             .set_fill(color="#C1C178", opacity=1),
#             # Top left (rain, t-shirt) - 6%
#             Rectangle(height=square_size * 0.08, width=square_size * 0.62)
#             .set_fill(color="#9370DB", opacity=1),
#             # Top right (rain, coat) - 19%
#             Rectangle(height=square_size * 0.50, width=square_size * 0.38)
#             .set_fill(color="#9370DB", opacity=1),
#         )

#         # Position sections
#         sections[0].move_to(main_square.get_bottom(), aligned_edge=DOWN).align_to(main_square, LEFT)
#         sections[1].move_to(main_square.get_bottom(), aligned_edge=DOWN).align_to(main_square, RIGHT)
#         sections[2].move_to(sections[0].get_top(), aligned_edge=DOWN)
#         sections[3].move_to(sections[1].get_top(), aligned_edge=DOWN)

#         # Create title
#         title = MathTex("P(X,", "\\,", "Y)").scale(0.8)
#         clothing = Text("clothing", font_size=24).next_to(title[0], DOWN, buff=0.1)
#         weather = Text("weather", font_size=24).next_to(title[2], DOWN, buff=0.1)
#         title_group = VGroup(title, clothing, weather).arrange_in_grid(rows=2, cols=3, buff=0.1)
#         title_group.next_to(main_square, UP, buff=0.3)

#         # Create percentage labels
#         percentage_labels = VGroup(
#             Text("56%", font_size=36, color=BLACK).move_to(sections[0]),
#             Text("19%", font_size=36, color=BLACK).move_to(sections[1]),
#             Text("6%", font_size=36, color=WHITE).move_to(sections[2]),
#             Text("19%", font_size=36, color=WHITE).move_to(sections[3])
#         )

#         # Create side labels
#         left_labels = VGroup(
#             VGroup(
#                 Text("raining", font_size=24),
#                 Text("8%", font_size=24)
#             ).arrange(DOWN, buff=0.1),
#             VGroup(
#                 Text("sunny", font_size=24),
#                 Text("92%", font_size=24)
#             ).arrange(DOWN, buff=0.1)
#         ).arrange(DOWN, buff=1.5).next_to(main_square, LEFT, buff=0.5)

#         right_labels = VGroup(
#             VGroup(
#                 Text("raining", font_size=24),
#                 Text("50%", font_size=24)
#             ).arrange(DOWN, buff=0.1),
#             VGroup(
#                 Text("sunny", font_size=24),
#                 Text("50%", font_size=24)
#             ).arrange(DOWN, buff=0.1)
#         ).arrange(DOWN, buff=1.5).next_to(main_square, RIGHT, buff=0.5)

#         # Create bottom labels
#         bottom_labels = VGroup(
#             VGroup(
#                 Text("t-shirt", font_size=24),
#                 Text("62%", font_size=24)
#             ).arrange(DOWN, buff=0.1),
#             VGroup(
#                 Text("coat", font_size=24),
#                 Text("38%", font_size=24)
#             ).arrange(DOWN, buff=0.1)
#         ).arrange(RIGHT, buff=2).next_to(main_square, DOWN, buff=0.5)

#         VGroup(main_square, sections, title_group, percentage_labels, left_labels, right_labels, bottom_labels).animate.move_to(ORIGIN)

#         # Animations
#         self.play(Create(main_square))
#         self.play(Create(sections))
#         self.play(Write(title_group))
#         self.play(Write(percentage_labels))
#         self.play(
#             Write(left_labels),
#             Write(right_labels)
#         )
#         self.play(Write(bottom_labels))
#         self.wait(2)

#         # Group everything for movement
#         all_elements = VGroup(
#             main_square, sections, title_group, percentage_labels,
#             left_labels, right_labels, bottom_labels
#         )

#         # Move everything to the left
#         self.play(
#             all_elements.animate.shift(LEFT * 3)
#         )
#         self.wait()

#         # Create arrow
#         arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, buff=0.3, color=WHITE)
#         self.play(Create(arrow))

#         # Create flattened rectangle
#         rect_height = 4  # Same as square_size
#         rect_width = 1.5
        
#         flat_sections = VGroup(
#             # Raining & t-shirt (6%)
#             Rectangle(height=rect_height * 0.06, width=rect_width)
#             .set_fill(color="#9370DB", opacity=1),
#             # Raining & coat (19%)
#             Rectangle(height=rect_height * 0.19, width=rect_width)
#             .set_fill(color="#9370DB", opacity=1),
#             # Sunny & t-shirt (56%)
#             Rectangle(height=rect_height * 0.56, width=rect_width)
#             .set_fill(color="#E8E8AA", opacity=1),
#             # Sunny & coat (19%)
#             Rectangle(height=rect_height * 0.19, width=rect_width)
#             .set_fill(color="#C1C178", opacity=1)
#         ).arrange(DOWN, buff=0)
        
#         flat_rect = Rectangle(height=rect_height, width=rect_width, stroke_width=2)
#         flat_group = VGroup(flat_rect, flat_sections).move_to(RIGHT * 3)

#         # Labels for flattened rectangle
#         flat_labels = VGroup(
#             Text("6%   raining & t-shirt", font_size=24),
#             Text("19%  raining & coat", font_size=24),
#             Text("56%  sunny & t-shirt", font_size=24),
#             Text("19%  sunny & coat", font_size=24)
#         )

#         for label, section in zip(flat_labels, flat_sections):
#             label.next_to(section, RIGHT, buff=0.5)

#         self.play(
#             Create(flat_rect),
#             Create(flat_sections)
#         )
#         self.play(Write(flat_labels))
#         self.wait(2)

#         # Fade out previous elements
#         self.play(*[FadeOut(mob) for mob in self.mobjects])
#         self.wait()

#         # Create title
#         title = MathTex("H(X, Y)").scale(1.2)
#         title.to_edge(UP, buff=0.5)
        
#         # Create axes lines and labels
#         x_line = Line(LEFT * 2, RIGHT * 4, stroke_width=1)
#         x_labels = VGroup(
#             Text("1 bit", font_size=24),
#             Text("2 bit", font_size=24),
#             Text("3 bit", font_size=24),
#             Text("4 bit", font_size=24)
#         )
        
#         for i, label in enumerate(x_labels):
#             label.next_to(x_line, DOWN, buff=0.3)
#             label.shift(RIGHT * (i - 1))

#         # Create bars
#         bar_height = 0.5
#         bars = VGroup(
#             # 6% bar (4 bits)
#             Rectangle(height=bar_height, width=6, color=WHITE, fill_color="#9370DB", fill_opacity=1),
#             # 19% bar (2.5 bits)
#             Rectangle(height=bar_height, width=3.75, color=WHITE, fill_color="#9370DB", fill_opacity=0.8),
#             # 56% bar (1 bit)
#             Rectangle(height=bar_height, width=1.5, color=WHITE, fill_color="#E8E8AA", fill_opacity=1),
#             # 19% bar (2 bits)
#             Rectangle(height=bar_height, width=3, color=WHITE, fill_color="#C1C178", fill_opacity=1)
#         )
        
#         # Position bars
#         bars.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
#         bars.next_to(x_line, UP, buff=1)
        
#         # Add percentage labels
#         percentages = VGroup(
#             Text("6%", font_size=24),
#             Text("19%", font_size=24),
#             Text("56%", font_size=24),
#             Text("19%", font_size=24)
#         )
        
#         for percentage, bar in zip(percentages, bars):
#             percentage.next_to(bar, LEFT, buff=0.3)

#         # Add dotted vertical lines
#         vertical_lines = VGroup()
#         for i in range(4):
#             line = DashedLine(
#                 UP * 4, DOWN * 1,
#                 dash_length=0.1,
#                 stroke_width=1,
#                 color=GRAY
#             ).move_to(x_line.get_left() + RIGHT * (i + 1))
#             vertical_lines.add(line)

#         # Animations
#         self.play(Write(title))
#         self.play(Create(x_line), Create(vertical_lines))
#         self.play(Write(x_labels))
        
#         for bar, percentage in zip(bars, percentages):
#             self.play(
#                 Create(bar),
#                 Write(percentage)
#             )
        
#         self.wait(2)

#         self.play(*[FadeOut(mob) for mob in self.mobjects])
#         self.wait()

# class EntropyIn3D(ThreeDScene):
#     def construct(self):
#         # Set the camera orientation
#         self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
#         # Create the axes
#         axes = ThreeDAxes(
#             x_range=[0, 2, 1],
#             y_range=[0, 2, 1],
#             z_range=[0, 4, 1],
#             x_length=4,
#             y_length=4,
#             z_length=6
#         )
        
#         # Create title and axis labels
#         title = MathTex("L(x,y)", "= -\\log_2 \\frac{1}{p(x,y)}")
#         title.to_corner(UL)
#         x_label = Text("t-shirt", font_size=24)
#         y_label = Text("coat", font_size=24)
        
#         # Create the prisms
#         # Raining & t-shirt (tallest, 4 bits)
#         rain_tshirt = Prism(
#             dimensions=[1, 1, 4],
#             fill_color="#9370DB",
#             fill_opacity=0.8
#         )
        
#         # Raining & coat (2.5 bits)
#         rain_coat = Prism(
#             dimensions=[1, 1, 2.5],
#             fill_color="#9370DB",
#             fill_opacity=0.8
#         )
        
#         # Sunny & t-shirt (1 bit)
#         sunny_tshirt = Prism(
#             dimensions=[1, 1, 1],
#             fill_color="#E8E8AA",
#             fill_opacity=0.8
#         )
        
#         # Sunny & coat (2 bits)
#         sunny_coat = Prism(
#             dimensions=[1, 1, 2],
#             fill_color="#E8E8AA",
#             fill_opacity=0.8
#         )
        
#         # Position the prisms
#         rain_tshirt.move_to(axes.c2p(0, 0, 2))
#         rain_coat.move_to(axes.c2p(1, 0, 1.25))
#         sunny_tshirt.move_to(axes.c2p(0, 1, 0.5))
#         sunny_coat.move_to(axes.c2p(1, 1, 1))
        
#         # Create side labels
#         weather_label = Text("weather", font_size=24).rotate(90 * DEGREES)
#         prob_label = MathTex("p(x,y)", font_size=24)
        
#         # Animations
#         self.play(Create(axes))
#         self.play(Write(title))
        
#         # Add prisms one by one
#         self.play(Create(rain_tshirt))
#         self.play(Create(rain_coat))
#         self.play(Create(sunny_tshirt))
#         self.play(Create(sunny_coat))
        
#         # Rotate the camera to show the 3D nature
#         self.begin_ambient_camera_rotation(rate=0.2)
#         self.wait(3)
#         self.stop_ambient_camera_rotation()
        
#         # Final pause
#         self.wait(2)

        
#         # Stop any ongoing camera movement
#         self.stop_ambient_camera_rotation()
        
#         # Create new axes for split view
#         axes_left = ThreeDAxes(
#             x_range=[0, 2, 1],
#             y_range=[0, 2, 1],
#             z_range=[0, 4, 1],
#             x_length=4,
#             y_length=4,
#             z_length=6
#         ).shift(LEFT * 4)

#         axes_right = ThreeDAxes(
#             x_range=[0, 2, 1],
#             y_range=[0, 2, 1],
#             z_range=[0, 4, 1],
#             x_length=4,
#             y_length=4,
#             z_length=6
#         ).shift(RIGHT * 4)

#         # New titles
#         left_title = MathTex("H(X|Y = raining)").next_to(axes_left, UP)
#         right_title = MathTex("H(X|Y = sunny)").next_to(axes_right, UP)

#         # First transform the axes and add new ones
#         self.play(
#             Transform(axes, VGroup(axes_left, axes_right)),
#             Transform(title, VGroup(left_title, right_title))
#         )

#         # Move purple prisms to left side
#         self.play(
#             rain_tshirt.animate.move_to(axes_left.c2p(0, 0, 2)),
#             rain_coat.animate.move_to(axes_left.c2p(1, 0, 1.25))
#         )

#         # Move yellow prisms to right side
#         self.play(
#             sunny_tshirt.animate.move_to(axes_right.c2p(0, 0, 0.5)),
#             sunny_coat.animate.move_to(axes_right.c2p(1, 0, 1))
#         )

#         # Add new labels
#         labels_left = VGroup(
#             Text("t-shirt", font_size=24).next_to(axes_left.x_axis, RIGHT),
#             Text("coat", font_size=24).next_to(axes_left.y_axis, RIGHT),
#             Text("raining", font_size=24).next_to(axes_left, DOWN)
#         )

#         labels_right = VGroup(
#             Text("t-shirt", font_size=24).next_to(axes_right.x_axis, RIGHT),
#             Text("coat", font_size=24).next_to(axes_right.y_axis, RIGHT),
#             Text("sunny", font_size=24).next_to(axes_right, DOWN)
#         )

#         self.play(
#             Write(labels_left),
#             Write(labels_right)
#         )

#         self.wait(2)

#         # Add this at the end of your construct method, after self.wait(2):

#         # Create new axes for joint probability
#         joint_axes = ThreeDAxes(
#             x_range=[0, 2, 1],
#             y_range=[0, 2, 1],
#             z_range=[0, 4, 1],
#             x_length=4,
#             y_length=4,
#             z_length=6
#         )

#         # New title for joint probability
#         joint_title = MathTex("H(X|Y)", "= 0.81\\ bits").to_corner(UL)

#         # Move all prisms back to center
#         self.play(
#             Transform(VGroup(axes_left, axes_right), joint_axes),
#             Transform(VGroup(left_title, right_title), joint_title),
#             rain_tshirt.animate.move_to(joint_axes.c2p(0, 0, 2)),
#             rain_coat.animate.move_to(joint_axes.c2p(1, 0, 1.25)),
#             sunny_tshirt.animate.move_to(joint_axes.c2p(0, 1, 0.5)),
#             sunny_coat.animate.move_to(joint_axes.c2p(1, 1, 1)),
#             FadeOut(labels_left),
#             FadeOut(labels_right)
#         )

#         # Add final labels
#         final_labels = VGroup(
#             Text("t-shirt", font_size=24).next_to(joint_axes.x_axis, RIGHT),
#             Text("coat", font_size=24).next_to(joint_axes.y_axis, RIGHT),
#             VGroup(
#                 Text("raining", font_size=20),
#                 Text("sunny", font_size=20).next_to(Text("raining", font_size=20), DOWN)
#             ).next_to(joint_axes, LEFT)
#         )

#         self.play(Write(final_labels))

#         # Final rotation to match the image perspective
#         self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES)
#         self.wait(2)

#         # Add this after your last self.wait(2):

#         # Create the equations
#         eq1 = MathTex(
#             "H(X|Y)", "=", "\\sum_y", "p(y)", "\\sum_x", "p(x|y)", "\\log_2", "\\left(\\frac{1}{p(x|y)}\\right)"
#         ).scale(0.9)

#         eq2 = MathTex(
#             "=", "\\sum_{x,y}", "p(x,y)", "\\log_2", "\\left(\\frac{1}{p(x|y)}\\right)"
#         ).scale(0.9)

#         # Position equations
#         eq1.shift(UP * 0.5)
#         eq2.shift(DOWN * 0.5)
#         eq2.align_to(eq1, LEFT)

#         # Group equations
#         equations = VGroup(eq1, eq2)
#         equations.center()

#         # Add text above
#         text = Text("We call this the conditional entropy. If you formalize it into an equation, you get:", 
#                     font_size=36).next_to(equations, UP * 2)

#         # Fade out everything except camera
#         self.play(
#             *[FadeOut(mob) for mob in self.mobjects if not isinstance(mob, Camera)],
#             run_time=1.5
#         )

#         # Show text and equations
#         self.play(Write(text))
#         self.wait(0.5)
#         self.play(Write(eq1))
#         self.wait(1)
#         self.play(Write(eq2))
#         self.wait(2)