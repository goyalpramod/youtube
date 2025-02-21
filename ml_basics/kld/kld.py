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

class TextKLD(Scene):
    def construct(self):
        text = Text("Kullback Leibler Divergence", font_size=72)
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))

"""
Replace the examples with pizza and cooking utensil 

Pizza Style & Cooking Method

Style: {Thin crust (60%), Thick crust (40%)}
Method: {Oven (55%), Pan (45%)}
These are dependent because thin crust pizzas are more commonly cooked on stones for crispiness.
"""
class IndependentProbabilityDistributions(Scene):
    def construct(self):
        # Constants for probabilities
        WEATHER_RAIN_PROB = 0.25
        WEATHER_SUNNY_PROB = 0.75
        CLOTHING_TSHIRT_PROB = 0.60  # Corrected from 0.60 to 0.62
        CLOTHING_COAT_PROB = 0.40    # Corrected from 0.40 to 0.38

        # Create the first distribution (Weather)
        weather_rect = Rectangle(height=4, width=1, stroke_width=2)
        weather_parts = VGroup(
            # Sunny (bottom)
            Rectangle(height=4*WEATHER_SUNNY_PROB, width=1)
            .set_fill(color=YELLOW_A, opacity=0.8),
            # Raining (top)
            Rectangle(height=4*WEATHER_RAIN_PROB, width=1)
            .set_fill(color=BLUE_D, opacity=1),
        ).arrange(UP, buff=0)
        
        weather_group = VGroup(weather_rect, weather_parts)
        
        # Weather labels
        weather_title = Text("weather", font_size=24)
        weather_title.next_to(weather_group, UP, buff=0.3)
        
        weather_labels = VGroup(
            Text(f"raining\n{int(WEATHER_RAIN_PROB*100)}%", font_size=20),
            Text(f"sunny\n{int(WEATHER_SUNNY_PROB*100)}%", font_size=20)
        )
        weather_labels[0].next_to(weather_parts[1], LEFT, buff=0.3)
        weather_labels[1].next_to(weather_parts[0], LEFT, buff=0.3)
        
        weather_full_group = VGroup(weather_group, weather_title, weather_labels)
        weather_full_group.move_to(LEFT*3)

        # Create second distribution (Clothing)
        clothing_rect = Rectangle(height=4, width=1, stroke_width=2)
        clothing_parts = VGroup(
            # T-shirt (bottom)
            Rectangle(height=4*CLOTHING_TSHIRT_PROB, width=1)
            .set_fill(color=YELLOW_A, opacity=0.5),
            # Coat (top)
            Rectangle(height=4*CLOTHING_COAT_PROB, width=1)
            .set_fill(color=YELLOW_B, opacity=0.5),
        ).arrange(UP, buff=0)
        
        clothing_group = VGroup(clothing_rect, clothing_parts)
        
        # Clothing labels
        clothing_title = Text("clothing", font_size=24)
        clothing_title.next_to(clothing_group, UP, buff=0.3)
        
        clothing_labels = VGroup(
            Text(f"coat\n{int(CLOTHING_COAT_PROB*100)}%", font_size=20),
            Text(f"t-shirt\n{int(CLOTHING_TSHIRT_PROB*100)}%", font_size=20)
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
            Text("t-shirt", font_size=20),
            Text("coat", font_size=20)
        ).arrange(RIGHT, buff=1.5)
        bottom_labels.next_to(clothing_group, DOWN, buff=0.3)
        
        percentages = VGroup(
            Text(f"{int(CLOTHING_TSHIRT_PROB*100)}%", font_size=16),
            Text(f"{int(CLOTHING_COAT_PROB*100)}%", font_size=16)
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

"""
Add multiplication equation for forming each box and explain it in greater detail
"""

class ConditionalProbabilityDistributions(Scene):
    def construct(self):
        # Constants for probabilities
        WEATHER_RAIN_PROB = 0.25
        WEATHER_SUNNY_PROB = 0.75
        CLOTHING_TSHIRT_PROB = 0.75  # Changed to match image
        CLOTHING_COAT_PROB = 0.25    # Changed to match image
        
        # Initial distribution (left side)
        weather_height = 4
        weather_width = 1
        
        # Create the initial rectangle with its parts
        weather_group = VGroup(
            # Main container
            Rectangle(height=weather_height, width=weather_width, stroke_width=2),
            # Sunny part (bottom)
            Rectangle(height=weather_height*WEATHER_SUNNY_PROB, width=weather_width)
            .set_fill(color="#D4D0AB", opacity=1),
            # Raining part (top)
            Rectangle(height=weather_height*WEATHER_RAIN_PROB, width=weather_width)
            .set_fill(color="#4FB3BF", opacity=1),
        )
        
        # Position the parts
        weather_group[1].move_to(weather_group[0].get_bottom(), aligned_edge=DOWN)
        weather_group[2].move_to(weather_group[0].get_top(), aligned_edge=UP)
        
        # Weather labels
        weather_labels = VGroup(
            Text("raining\n25%", font_size=20, color=WHITE),
            Text("sunny\n75%", font_size=20, color=WHITE)
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
            Text("t-shirt", font_size=24, color=WHITE),
            Text("coat", font_size=24, color=WHITE),
            Text("75%", font_size=20, color=WHITE),
            Text("25%", font_size=20, color=WHITE),
        )
        
        # Position bottom labels
        bottom_labels[0].next_to(joint_square, DOWN, buff=0.3).shift(LEFT*1.5)
        bottom_labels[1].next_to(joint_square, DOWN, buff=0.3).shift(RIGHT*1.5)
        bottom_labels[2].next_to(bottom_labels[0], DOWN, buff=0.1)
        bottom_labels[3].next_to(bottom_labels[1], DOWN, buff=0.1)

        # Formula
        formula = MathTex(
            r"p(x,y) = p(x) \cdot p(y|x)",
            color=WHITE,
            font_size=36
        ).next_to(joint_square, DOWN, buff=2)

        # Animation sequence
        self.play(
            Create(weather_group),
            Write(weather_labels)
        )
        self.wait()
        
        self.play(
            Create(joint_square),
            Create(sections)
        )
        self.wait()

        self.play(Write(percentage_labels))
        self.wait()

        self.play(Write(bottom_labels))
        self.wait()

        self.play(Write(formula))
        self.wait(2)

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
            Rectangle(height=0.5, width=4 * 0.62)
            .set_fill(color="#D4D0AB", opacity=1),
            # Right section (38%)
            Rectangle(height=0.5, width=4 * 0.38)
            .set_fill(color="#D4D0AB", opacity=1),
        ).arrange(RIGHT, buff=0)
        
        bottom_group = VGroup(bottom_bar, bottom_sections)
        bottom_group.move_to(DOWN*3)

        # Bottom percentages
        bottom_labels = VGroup(
            Text("62%", font_size=24, color=WHITE).move_to(bottom_sections[0]),
            Text("38%", font_size=24, color=WHITE).move_to(bottom_sections[1])
        )

        # Upward arrow
        arrow = Arrow(
            bottom_bar.get_top(),
            ORIGIN + DOWN*0.5,
            buff=0.2,
            color=WHITE
        )

        # Square with new proportions
        square_size = 4
        main_square = Square(side_length=square_size, stroke_width=2)
        
        # Create sections with new proportions
        sections = VGroup(
            # Bottom left (sunny, left) - 56%
            Rectangle(height=square_size * 0.80, width=square_size * 0.62)
            .set_fill(color="#D4D0AB", opacity=1),
            # Bottom right (sunny, right) - 19%
            Rectangle(height=square_size * 0.50, width=square_size * 0.38)
            .set_fill(color="#D4D0AB", opacity=1),
            # Top left (rain, left) - 6%
            Rectangle(height=square_size * (1 - 0.80), width=square_size * 0.62)
            .set_fill(color="#4FB3BF", opacity=1),
            # Top right (rain, right) - 19%
            Rectangle(height=square_size * 0.50, width=square_size * 0.38)
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
            Text("56%", font_size=36, color=WHITE).move_to(sections[0]),
            Text("19%", font_size=36, color=WHITE).move_to(sections[1]),
            Text("6%", font_size=36, color=WHITE).move_to(sections[2]),
            Text("19%", font_size=36, color=WHITE).move_to(sections[3])
        )

        # Side labels for rain/sunny percentages
        side_labels = VGroup(
            Text("raining\n8%", font_size=24, color=WHITE).next_to(main_square, LEFT, buff=0.5),
            Text("sunny\n92%", font_size=24, color=WHITE).next_to(main_square, LEFT, buff=0.5).shift(DOWN*2),
            Text("raining\n50%", font_size=24, color=WHITE).next_to(main_square, RIGHT, buff=0.5),
            Text("sunny\n50%", font_size=24, color=WHITE).next_to(main_square, RIGHT, buff=0.5).shift(DOWN*2)
        )

        # Animation sequence for new visualization
        self.play(
            Create(bottom_bar),
            Create(bottom_sections),
            Write(bottom_labels)
        )
        self.wait()

        self.play(Create(arrow))
        self.wait()

        self.play(
            Create(main_square),
            Create(sections)
        )
        self.wait()

        self.play(Write(percentage_labels))
        self.wait()

        self.play(Write(side_labels))
        self.wait(2)

