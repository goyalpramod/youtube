from manim import *

class TextKLD(Scene):
    def construct(self):
        text = Text("Kullback Leibler Divergence", font_size=72)
        self.play(Write(text), run_time=3)
        self.play(FadeOut(text))
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
            .set_fill(color=PURPLE_A, opacity=0.8),
        ).arrange(UP, buff=0)
        
        weather_group = VGroup(weather_rect, weather_parts)
        
        # Weather labels
        weather_title = Text("weather\nnext week", font_size=24)
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
            .set_fill(color=YELLOW_A, opacity=0.8),
            # Coat (top)
            Rectangle(height=4*CLOTHING_COAT_PROB, width=1)
            .set_fill(color=YELLOW_D, opacity=0.8),
        ).arrange(UP, buff=0)
        
        clothing_group = VGroup(clothing_rect, clothing_parts)
        
        # Clothing labels
        clothing_title = Text("clothing\ntoday", font_size=24)
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
            FadeOut(clothing_labels)
        )
        
        # Move to form square (align left edges)
        self.play(
            clothing_group.animate.next_to(weather_group.get_bottom(), UP*0.2, buff=0).align_to(weather_group, LEFT)  # Align left
        )
        
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
        
        self.play(
            Write(bottom_labels),
            Write(percentages)
        )
        
        # 5. Create and animate slider
        slider = Line(LEFT*2, RIGHT*2).next_to(percentages, DOWN, buff=1)
        dot = Dot().move_to(slider.point_from_proportion(CLOTHING_TSHIRT_PROB))
        
        self.play(
            Create(slider),
            Create(dot)
        )
        
        # Animate slider to show independence
        self.play(
            dot.animate.shift(RIGHT),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait()
        
        # Final pause
        self.wait(2)