"""
Now I love to cook, and I have a few favorite recipes that I like to make.
Them being 

Pizza, Pasta, Salad, & Soup

And my sister loves to eat them all. But she would still like to know what I have cooked. 
But she loves to play games, so she tells me I can only tell the food I have cooked in binary code. 

"""
class KLDIntroTalk(Scene):
    def construct(self):
        pass


class KLDIntro(Scene):
   def construct(self):
        # Constants for consistent styling
        SYMBOL_COLOR = "#C19EE0"  # Light purple
        CODE_COLOR = "#98FB98"    # Light green
        
        # Create the binary string at top
        binary_string = Text("1 0 0 1 1 0...", color=CODE_COLOR)
        binary_string.to_edge(UP, buff=1)
        
        # Create the mapping diagram
        # Left side - symbols with food items
        symbols = VGroup(
            Text("Pizza", font_size=36),
            Text("Pasta", font_size=36), 
            Text("Salad", font_size=36),
            Text("Soup", font_size=36)
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
        encoded_string = Text("0 0 0 1 0 0 1 1", color=CODE_COLOR)
        codewords_text = Text("00 01 00 11", color=CODE_COLOR)
        source_text = Text("Pizza Pasta Pizza Soup", color=SYMBOL_COLOR)
        
        # Create boxes
        encoded_box = RoundedRectangle(
            height=encoded_string.height + 0.5,
            width=encoded_string.width + 1,
            corner_radius=0.2,
            color=CODE_COLOR
        )
        codewords_box = RoundedRectangle(
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
        
        # Create labels
        encoded_label = Text("encoded string", color=WHITE)
        codewords_label = Text("codewords", color=WHITE)
        source_label = Text("source symbols", color=WHITE)
        
        # Create groups and align them
        encoded_group = VGroup(encoded_box, encoded_string)
        codewords_group = VGroup(codewords_box, codewords_text)
        source_group = VGroup(source_box, source_text)
        
        # Move texts to their boxes
        encoded_string.move_to(encoded_box)
        codewords_text.move_to(codewords_box)
        source_text.move_to(source_box)
        
        # Arrange boxes vertically
        boxes_group = VGroup(encoded_group, codewords_group, source_group).arrange(DOWN, buff=0.5)
        
        # Align labels to the right of their respective boxes
        encoded_label.next_to(encoded_box, RIGHT, buff=0.5)
        codewords_label.next_to(codewords_box, RIGHT, buff=0.5)
        source_label.next_to(source_box, RIGHT, buff=0.5)
        
        # Create final groups for animation
        bottom_group = VGroup(
            VGroup(encoded_group, encoded_label),
            VGroup(codewords_group, codewords_label),
            VGroup(source_group, source_label)
        ).move_to(ORIGIN)
        
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