# from manim import *
# import numpy as np

# class IntroductionScene(Scene):
#     def construct(self):
#         title = Text("Linear Algebra: A Visual Introduction", font_size=48)
#         subtitle = Text("Mathematics for Machine Learning", font_size=36)
#         subtitle.next_to(title, DOWN, buff=0.5)
        
#         self.play(Write(title))
#         self.play(FadeIn(subtitle))
#         self.wait(2)
#         self.play(FadeOut(title), FadeOut(subtitle))
        
#         # Outline of topics
#         topic_list = BulletedList(
#             "Vectors and Vector Operations",
#             "Matrices and Linear Transformations",
#             "Systems of Linear Equations",
#             "Vector Space and Span",
#             "Basis and Rank",
#             "Elementary Transformations and Row Echelon Form",
#             "Image and Kernel (Null Space)",
#             font_size=36
#         )
        
#         self.play(Write(topic_list), run_time=3)
#         self.wait(2)
#         self.play(FadeOut(topic_list))
        
#         # Transition to next scene
#         next_scene = Text("Let's start with Vectors", font_size=48)
#         self.play(Write(next_scene))
#         self.wait(1)
#         self.play(FadeOut(next_scene))


# class VectorsScene(Scene):
#     def construct(self):
#         title = Title("1. Vectors: The Building Blocks")
#         self.play(Write(title))
        
#         # Define coordinate system
#         axes = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             axis_config={"include_tip": True, "numbers_to_include": range(-4, 5, 2)}
#         )
#         axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
#         self.play(Create(axes), Write(axes_labels))
        
#         # Definition of a vector
#         vector_def = MathTex(r"\text{A vector } \vec{v} \text{ is an element of a vector space}")
#         vector_def.next_to(title, DOWN, buff=0.5)
        
#         vector_example = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}")
#         vector_example.next_to(vector_def, DOWN, buff=0.5)
        
#         self.play(Write(vector_def))
#         self.play(Write(vector_example))
#         self.wait(1)
        
#         # Display a vector
#         vector_v = Vector([3, 2], color=YELLOW)
#         vector_v_label = MathTex(r"\vec{v}", color=YELLOW)
#         vector_v_label.next_to(vector_v.get_end(), UP+RIGHT, buff=0.1)
        
#         self.play(
#             GrowArrow(vector_v),
#             Write(vector_v_label)
#         )
#         self.wait(1)
        
#         # Vector operations
#         self.play(
#             FadeOut(vector_def),
#             FadeOut(vector_example),
#         )
        
#         operations_title = Text("Vector Operations", font_size=36)
#         operations_title.next_to(title, DOWN, buff=0.5)
#         self.play(Write(operations_title))
        
#         # Addition of vectors
#         vector_w = Vector([1, 3], color=BLUE)
#         vector_w_label = MathTex(r"\vec{w}", color=BLUE)
#         vector_w_label.next_to(vector_w.get_end(), RIGHT, buff=0.1)
        
#         self.play(
#             GrowArrow(vector_w),
#             Write(vector_w_label)
#         )
        
#         addition_eq = MathTex(r"\vec{v} + \vec{w} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} + \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \end{bmatrix}")
#         addition_eq.to_edge(UP)
        
#         vector_sum = Vector([4, 5], color=GREEN)
#         vector_sum_label = MathTex(r"\vec{v} + \vec{w}", color=GREEN)
#         vector_sum_label.next_to(vector_sum.get_end(), RIGHT, buff=0.1)
        
#         # Show parallelogram law
#         parallelogram = Polygon(
#             [0, 0, 0],
#             [3, 2, 0],
#             [4, 5, 0],
#             [1, 3, 0],
#             stroke_opacity=0.5,
#             fill_opacity=0.2,
#             fill_color=GREEN
#         )
        
#         self.play(Write(addition_eq))
#         self.play(Create(parallelogram))
#         self.play(GrowArrow(vector_sum), Write(vector_sum_label))
#         self.wait(2)
        
#         # Scalar multiplication
#         self.play(
#             FadeOut(vector_w),
#             FadeOut(vector_w_label),
#             FadeOut(vector_sum),
#             FadeOut(vector_sum_label),
#             FadeOut(parallelogram),
#             FadeOut(addition_eq),
#         )
        
#         scalar_eq = MathTex(r"2 \cdot \vec{v} = 2 \cdot \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \end{bmatrix}")
#         scalar_eq.to_edge(UP)
        
#         vector_scaled = Vector([6, 4], color=RED)
#         vector_scaled_label = MathTex(r"2\vec{v}", color=RED)
#         vector_scaled_label.next_to(vector_scaled.get_end(), RIGHT, buff=0.1)
        
#         self.play(Write(scalar_eq))
#         self.play(GrowArrow(vector_scaled), Write(vector_scaled_label))
#         self.wait(2)
        
#         # Vector properties summary
#         properties = BulletedList(
#             "Vectors have magnitude and direction",
#             "Vector addition: head-to-tail or parallelogram method",
#             "Scalar multiplication: scales length, preserves/flips direction",
#             font_size=28
#         )
#         properties.to_edge(DOWN, buff=0.5)
        
#         self.play(
#             FadeOut(scalar_eq),
#             FadeOut(operations_title),
#             Write(properties)
#         )
#         self.wait(3)
        
#         # Transition
#         self.play(
#             FadeOut(vector_v),
#             FadeOut(vector_v_label),
#             FadeOut(vector_scaled),
#             FadeOut(vector_scaled_label),
#             FadeOut(properties),
#             FadeOut(title),
#             FadeOut(axes),
#             FadeOut(axes_labels)
#         )


# class MatricesScene(Scene):
#     def construct(self):
#         title = Title("2. Matrices: Arrays of Numbers with Purpose")
#         self.play(Write(title))
        
#         # Define a matrix
#         matrix_def = MathTex(r"\text{A matrix is a rectangular array of numbers}")
#         matrix_def.next_to(title, DOWN, buff=0.5)
        
#         matrix_A = MathTex(r"A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}")
#         matrix_A.next_to(matrix_def, DOWN, buff=0.5)
        
#         matrix_dim = MathTex(r"\text{This is a } 2 \times 3 \text{ matrix (2 rows, 3 columns)}")
#         matrix_dim.next_to(matrix_A, DOWN, buff=0.5)
        
#         self.play(Write(matrix_def))
#         self.play(Write(matrix_A))
#         self.play(Write(matrix_dim))
#         self.wait(2)
        
#         # Matrices as linear transformations
#         self.play(
#             FadeOut(matrix_def),
#             FadeOut(matrix_A),
#             FadeOut(matrix_dim)
#         )
        
#         transform_title = Text("Matrices as Linear Transformations", font_size=36)
#         transform_title.next_to(title, DOWN, buff=0.5)
#         self.play(Write(transform_title))
        
#         # Create a coordinate system
#         axes = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             axis_config={"include_tip": True}
#         )
#         grid = NumberPlane(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             background_line_style={
#                 "stroke_opacity": 0.4
#             }
#         )
        
#         self.play(Create(grid), Create(axes))
        
#         # Create basis vectors
#         basis_i = Vector([1, 0], color=RED)
#         basis_j = Vector([0, 1], color=BLUE)
        
#         basis_i_label = MathTex(r"\hat{\imath}", color=RED)
#         basis_j_label = MathTex(r"\hat{\jmath}", color=BLUE)
        
#         basis_i_label.next_to(basis_i.get_end(), DOWN, buff=0.1)
#         basis_j_label.next_to(basis_j.get_end(), LEFT, buff=0.1)
        
#         self.play(
#             GrowArrow(basis_i),
#             GrowArrow(basis_j),
#             Write(basis_i_label),
#             Write(basis_j_label)
#         )
#         self.wait(1)
        
#         # Define a transformation matrix
#         matrix_T = MathTex(r"T = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}")
#         matrix_T.to_edge(UP)
#         self.play(Write(matrix_T))
        
#         # Show the transformation
#         transformed_i = Vector([2, 0], color=RED_E)
#         transformed_j = Vector([1, 1], color=BLUE_E)
        
#         transformed_i_label = MathTex(r"T\hat{\imath}", color=RED_E)
#         transformed_j_label = MathTex(r"T\hat{\jmath}", color=BLUE_E)
        
#         transformed_i_label.next_to(transformed_i.get_end(), DOWN, buff=0.1)
#         transformed_j_label.next_to(transformed_j.get_end(), LEFT, buff=0.1)
        
#         self.play(
#             Transform(basis_i, transformed_i),
#             Transform(basis_j, transformed_j),
#             Transform(basis_i_label, transformed_i_label),
#             Transform(basis_j_label, transformed_j_label)
#         )
        
#         # Show the grid transformation
#         transformed_grid = grid.copy()
#         transformed_grid.apply_matrix([[2, 1], [0, 1]])
#         transformed_grid.set_color(YELLOW_E)
        
#         self.play(
#             Transform(grid, transformed_grid),
#             run_time=2
#         )
#         self.wait(2)
        
#         # Matrix operations
#         self.play(
#             FadeOut(grid),
#             FadeOut(axes),
#             FadeOut(basis_i),
#             FadeOut(basis_j),
#             FadeOut(basis_i_label),
#             FadeOut(basis_j_label),
#             FadeOut(matrix_T),
#             FadeOut(transform_title)
#         )
        
#         operations_title = Text("Matrix Operations", font_size=36)
#         operations_title.next_to(title, DOWN, buff=0.5)
#         self.play(Write(operations_title))
        
#         # Matrix addition
#         matrix_A = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
#         matrix_B = MathTex(r"B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")
        
#         matrix_A.shift(UP + LEFT * 3)
#         matrix_B.shift(UP + RIGHT * 3)
        
#         self.play(Write(matrix_A), Write(matrix_B))
        
#         plus_sign = MathTex(r"+")
#         plus_sign.next_to(matrix_A, RIGHT)
#         equals_sign = MathTex(r"=")
#         equals_sign.next_to(matrix_B, RIGHT)
        
#         matrix_sum = MathTex(r"\begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}")
#         matrix_sum.next_to(equals_sign, RIGHT)
        
#         self.play(Write(plus_sign), Write(equals_sign))
#         self.play(Write(matrix_sum))
#         self.wait(1)
        
#         # Matrix multiplication
#         self.play(
#             FadeOut(matrix_A),
#             FadeOut(plus_sign),
#             FadeOut(matrix_B),
#             FadeOut(equals_sign),
#             FadeOut(matrix_sum)
#         )
        
#         matrix_C = MathTex(r"C = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
#         matrix_D = MathTex(r"D = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")
        
#         matrix_C.shift(UP + LEFT * 3)
#         matrix_D.shift(UP + RIGHT * 3)
        
#         self.play(Write(matrix_C), Write(matrix_D))
        
#         times_sign = MathTex(r"\times")
#         times_sign.next_to(matrix_C, RIGHT)
#         equals_sign = MathTex(r"=")
#         equals_sign.next_to(matrix_D, RIGHT)
        
#         matrix_product = MathTex(r"\begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}")
#         matrix_product.next_to(equals_sign, RIGHT)
        
#         self.play(Write(times_sign), Write(equals_sign))
        
#         # Show the multiplication process
#         calc1 = MathTex(r"1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19")
#         calc2 = MathTex(r"1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22")
#         calc3 = MathTex(r"3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43")
#         calc4 = MathTex(r"3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50")
        
#         calcs = VGroup(calc1, calc2, calc3, calc4).arrange(DOWN, buff=0.3)
#         calcs.to_edge(DOWN, buff=1)
        
#         self.play(Write(calcs), run_time=3)
#         self.wait(1)
#         self.play(Write(matrix_product))
#         self.wait(1)
#         self.play(FadeOut(calcs))
        
#         # Properties summary
#         properties = BulletedList(
#             "Matrices represent linear transformations",
#             "Matrix multiplication is composition of transformations",
#             "Matrix multiplication is NOT commutative (A×B ≠ B×A generally)",
#             "Identity matrix I is the 'do nothing' transformation",
#             font_size=28
#         )
#         properties.to_edge(DOWN, buff=0.5)
        
#         self.play(
#             FadeOut(matrix_C),
#             FadeOut(times_sign),
#             FadeOut(matrix_D),
#             FadeOut(equals_sign),
#             FadeOut(matrix_product),
#             Write(properties)
#         )
#         self.wait(3)
        
#         # Transition
#         self.play(
#             FadeOut(properties),
#             FadeOut(operations_title),
#             FadeOut(title)
#         )


# class LinearEquationsScene(Scene):
#     def construct(self):
#         title = Title("3. Systems of Linear Equations")
#         self.play(Write(title))
        
#         # Define a system of linear equations
#         system = MathTex(
#             r"\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}"
#         )
#         system.next_to(title, DOWN, buff=0.5)
        
#         self.play(Write(system))
#         self.wait(1)
        
#         # Matrix form
#         matrix_form_title = Text("Matrix Form:", font_size=36)
#         matrix_form_title.next_to(system, DOWN, buff=0.5)
        
#         matrix_form = MathTex(
#             r"\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}"
#         )
#         matrix_form.next_to(matrix_form_title, DOWN, buff=0.5)
        
#         self.play(Write(matrix_form_title))
#         self.play(Write(matrix_form))
#         self.wait(1)
        
#         # Simplified notation
#         simplified = MathTex(r"A\vec{x} = \vec{b}")
#         simplified.next_to(matrix_form, DOWN, buff=0.5)
        
#         self.play(Write(simplified))
#         self.wait(2)
        
#         # Geometrical interpretation
#         self.play(
#             FadeOut(system),
#             FadeOut(matrix_form_title),
#             FadeOut(matrix_form),
#             FadeOut(simplified)
#         )
        
#         geometric_title = Text("Geometric Interpretation", font_size=36)
#         geometric_title.next_to(title, DOWN, buff=0.5)
#         self.play(Write(geometric_title))
        
#         # Create coordinate system
#         axes = Axes(
#             x_range=[-1, 6, 1],
#             y_range=[-1, 6, 1],
#             axis_config={"include_tip": True, "numbers_to_include": range(0, 6, 1)}
#         )
#         axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
#         self.play(Create(axes), Write(axes_labels))
        
#         # Plot the lines
#         line1 = axes.plot(lambda x: 5 - 2*x, color=RED)
#         line2 = axes.plot(lambda x: x - 1, color=BLUE)
        
#         line1_eq = MathTex(r"2x + y = 5", color=RED)
#         line2_eq = MathTex(r"x - y = 1", color=BLUE)
        
#         line1_eq.to_edge(UP, buff=1)
#         line2_eq.next_to(line1_eq, DOWN, buff=0.5)
        
#         self.play(Create(line1), Write(line1_eq))
#         self.play(Create(line2), Write(line2_eq))
        
#         # Highlight the solution
#         solution_point = Dot(axes.c2p(2, 1), color=YELLOW)
#         solution_coords = MathTex(r"(2, 1)", color=YELLOW)
#         solution_coords.next_to(solution_point, UP+RIGHT, buff=0.1)
        
#         self.play(FadeIn(solution_point, scale=0.5), Write(solution_coords))
#         self.wait(2)
        
#         # Solution explanation
#         solution_check = MathTex(
#             r"\begin{cases} 2(2) + 1 = 5 \checkmark \\ 2 - 1 = 1 \checkmark \end{cases}"
#         )
#         solution_check.to_edge(RIGHT, buff=1)
        
#         self.play(Write(solution_check))
#         self.wait(2)
        
#         # Summary
#         self.play(
#             FadeOut(axes),
#             FadeOut(axes_labels),
#             FadeOut(line1),
#             FadeOut(line2),
#             FadeOut(line1_eq),
#             FadeOut(line2_eq),
#             FadeOut(solution_point),
#             FadeOut(solution_coords),
#             FadeOut(solution_check),
#             FadeOut(geometric_title)
#         )
        
#         summary = BulletedList(
#             "Systems of linear equations can be written as A\\vec{x} = \\vec{b}",
#             "Solutions are where all equations are satisfied simultaneously",
#             "Can have: unique solution, no solution, or infinitely many solutions",
#             "Matrix methods provide powerful tools to find solutions",
#             font_size=28
#         )
#         summary.next_to(title, DOWN, buff=0.5)
        
#         self.play(Write(summary))
#         self.wait(3)
        
#         # Transition
#         self.play(
#             FadeOut(summary),
#             FadeOut(title)
#         )


# class VectorSpaceScene(Scene):
#     def construct(self):
#         title = Title("4. Vector Spaces and Span")
#         self.play(Write(title))
        
#         # Define vector space
#         vector_space_def = Text("A vector space is a set of vectors with operations:", font_size=36)
#         vector_space_def.next_to(title, DOWN, buff=0.5)
        
#         properties = BulletedList(
#             "Closure under addition: $\\vec{u} + \\vec{v}$ is in the space",
#             "Closure under scalar multiplication: $c\\vec{v}$ is in the space",
#             "Satisfies certain algebraic properties (associativity, etc.)",
#             font_size=28
#         )
#         properties.next_to(vector_space_def, DOWN, buff=0.5)
        
#         self.play(Write(vector_space_def))
#         self.play(Write(properties))
#         self.wait(2)
        
#         # Span concept
#         self.play(
#             FadeOut(vector_space_def),
#             FadeOut(properties)
#         )
        
#         span_title = Text("The Span of Vectors", font_size=36)
#         span_title.next_to(title, DOWN, buff=0.5)
        
#         span_def = MathTex(r"\text{span}(\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n) = \{c_1\vec{v}_1 + c_2\vec{v}_2 + \ldots + c_n\vec{v}_n \mid c_i \in \mathbb{R}\}")
#         span_def.scale(0.8)
#         span_def.next_to(span_title, DOWN, buff=0.5)
        
#         span_explain = Text("All possible linear combinations of the vectors", font_size=28)
#         span_explain.next_to(span_def, DOWN, buff=0.5)
        
#         self.play(Write(span_title))
#         self.play(Write(span_def))
#         self.play(Write(span_explain))
#         self.wait(2)
        
#         # Visualize span in R2
#         self.play(
#             FadeOut(span_def),
#             FadeOut(span_explain)
#         )
        
#         # Create coordinate system
#         axes = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             axis_config={"include_tip": True}
#         )
#         grid = NumberPlane(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             background_line_style={
#                 "stroke_opacity": 0.4
#             }
#         )
        
#         self.play(Create(grid), Create(axes))
        
#         # Case 1: Span of one vector
#         v1 = Vector([2, 1], color=RED)
#         v1_label = MathTex(r"\vec{v}_1", color=RED)
#         v1_label.next_to(v1.get_end(), UP, buff=0.1)
        
#         self.play(GrowArrow(v1), Write(v1_label))
        
#         span1_title = Text("Span of one vector:", font_size=28)
#         span1_title.to_edge(UP, buff=1)
        
#         span1_line = DashedLine(
#             start=axes.c2p(-5, -2.5),
#             end=axes.c2p(5, 2.5),
#             color=RED_E,
#             stroke_opacity=0.6
#         )
        
#         self.play(Write(span1_title))
#         self.play(Create(span1_line))
#         self.wait(1)
        
#         span1_explain = Text("A line through the origin", font_size=24)
#         span1_explain.next_to(span1_title, DOWN, buff=0.3)
        
#         self.play(Write(span1_explain))
#         self.wait(2)
        
#         # Case 2: Span of two linearly independent vectors
#         self.play(
#             FadeOut(span1_title),
#             FadeOut(span1_explain),
#             FadeOut(span1_line)
#         )
        
#         v2 = Vector([0, 2], color=BLUE)
#         v2_label = MathTex(r"\vec{v}_2", color=BLUE)
#         v2_label.next_to(v2.get_end(), RIGHT, buff=0.1)
        
#         self.play(GrowArrow(v2), Write(v2_label))
        
#         span2_title = Text("Span of two linearly independent vectors:", font_size=28)
#         span2_title.to_edge(UP, buff=1)
        
#         # Visualize the span as a plane
#         span2_plane = Rectangle(
#             width=10,
#             height=10,
#             stroke_opacity=0,
#             fill_opacity=0.2,
#             fill_color=YELLOW
#         )
#         span2_plane.move_to(axes.c2p(0, 0))
        
#         self.play(Write(span2_title))
#         self.play(FadeIn(span2_plane))
        
#         span2_explain = Text("The entire 2D plane (R²)", font_size=24)
#         span2_explain.next_to(span2_title, DOWN, buff=0.3)
        
#         self.play(Write(span2_explain))
#         self.wait(2)
        
#         # Case 3: Span of two linearly dependent vectors
#         self.play(
#             FadeOut(span2_title),
#             FadeOut(span2_explain),
#             FadeOut(span2_plane),
#             FadeOut(v2),
#             FadeOut(v2_label)
#         )
        
#         v3 = Vector([4, 2], color=GREEN)
#         v3_label = MathTex(r"\vec{v}_3 = 2\vec{v}_1", color=GREEN)
#         v3_label.next_to(v3.get_end(), UP, buff=0.1)
        
#         self.play(GrowArrow(v3), Write(v3_label))
        
#         span3_title = Text("Span of two linearly dependent vectors:", font_size=28)
#         span3_title.to_edge(UP, buff=1)
        
#         span3_line = DashedLine(
#             start=axes.c2p(-5, -2.5),
#             end=axes.c2p(5, 2.5),
#             color=YELLOW_E,
#             stroke_opacity=0.6
#         )
        
#         self.play(Write(span3_title))
#         self.play(Create(span3_line))
        
#         span3_explain = Text("Still just a line through the origin", font_size=24)
#         span3_explain.next_to(span3_title, DOWN, buff=0.3)
        
#         self.play(Write(span3_explain))
#         self.wait(2)
        
#         # Subspace concept
#         self.play(
#             FadeOut(span3_title),
#             FadeOut(span3_explain),
#             FadeOut(span3_line),
#             FadeOut(v1),
#             FadeOut(v1_label),
#             FadeOut(v3),
#             FadeOut(v3_label),
#             FadeOut(grid),
#             FadeOut(axes)
#         )
        
#         subspace_title = Text("Subspaces and Abelian Groups", font_size=36)
#         subspace_title.next_to(title, DOWN, buff=0.5)
        
#         self.play(Write(subspace_title))
        
#         subspace_def = BulletedList(
#             "A subspace is a subset of a vector space that is itself a vector space",
#             "Must contain the zero vector",
#             "Closed under addition and scalar multiplication",
#             "An Abelian group is a group where operations are commutative (a+b = b+a)",
#             "Vector spaces form Abelian groups under addition",
#             font_size=28
#         )
#         subspace_def.next_to(subspace_title, DOWN, buff=0.5)
        
#         self.play(Write(subspace_def))
#         self.wait(3)
        
#         # Transition
#         self.play(
#             FadeOut(subspace_title),
#             FadeOut(subspace_def),
#             FadeOut(title)
#         )


# class BasisRankScene(Scene):
#     def construct(self):
#         title = Title("5. Basis and Rank")
#         self.play(Write(title))
        
#         # Define basis
#         basis_title = Text("Basis of a Vector Space", font_size=36)
#         basis_title.next_to(title, DOWN, buff=0.5)
        
#         basis_def = BulletedList(
#             "A basis is a set of linearly independent vectors that span the space",
#             "Every vector in the space can be written as a unique linear combination of basis vectors",
#             "The number of vectors in a basis is the dimension of the space",
#             font_size=28
#         )
#         basis_def.next_to(basis_title, DOWN, buff=0.5)
        
#         self.play(Write(basis_title))
#         self.play(Write(basis_def))
#         self.wait(2)
        
#         # Standard basis example
#         self.play(
#             FadeOut(basis_def)
#         )
        
#         standard_title = Text("Standard Basis in R²", font_size=32)
#         standard_title.next_to(basis_title, DOWN, buff=0.5)
        
#         # Create coordinate system
#         axes = Axes(
#             x_range=[-3, 3, 1],
#             y_range=[-3, 3, 1],
#             axis_config={"include_tip": True}
#         )
#         grid = NumberPlane(
#             x_range=[-3, 3, 1],
#             y_range=[-3, 3, 1],
#             background_line_style={
#                 "stroke_opacity": 0.4
#             }
#         )
        
#         self.play(Create(grid), Create(axes))
#         self.play(Write(standard_title))
        
#         # Standard basis vectors
#         e1 = Vector([1, 0], color=RED)
#         e2 = Vector([0, 1], color=BLUE)
        
#         e1_label = MathTex(r"\hat{e}_1", color=RED)
#         e2_label = MathTex(r"\hat{e}_2", color=BLUE)
        
#         e1_label.next_to(e1.get_end(), DOWN, buff=0.1)
#         e2_label.next_to(e2.get_end(), LEFT, buff=0.1)
        
#         self.play(
#             GrowArrow(e1),
#             GrowArrow(e2),
#             Write(e1_label),
#             Write(e2_label)
#         )
        
#         # Show expressing a vector in the standard basis
#         v = Vector([2, 1], color=GREEN)
#         v_label = MathTex(r"\vec{v}", color=GREEN)
#         v_label.next_to(v.get_end(), RIGHT, buff=0.1)
        
#         self.play(GrowArrow(v), Write(v_label))
        
#         v_components = MathTex(r"\vec{v} = 2\hat{e}_1 + 1\hat{e}_2")
#         v_components.to_edge(UP, buff=1)
        
#         self.play(Write(v_components))
#         self.wait(2)
        
#         # Define rank
#         self.play(
#             FadeOut(grid),
#             FadeOut(axes),
#             FadeOut(e1),
#             FadeOut(e2),
#             FadeOut(e1_label),
#             FadeOut(e2_label),
#             FadeOut(v),
#             FadeOut(v_label),
#             FadeOut(v_components),
#             FadeOut(standard_title),
#             FadeOut(basis_title)
#         )
        
#         rank_title = Text("Rank of a Matrix", font_size=36)
#         rank_title.next_to(title, DOWN, buff=0.5)
        
#         rank_def = BulletedList(
#             "The rank of a matrix is the dimension of its column space (or row space)",
#             "It's the number of linearly independent columns (or rows)",
#             "Rank tells us how much information the matrix contains",
#             "Rank is preserved by elementary row operations",
#             font_size=28
#         )
#         rank_def.next_to(rank_title, DOWN, buff=0.5)
        
#         self.play(Write(rank_title))
#         self.play(Write(rank_def))
#         self.wait(2)
        
#         # Rank examples
#         self.play(
#             FadeOut(rank_def)
#         )
        
#         examples_title = Text("Rank Examples", font_size=32)
#         examples_title.next_to(rank_title, DOWN, buff=0.5)
        
#         # Full rank example
#         matrix_A = MathTex(r"A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}")
#         rank_A = MathTex(r"\text{rank}(A) = 2")
        
#         matrix_A.next_to(examples_title, DOWN, buff=0.5)
#         rank_A.next_to(matrix_A, RIGHT, buff=1)
        
#         self.play(Write(examples_title))
#         self.play(Write(matrix_A), Write(rank_A))
        
#         # Deficient rank example
#         matrix_B = MathTex(r"B = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}")
#         rank_B = MathTex(r"\text{rank}(B) = 1")
        
#         matrix_B.next_to(matrix_A, DOWN, buff=0.5)
#         rank_B.next_to(matrix_B, RIGHT, buff=1)
        
#         self.play(Write(matrix_B), Write(rank_B))
        
#         # Zero matrix
#         matrix_C = MathTex(r"C = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}")
#         rank_C = MathTex(r"\text{rank}(C) = 0")
        
#         matrix_C.next_to(matrix_B, DOWN, buff=0.5)
#         rank_C.next_to(matrix_C, RIGHT, buff=1)
        
#         self.play(Write(matrix_C), Write(rank_C))
#         self.wait(2)
        
#         # Transition
#         self.play(
#             FadeOut(examples_title),
#             FadeOut(matrix_A),
#             FadeOut(rank_A),
#             FadeOut(matrix_B),
#             FadeOut(rank_B),
#             FadeOut(matrix_C),
#             FadeOut(rank_C),
#             FadeOut(rank_title),
#             FadeOut(title)
#         )


# class ElementaryTransformationsScene(Scene):
#     def construct(self):
#         title = Title("6. Elementary Row Operations and Row Echelon Form")
#         self.play(Write(title))
        
#         # Elementary row operations
#         row_ops_title = Text("Elementary Row Operations", font_size=36)
#         row_ops_title.next_to(title, DOWN, buff=0.5)
        
#         row_ops = BulletedList(
#             "Swap two rows: $R_i \\leftrightarrow R_j$",
#             "Multiply a row by a non-zero scalar: $R_i \\rightarrow cR_i$",
#             "Add a multiple of one row to another: $R_i \\rightarrow R_i + cR_j$",
#             font_size=28
#         )
#         row_ops.next_to(row_ops_title, DOWN, buff=0.5)
        
#         self.play(Write(row_ops_title))
#         self.play(Write(row_ops))
#         self.wait(2)
        
#         # Why we use row operations
#         why_title = Text("Why Use Row Operations?", font_size=32)
#         why_title.next_to(row_ops, DOWN, buff=0.5)
        
#         why_points = BulletedList(
#             "Simplify systems of linear equations",
#             "Calculate determinants and inverses",
#             "Find rank and basis",
#             "Determine if vectors are linearly independent",
#             font_size=28
#         )
#         why_points.next_to(why_title, DOWN, buff=0.3)
        
#         self.play(Write(why_title))
#         self.play(Write(why_points))
#         self.wait(2)
        
#         # Row echelon form
#         self.play(
#             FadeOut(row_ops_title),
#             FadeOut(row_ops),
#             FadeOut(why_title),
#             FadeOut(why_points)
#         )
        
#         ref_title = Text("Row Echelon Form (REF)", font_size=36)
#         ref_title.next_to(title, DOWN, buff=0.5)
        
#         ref_properties = BulletedList(
#             "All zero rows are at the bottom",
#             "Leading coefficient of each non-zero row is to the right of the leading coefficient in the row above",
#             "All entries in a column below a leading coefficient are zero",
#             font_size=28
#         )
#         ref_properties.next_to(ref_title, DOWN, buff=0.5)
        
#         self.play(Write(ref_title))
#         self.play(Write(ref_properties))
#         self.wait(2)
        
#         # Example of row reduction
#         self.play(
#             FadeOut(ref_properties)
#         )
        
#         example_title = Text("Example: Row Reduction to REF", font_size=32)
#         example_title.next_to(ref_title, DOWN, buff=0.5)
        
#         # Starting matrix
#         matrix_start = MathTex(r"A = \begin{bmatrix} 1 & 3 & 1 \\ 2 & 7 & 3 \\ 1 & 5 & 3 \end{bmatrix}")
#         matrix_start.next_to(example_title, DOWN, buff=0.5)
        
#         self.play(Write(example_title))
#         self.play(Write(matrix_start))
#         self.wait(1)
        
#         # Step 1
#         step1 = Text("Step 1: Eliminate entries below pivot in first column", font_size=24)
#         step1.next_to(matrix_start, DOWN, buff=0.5)
        
#         matrix_step1 = MathTex(r"A_1 = \begin{bmatrix} 1 & 3 & 1 \\ 0 & 1 & 1 \\ 0 & 2 & 2 \end{bmatrix}")
#         matrix_step1.next_to(step1, DOWN, buff=0.5)
        
#         explanation1 = MathTex(r"R_2 \rightarrow R_2 - 2R_1, \quad R_3 \rightarrow R_3 - R_1")
#         explanation1.next_to(matrix_step1, DOWN, buff=0.3)
        
#         self.play(Write(step1))
#         self.play(Write(matrix_step1))
#         self.play(Write(explanation1))
#         self.wait(1)
        
#         # Step 2
#         step2 = Text("Step 2: Eliminate entries below pivot in second column", font_size=24)
#         step2.next_to(explanation1, DOWN, buff=0.5)
        
#         matrix_step2 = MathTex(r"A_2 = \begin{bmatrix} 1 & 3 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}")
#         matrix_step2.next_to(step2, DOWN, buff=0.5)
        
#         explanation2 = MathTex(r"R_3 \rightarrow R_3 - 2R_2")
#         explanation2.next_to(matrix_step2, DOWN, buff=0.3)
        
#         self.play(Write(step2))
#         self.play(Write(matrix_step2))
#         self.play(Write(explanation2))
#         self.wait(1)
        
#         # Final REF form
#         conclusion = Text("The matrix is now in Row Echelon Form!", font_size=28)
#         conclusion.next_to(explanation2, DOWN, buff=0.5)
        
#         self.play(Write(conclusion))
#         self.wait(2)
        
#         # Reduced Row Echelon Form (RREF)
#         self.play(
#             FadeOut(matrix_start),
#             FadeOut(step1),
#             FadeOut(matrix_step1),
#             FadeOut(explanation1),
#             FadeOut(step2),
#             FadeOut(matrix_step2),
#             FadeOut(explanation2),
#             FadeOut(conclusion),
#             FadeOut(example_title),
#             FadeOut(ref_title)
#         )
        
#         rref_title = Text("Reduced Row Echelon Form (RREF)", font_size=36)
#         rref_title.next_to(title, DOWN, buff=0.5)
        
#         rref_properties = BulletedList(
#             "All properties of REF",
#             "Leading coefficient of each non-zero row is 1",
#             "Each leading 1 is the only non-zero entry in its column",
#             font_size=28
#         )
#         rref_properties.next_to(rref_title, DOWN, buff=0.5)
        
#         self.play(Write(rref_title))
#         self.play(Write(rref_properties))
#         self.wait(2)
        
#         # RREF example
#         self.play(
#             FadeOut(rref_properties)
#         )
        
#         rref_example_title = Text("Example: Converting REF to RREF", font_size=32)
#         rref_example_title.next_to(rref_title, DOWN, buff=0.5)
        
#         matrix_ref = MathTex(r"A_{\text{REF}} = \begin{bmatrix} 1 & 3 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}")
#         matrix_ref.next_to(rref_example_title, DOWN, buff=0.5)
        
#         self.play(Write(rref_example_title))
#         self.play(Write(matrix_ref))
#         self.wait(1)
        
#         # Step 1 for RREF
#         step1 = Text("Step 1: Make leading entries 1 (already done)", font_size=24)
#         step1.next_to(matrix_ref, DOWN, buff=0.5)
        
#         self.play(Write(step1))
#         self.wait(1)
        
#         # Step 2 for RREF
#         step2 = Text("Step 2: Eliminate entries above pivots", font_size=24)
#         step2.next_to(step1, DOWN, buff=0.5)
        
#         matrix_rref = MathTex(r"A_{\text{RREF}} = \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}")
#         matrix_rref.next_to(step2, DOWN, buff=0.5)
        
#         explanation_rref = MathTex(r"R_1 \rightarrow R_1 - 3R_2")
#         explanation_rref.next_to(matrix_rref, DOWN, buff=0.3)
        
#         self.play(Write(step2))
#         self.play(Write(matrix_rref))
#         self.play(Write(explanation_rref))
#         self.wait(2)
        
#         # Transition
#         self.play(
#             FadeOut(matrix_ref),
#             FadeOut(step1),
#             FadeOut(step2),
#             FadeOut(matrix_rref),
#             FadeOut(explanation_rref),
#             FadeOut(rref_example_title),
#             FadeOut(rref_title),
#             FadeOut(title)
#         )


# class ImageKernelScene(Scene):
#     def construct(self):
#         title = Title("7. Image and Kernel")
#         self.play(Write(title))
        
#         # Define image
#         image_title = Text("Image (Range) of a Matrix", font_size=36)
#         image_title.next_to(title, DOWN, buff=0.5)
        
#         image_def = MathTex(r"\text{Im}(A) = \{A\vec{x} \mid \vec{x} \in \mathbb{R}^n\}")
#         image_def.next_to(image_title, DOWN, buff=0.5)
        
#         image_explain = Text("The set of all possible outputs of the transformation", font_size=28)
#         image_explain.next_to(image_def, DOWN, buff=0.3)
        
#         self.play(Write(image_title))
#         self.play(Write(image_def))
#         self.play(Write(image_explain))
#         self.wait(2)
        
#         # Define kernel
#         self.play(
#             FadeOut(image_def),
#             FadeOut(image_explain)
#         )
        
#         kernel_title = Text("Kernel (Null Space) of a Matrix", font_size=36)
#         kernel_title.next_to(image_title, DOWN, buff=0.5)
        
#         kernel_def = MathTex(r"\text{Ker}(A) = \{\vec{x} \mid A\vec{x} = \vec{0}\}")
#         kernel_def.next_to(kernel_title, DOWN, buff=0.5)
        
#         kernel_explain = Text("The set of all vectors that the transformation maps to zero", font_size=28)
#         kernel_explain.next_to(kernel_def, DOWN, buff=0.3)
        
#         self.play(Write(kernel_title))
#         self.play(Write(kernel_def))
#         self.play(Write(kernel_explain))
#         self.wait(2)
        
#         # Visualize with an example
#         self.play(
#             FadeOut(image_title),
#             FadeOut(kernel_title),
#             FadeOut(kernel_def),
#             FadeOut(kernel_explain)
#         )
        
#         example_title = Text("Visual Example: Projection Matrix", font_size=36)
#         example_title.next_to(title, DOWN, buff=0.5)
        
#         # Create coordinate system
#         axes = Axes(
#             x_range=[-3, 3, 1],
#             y_range=[-3, 3, 1],
#             axis_config={"include_tip": True}
#         )
#         grid = NumberPlane(
#             x_range=[-3, 3, 1],
#             y_range=[-3, 3, 1],
#             background_line_style={
#                 "stroke_opacity": 0.4
#             }
#         )
        
#         self.play(Create(grid), Create(axes))
#         self.play(Write(example_title))
        
#         # Define projection matrix onto x-axis
#         matrix_P = MathTex(r"P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}")
#         matrix_P.to_edge(UP, buff=1)
        
#         self.play(Write(matrix_P))
        
#         # Show the image - the x-axis
#         x_axis = Line(axes.c2p(-3, 0), axes.c2p(3, 0), color=RED)
#         image_label = Text("Image: x-axis", font_size=24, color=RED)
#         image_label.next_to(x_axis.get_end(), RIGHT, buff=0.2)
        
#         self.play(Create(x_axis), Write(image_label))
        
#         # Show the kernel - the y-axis
#         y_axis = Line(axes.c2p(0, -3), axes.c2p(0, 3), color=BLUE)
#         kernel_label = Text("Kernel: y-axis", font_size=24, color=BLUE)
#         kernel_label.next_to(y_axis.get_end(), UP, buff=0.2)
        
#         self.play(Create(y_axis), Write(kernel_label))
        
#         # Show a vector in the domain
#         v = Vector([2, 1], color=GREEN)
#         v_label = MathTex(r"\vec{v}", color=GREEN)
#         v_label.next_to(v.get_end(), UP+RIGHT, buff=0.1)
        
#         self.play(GrowArrow(v), Write(v_label))
        
#         # Show its projection onto the x-axis (the image)
#         v_proj = Vector([2, 0], color=YELLOW)
#         v_proj_label = MathTex(r"P\vec{v}", color=YELLOW)
#         v_proj_label.next_to(v_proj.get_end(), DOWN, buff=0.1)
        
#         projection_line = DashedLine(
#             start=axes.c2p(2, 1),
#             end=axes.c2p(2, 0),
#             color=YELLOW,
#             stroke_opacity=0.6
#         )
        
#         self.play(GrowArrow(v_proj), Write(v_proj_label), Create(projection_line))
#         self.wait(2)
        
#         # Show the Rank-Nullity theorem
#         self.play(
#             FadeOut(grid),
#             FadeOut(axes),
#             FadeOut(x_axis),
#             FadeOut(y_axis),
#             FadeOut(image_label),
#             FadeOut(kernel_label),
#             FadeOut(v),
#             FadeOut(v_label),
#             FadeOut(v_proj),
#             FadeOut(v_proj_label),
#             FadeOut(projection_line),
#             FadeOut(matrix_P),
#             FadeOut(example_title)
#         )
        
#         rank_nullity_title = Text("Rank-Nullity Theorem", font_size=36)
#         rank_nullity_title.next_to(title, DOWN, buff=0.5)
        
#         rank_nullity_eq = MathTex(r"\text{dim}(\text{Im}(A)) + \text{dim}(\text{Ker}(A)) = n")
#         rank_nullity_eq.next_to(rank_nullity_title, DOWN, buff=0.5)
        
#         rank_nullity_explain = Text("The dimensions of the image and kernel sum to the dimension of the domain", font_size=24)
#         rank_nullity_explain.next_to(rank_nullity_eq, DOWN, buff=0.5)
        
#         self.play(Write(rank_nullity_title))
#         self.play(Write(rank_nullity_eq))
#         self.play(Write(rank_nullity_explain))
#         self.wait(2)
        
#         # Summary of concepts
#         self.play(
#             FadeOut(rank_nullity_title),
#             FadeOut(rank_nullity_eq),
#             FadeOut(rank_nullity_explain)
#         )
        
#         summary_title = Text("Summary of Key Concepts", font_size=36)
#         summary_title.next_to(title, DOWN, buff=0.5)
        
#         summary = BulletedList(
#             "Image: the set of all possible outputs (column space)",
#             "Kernel: the set of all inputs that map to zero",
#             "rank(A) = dimension of the image",
#             "nullity(A) = dimension of the kernel",
#             "rank(A) + nullity(A) = number of columns of A",
#             font_size=28
#         )
#         summary.next_to(summary_title, DOWN, buff=0.5)
        
#         self.play(Write(summary_title))
#         self.play(Write(summary))
#         self.wait(3)
        
#         # Final transition
#         self.play(
#             FadeOut(summary),
#             FadeOut(summary_title),
#             FadeOut(title)
#         )


# class ConclusionScene(Scene):
#     def construct(self):
#         title = Text("Linear Algebra: Building the Foundation", font_size=48)
#         self.play(Write(title))
#         self.wait(1)
        
#         summary = BulletedList(
#             "Vectors: directional quantities with magnitude",
#             "Matrices: transformations and operators",
#             "Systems of Linear Equations: finding solutions",
#             "Vector Spaces and Span: sets closed under operations",
#             "Basis and Rank: measuring dimension and information",
#             "Row Operations: tools for matrix manipulation",
#             "Image and Kernel: understanding transformations",
#             font_size=32
#         )
#         summary.next_to(title, DOWN, buff=0.5)
        
#         self.play(Write(summary), run_time=3)
#         self.wait(2)
        
#         applications = Text("Applications: Machine Learning, Computer Graphics, Quantum Physics, Data Science...", font_size=28)
#         applications.to_edge(DOWN, buff=1)
        
#         self.play(Write(applications))
#         self.wait(2)
        
#         final_message = Text("Understanding these fundamentals unlocks the power of linear algebra!", font_size=32)
#         final_message.to_edge(DOWN, buff=1)
        
#         self.play(ReplacementTransform(applications, final_message))
#         self.wait(3)
        
#         self.play(
#             FadeOut(title),
#             FadeOut(summary),
#             FadeOut(final_message)
#         )

from manim import *
import numpy as np

"""
Linear Algebra Visualizations using Manim CE
This program contains separate scenes for key linear algebra concepts,
organized in a pedagogically sound sequence with clear visualizations.
"""

class IntroScene(Scene):
    def construct(self):
        title = Text("Understanding Linear Algebra", font_size=48)
        subtitle = Text("A Visual Journey", font_size=36)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        topics = VGroup(
            Text("1. Vectors", font_size=30),
            Text("2. Vector Spaces", font_size=30),
            Text("3. Linear Transformations", font_size=30),
            Text("4. Systems of Linear Equations", font_size=30),
            Text("5. Matrices", font_size=30),
            Text("6. Basis and Rank", font_size=30),
            Text("7. Image and Kernel", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        topics.move_to(ORIGIN)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(Write(topics), run_time=3)
        self.wait(2)
        
        final_text = Text("Let's begin with vectors...", font_size=36)
        self.play(FadeOut(topics), FadeIn(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))


class VectorsScene(Scene):
    def construct(self):
        # Title
        title = Text("1. Vectors", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Create(axes_labels))
        self.wait(1)
        
        # Definition of a vector
        definition = Text("A vector is a quantity with both magnitude and direction.", font_size=28)
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(2)
        
        # Create a vector
        vector = Vector([3, 2], color=RED)
        vector_label = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}")
        vector_label.next_to(vector.get_end(), RIGHT)
        
        # Show vector components
        x_line = Line(
            start=ORIGIN,
            end=[3, 0, 0],
            color=GREEN
        )
        y_line = Line(
            start=[3, 0, 0],
            end=[3, 2, 0],
            color=BLUE
        )
        x_label = MathTex("x = 3", color=GREEN)
        x_label.next_to(x_line, DOWN)
        y_label = MathTex("y = 2", color=BLUE)
        y_label.next_to(y_line, RIGHT)
        
        # Animate vector
        self.play(GrowArrow(vector), Write(vector_label))
        self.wait(1)
        self.play(Create(x_line), Create(y_line), Write(x_label), Write(y_label))
        self.wait(2)
        
        # Vector operations
        operations_title = Text("Vector Operations", font_size=32)
        operations_title.next_to(definition, DOWN, buff=1.5)
        self.play(Write(operations_title))
        self.wait(1)
        
        # Clear previous elements except title and axes
        self.play(
            FadeOut(vector), FadeOut(vector_label),
            FadeOut(x_line), FadeOut(y_line),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(definition), FadeOut(operations_title)
        )
        
        # Vector addition
        vector1 = Vector([2, 1], color=RED)
        vector2 = Vector([1, 2], color=BLUE)
        vector2_shifted = Vector([1, 2], color=BLUE)
        vector2_shifted.shift([2, 1, 0])
        
        v1_label = MathTex(r"\vec{a} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", color=RED)
        v1_label.next_to(vector1.get_end(), RIGHT)
        
        v2_label = MathTex(r"\vec{b} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=BLUE)
        v2_label.next_to(vector2.get_end(), RIGHT)
        
        result_vector = Vector([3, 3], color=PURPLE)
        result_label = MathTex(r"\vec{a} + \vec{b} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}", color=PURPLE)
        result_label.next_to(result_vector.get_end(), RIGHT)
        
        addition_title = Text("Vector Addition", font_size=32)
        addition_title.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(addition_title))
        self.play(GrowArrow(vector1), Write(v1_label))
        self.play(GrowArrow(vector2), Write(v2_label))
        self.wait(1)
        
        self.play(Transform(vector2, vector2_shifted))
        self.play(GrowArrow(result_vector), Write(result_label))
        self.wait(2)
        
        # Clear for scalar multiplication
        self.play(
            FadeOut(vector1), FadeOut(v1_label),
            FadeOut(vector2), FadeOut(v2_label),
            FadeOut(result_vector), FadeOut(result_label),
            FadeOut(addition_title)
        )
        
        # Scalar multiplication
        scalar_title = Text("Scalar Multiplication", font_size=32)
        scalar_title.next_to(title, DOWN, buff=0.5)
        
        vector3 = Vector([2, 1], color=GREEN)
        v3_label = MathTex(r"\vec{v} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", color=GREEN)
        v3_label.next_to(vector3.get_end(), RIGHT)
        
        scaled_vector = Vector([4, 2], color=ORANGE)
        scaled_label = MathTex(r"2\vec{v} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}", color=ORANGE)
        scaled_label.next_to(scaled_vector.get_end(), RIGHT)
        
        self.play(Write(scalar_title))
        self.play(GrowArrow(vector3), Write(v3_label))
        self.wait(1)
        
        self.play(TransformFromCopy(vector3, scaled_vector), Write(scaled_label))
        self.wait(2)
        
        # Vector properties
        self.play(
            FadeOut(vector3), FadeOut(v3_label),
            FadeOut(scaled_vector), FadeOut(scaled_label),
            FadeOut(scalar_title)
        )
        
        # Show magnitude calculation
        mag_title = Text("Vector Magnitude", font_size=32)
        mag_title.next_to(title, DOWN, buff=0.5)
        
        vector4 = Vector([3, 4], color=YELLOW)
        v4_label = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}", color=YELLOW)
        v4_label.next_to(vector4.get_end(), RIGHT)
        
        magnitude_eq = MathTex(r"||\vec{v}|| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5")
        magnitude_eq.next_to(mag_title, DOWN, buff=0.5)
        
        # Show Pythagorean triangle
        x_line = Line(start=ORIGIN, end=[3, 0, 0], color=GREEN)
        y_line = Line(start=[3, 0, 0], end=[3, 4, 0], color=BLUE)
        triangle = Polygon(ORIGIN, [3, 0, 0], [3, 4, 0], fill_opacity=0.2)
        
        self.play(Write(mag_title))
        self.play(GrowArrow(vector4), Write(v4_label))
        self.wait(1)
        
        self.play(Create(triangle), Create(x_line), Create(y_line))
        self.play(Write(magnitude_eq))
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Vectors are the fundamental building blocks of linear algebra", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class VectorSpacesScene(Scene):
    def construct(self):
        # Title
        title = Text("2. Vector Spaces", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition
        definition = Text("A vector space is a collection of vectors that satisfies specific axioms.", font_size=28)
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(2)
        
        # Explain vector space formally
        formal_def = MathTex(r"V \text{ is a vector space over } \mathbb{R} \text{ if:}")
        formal_def.next_to(definition, DOWN, buff=0.5)
        self.play(Write(formal_def))
        
        # List the vector space axioms
        axioms = VGroup(
            MathTex(r"1. \text{ Closure under addition: } \vec{u} + \vec{v} \in V"),
            MathTex(r"2. \text{ Closure under scalar multiplication: } c\vec{v} \in V"),
            MathTex(r"3. \text{ Associativity: } (\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})"),
            MathTex(r"4. \text{ Commutativity: } \vec{u} + \vec{v} = \vec{v} + \vec{u}"),
            MathTex(r"5. \text{ Additive identity: } \exists \vec{0} : \vec{v} + \vec{0} = \vec{v}"),
            MathTex(r"6. \text{ Additive inverse: } \exists -\vec{v} : \vec{v} + (-\vec{v}) = \vec{0}"),
            MathTex(r"7. \text{ Multiplicative identity: } 1\vec{v} = \vec{v}"),
            MathTex(r"8. \text{ Distributivity: } c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        axioms.scale(0.8)
        axioms.next_to(formal_def, DOWN, buff=0.5)
        
        self.play(Write(axioms), run_time=4)
        self.wait(2)
        
        # Examples of vector spaces
        self.play(FadeOut(axioms), FadeOut(formal_def))
        
        examples_title = Text("Examples of Vector Spaces", font_size=32)
        examples_title.next_to(definition, DOWN, buff=1)
        self.play(Write(examples_title))
        
        examples = VGroup(
            MathTex(r"\mathbb{R}^2 = \left\{ \begin{bmatrix} x \\ y \end{bmatrix} : x, y \in \mathbb{R} \right\}"),
            MathTex(r"\mathbb{R}^3 = \left\{ \begin{bmatrix} x \\ y \\ z \end{bmatrix} : x, y, z \in \mathbb{R} \right\}"),
            MathTex(r"P_n = \{a_0 + a_1x + a_2x^2 + \ldots + a_nx^n : a_i \in \mathbb{R}\}"),
            MathTex(r"C[a,b] = \{f : [a,b] \to \mathbb{R} \text{ | } f \text{ is continuous}\}")
        ).arrange(DOWN, buff=0.5)
        examples.next_to(examples_title, DOWN, buff=0.5)
        
        self.play(Write(examples), run_time=3)
        self.wait(2)
        
        # Visualize R^2 as a vector space
        self.play(FadeOut(examples), FadeOut(examples_title))
        
        # Create a visualization of R^2
        r2_title = Text("Visualization of R²", font_size=32)
        r2_title.next_to(definition, DOWN, buff=0.5)
        self.play(Write(r2_title))
        
        # Setup coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        
        self.play(Create(grid), Create(axes), Create(axes_labels))
        self.wait(1)
        
        # Show some vectors in R^2
        vectors = VGroup(
            Vector([1, 2], color=RED),
            Vector([3, 1], color=BLUE),
            Vector([-2, 2], color=GREEN),
            Vector([0, -3], color=YELLOW)
        )
        
        self.play(AnimationGroup(*[GrowArrow(v) for v in vectors], lag_ratio=0.3))
        self.wait(1)
        
        # Show closure under operations
        operation_text = Text("Any linear combination stays in the space", font_size=24)
        operation_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(operation_text))
        
        # Show a linear combination
        v1 = vectors[0].copy()
        v2 = vectors[1].copy()
        
        v1_scaled = Vector([2, 4], color=RED)  # 2 * [1, 2]
        v2_scaled = Vector([1.5, 0.5], color=BLUE)  # 0.5 * [3, 1]
        
        result_vector = Vector([3.5, 4.5], color=PURPLE)  # [2, 4] + [1.5, 0.5]
        
        equation = MathTex(r"2\vec{v}_1 + 0.5\vec{v}_2 = \begin{bmatrix} 3.5 \\ 4.5 \end{bmatrix}")
        equation.next_to(operation_text, DOWN, buff=0.5)
        
        self.play(
            TransformFromCopy(v1, v1_scaled),
            TransformFromCopy(v2, v2_scaled)
        )
        self.wait(1)
        self.play(Write(equation))
        self.play(GrowArrow(result_vector))
        self.wait(2)
        
        # Transition to subspaces
        self.play(
            FadeOut(vectors), FadeOut(v1_scaled), FadeOut(v2_scaled),
            FadeOut(result_vector), FadeOut(equation), FadeOut(operation_text),
            FadeOut(r2_title)
        )
        
        # Introduce subspaces
        subspace_title = Text("Subspaces", font_size=32)
        subspace_title.next_to(definition, DOWN, buff=0.5)
        self.play(Write(subspace_title))
        
        subspace_def = Text("A subspace is a subset of a vector space that is itself a vector space.", font_size=24)
        subspace_def.next_to(subspace_title, DOWN, buff=0.5)
        self.play(Write(subspace_def))
        self.wait(1)
        
        # Visualize a line through origin as a subspace
        line_vector = Vector([4, 2], color=RED)
        line = Line(start=[-4, -2, 0], end=[4, 2, 0], color=RED)
        
        subspace_example = Text("Example: A line through the origin is a subspace of R²", font_size=24)
        subspace_example.next_to(subspace_def, DOWN, buff=0.5)
        
        self.play(Write(subspace_example))
        self.play(Create(line))
        self.wait(1)
        
        # Show vectors in this subspace
        subspace_vectors = VGroup(
            Vector([2, 1], color=YELLOW),
            Vector([-2, -1], color=GREEN),
            Vector([4, 2], color=BLUE)
        )
        
        self.play(AnimationGroup(*[GrowArrow(v) for v in subspace_vectors], lag_ratio=0.3))
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Vector spaces provide the mathematical foundation for linear algebra", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class LinearTransformationsScene(Scene):
    def construct(self):
        # Title
        title = Text("3. Linear Transformations", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition
        definition = Text("A linear transformation is a function between vector spaces that preserves vector operations.", font_size=28)
        definition.next_to(title, DOWN, buff=0.5)
        definition.scale(0.8)
        self.play(Write(definition))
        self.wait(2)
        
        # Formal definition
        formal_def = MathTex(r"T: V \to W \text{ is linear if:}")
        formal_def.next_to(definition, DOWN, buff=0.5)
        self.play(Write(formal_def))
        
        properties = VGroup(
            MathTex(r"1. \text{ Additivity: } T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})"),
            MathTex(r"2. \text{ Homogeneity: } T(c\vec{v}) = cT(\vec{v})")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        properties.next_to(formal_def, DOWN, buff=0.5)
        
        self.play(Write(properties))
        self.wait(2)
        
        # Setup for visualization
        self.play(FadeOut(formal_def), FadeOut(properties))
        
        # Create a grid to visualize transformations
        grid_title = Text("Visualizing Linear Transformations", font_size=32)
        grid_title.next_to(definition, DOWN, buff=0.5)
        self.play(Write(grid_title))
        
        # Setup initial grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        
        # Basis vectors
        basis_i = Vector([1, 0], color=RED)
        basis_j = Vector([0, 1], color=GREEN)
        
        i_label = MathTex(r"\hat{\imath}", color=RED)
        i_label.next_to(basis_i.get_end(), DOWN)
        
        j_label = MathTex(r"\hat{\jmath}", color=GREEN)
        j_label.next_to(basis_j.get_end(), LEFT)
        
        self.play(
            Create(grid),
            Create(axes),
            GrowArrow(basis_i),
            GrowArrow(basis_j),
            Write(i_label),
            Write(j_label)
        )
        self.wait(1)
        
        # Example 1: Scaling transformation
        transform_text = Text("Example 1: Scaling Transformation", font_size=28)
        transform_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(transform_text))
        
        # Define matrix for scaling
        matrix = MathTex(r"T(\vec{v}) = \begin{bmatrix} 2 & 0 \\ 0 & 1.5 \end{bmatrix}\vec{v}")
        matrix.next_to(transform_text, DOWN, buff=0.5)
        self.play(Write(matrix))
        self.wait(1)
        
        # Transformed basis vectors
        transformed_i = Vector([2, 0], color=RED_D)
        transformed_j = Vector([0, 1.5], color=GREEN_D)
        
        # Animate transformation
        self.play(
            Transform(basis_i, transformed_i),
            Transform(basis_j, transformed_j),
            Transform(i_label, MathTex(r"T(\hat{\imath})", color=RED_D).next_to(transformed_i.get_end(), DOWN)),
            Transform(j_label, MathTex(r"T(\hat{\jmath})", color=GREEN_D).next_to(transformed_j.get_end(), LEFT)),
            grid.animate.apply_matrix([[2, 0], [0, 1.5]])
        )
        self.wait(2)
        
        # Reset for next transformation
        self.play(
            FadeOut(transform_text),
            FadeOut(matrix),
            FadeOut(basis_i),
            FadeOut(basis_j),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(grid)
        )
        
        # Example 2: Rotation transformation
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        basis_i = Vector([1, 0], color=RED)
        basis_j = Vector([0, 1], color=GREEN)
        
        i_label = MathTex(r"\hat{\imath}", color=RED)
        i_label.next_to(basis_i.get_end(), DOWN)
        
        j_label = MathTex(r"\hat{\jmath}", color=GREEN)
        j_label.next_to(basis_j.get_end(), LEFT)
        
        self.play(
            Create(grid),
            GrowArrow(basis_i),
            GrowArrow(basis_j),
            Write(i_label),
            Write(j_label)
        )
        
        transform_text = Text("Example 2: Rotation Transformation (90° clockwise)", font_size=28)
        transform_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(transform_text))
        
        # Define matrix for rotation
        matrix = MathTex(r"T(\vec{v}) = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\vec{v}")
        matrix.next_to(transform_text, DOWN, buff=0.5)
        self.play(Write(matrix))
        self.wait(1)
        
        # Transformed basis vectors for rotation
        transformed_i = Vector([0, -1], color=RED_D)
        transformed_j = Vector([1, 0], color=GREEN_D)
        
        # Animate transformation
        self.play(
            Transform(basis_i, transformed_i),
            Transform(basis_j, transformed_j),
            Transform(i_label, MathTex(r"T(\hat{\imath})", color=RED_D).next_to(transformed_i.get_end(), UP)),
            Transform(j_label, MathTex(r"T(\hat{\jmath})", color=GREEN_D).next_to(transformed_j.get_end(), RIGHT)),
            grid.animate.apply_matrix([[0, 1], [-1, 0]])
        )
        self.wait(2)
        
        # Reset for next transformation
        self.play(
            FadeOut(transform_text),
            FadeOut(matrix),
            FadeOut(basis_i),
            FadeOut(basis_j),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(grid)
        )
        
        # Example 3: Shear transformation
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        basis_i = Vector([1, 0], color=RED)
        basis_j = Vector([0, 1], color=GREEN)
        
        i_label = MathTex(r"\hat{\imath}", color=RED)
        i_label.next_to(basis_i.get_end(), DOWN)
        
        j_label = MathTex(r"\hat{\jmath}", color=GREEN)
        j_label.next_to(basis_j.get_end(), LEFT)
        
        self.play(
            Create(grid),
            GrowArrow(basis_i),
            GrowArrow(basis_j),
            Write(i_label),
            Write(j_label)
        )
        
        transform_text = Text("Example 3: Shear Transformation", font_size=28)
        transform_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(transform_text))
        
        # Define matrix for shear
        matrix = MathTex(r"T(\vec{v}) = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\vec{v}")
        matrix.next_to(transform_text, DOWN, buff=0.5)
        self.play(Write(matrix))
        self.wait(1)
        
        # Transformed basis vectors for shear
        transformed_i = Vector([1, 0], color=RED_D)
        transformed_j = Vector([1, 1], color=GREEN_D)
        
        # Animate transformation
        self.play(
            Transform(basis_i, transformed_i),
            Transform(basis_j, transformed_j),
            Transform(i_label, MathTex(r"T(\hat{\imath})", color=RED_D).next_to(transformed_i.get_end(), DOWN)),
            Transform(j_label, MathTex(r"T(\hat{\jmath})", color=GREEN_D).next_to(transformed_j.get_end(), UP+RIGHT)),
            grid.animate.apply_matrix([[1, 1], [0, 1]])
        )
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Linear transformations are the essence of linear algebra", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class LinearSystemsScene(Scene):
    def construct(self):
        # Title
        title = Text("4. Systems of Linear Equations", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition
        definition = Text("A system of linear equations is a collection of linear equations with the same variables.", font_size=28)
        definition.next_to(title, DOWN, buff=0.5)
        definition.scale(0.8)
        self.play(Write(definition))
        self.wait(2)
        
        # Example system
        example_title = Text("Example System", font_size=32)
        example_title.next_to(definition, DOWN, buff=0.7)
        self.play(Write(example_title))
        
        system = MathTex(r"""\begin{cases}
        2x + y = 5 \\
        x - y = 1
        \end{cases}""")
        system.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(system))
        self.wait(1)
        
        # Graphical interpretation
        graph_title = Text("Graphical Interpretation", font_size=28)
        graph_title.next_to(system, DOWN, buff=1)
        self.play(Write(graph_title))
        
        # Setup coordinate system for graphing
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(axes), Create(axes_labels))
        self.wait(1)
        
        # First line: 2x + y = 5 => y = 5 - 2x
        line1 = axes.plot(lambda x: 5 - 2*x, color=RED)
        line1_label = MathTex("2x + y = 5", color=RED)
        line1_label.next_to(line1.point_from_proportion(0.7), UP)
        
        # Second line: x - y = 1 => y = x - 1
        line2 = axes.plot(lambda x: x - 1, color=BLUE)
        line2_label = MathTex("x - y = 1", color=BLUE)
        line2_label.next_to(line2.point_from_proportion(0.3), DOWN)
        
        self.play(Create(line1), Write(line1_label))
        self.play(Create(line2), Write(line2_label))
        self.wait(1)
        
        # Show intersection point
        intersection_point = Dot([2, 1, 0], color=GREEN)
        intersection_label = MathTex(r"(2, 1)", color=GREEN)
        intersection_label.next_to(intersection_point, RIGHT)
        
        self.play(Create(intersection_point), Write(intersection_label))
        self.wait(1)
        
        solution_text = Text("The solution is x = 2, y = 1", font_size=24)
        solution_text.next_to(axes, DOWN, buff=0.5)
        self.play(Write(solution_text))
        self.wait(2)
        
        # Clear for matrix representation
        self.play(
            FadeOut(axes), FadeOut(axes_labels),
            FadeOut(line1), FadeOut(line1_label),
            FadeOut(line2), FadeOut(line2_label),
            FadeOut(intersection_point), FadeOut(intersection_label),
            FadeOut(solution_text), FadeOut(graph_title)
        )
        
        # Matrix representation
        matrix_title = Text("Matrix Representation", font_size=32)
        matrix_title.next_to(system, DOWN, buff=0.7)
        self.play(Write(matrix_title))
        
        matrix_form = MathTex(r"\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}")
        matrix_form.next_to(matrix_title, DOWN, buff=0.5)
        
        compact_form = MathTex(r"A\vec{x} = \vec{b}")
        compact_form.next_to(matrix_form, DOWN, buff=0.5)
        
        self.play(Write(matrix_form))
        self.play(Write(compact_form))
        self.wait(2)
        
        # Solving the system
        solving_title = Text("Solving the System", font_size=32)
        solving_title.next_to(compact_form, DOWN, buff=0.7)
        self.play(Write(solving_title))
        
        steps = VGroup(
            MathTex(r"A\vec{x} = \vec{b}"),
            MathTex(r"A^{-1}A\vec{x} = A^{-1}\vec{b}"),
            MathTex(r"I\vec{x} = A^{-1}\vec{b}"),
            MathTex(r"\vec{x} = A^{-1}\vec{b}")
        ).arrange(DOWN, buff=0.5)
        steps.next_to(solving_title, DOWN, buff=0.5)
        
        self.play(Write(steps), run_time=3)
        self.wait(2)
        
        # Illustrate different solution types
        self.play(
            FadeOut(steps), FadeOut(solving_title),
            FadeOut(matrix_form), FadeOut(compact_form),
            FadeOut(matrix_title), FadeOut(system),
            FadeOut(example_title)
        )
        
        # Types of solutions
        types_title = Text("Types of Solutions", font_size=32)
        types_title.next_to(definition, DOWN, buff=0.7)
        self.play(Write(types_title))
        
        # Create examples for each type
        examples = VGroup(
            Text("1. Unique solution (lines intersect at one point)", font_size=24, color=GREEN),
            Text("2. No solution (parallel lines)", font_size=24, color=RED),
            Text("3. Infinitely many solutions (lines are the same)", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        examples.next_to(types_title, DOWN, buff=0.5)
        
        self.play(Write(examples), run_time=3)
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Linear systems are central to many applications in science and engineering", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class MatricesScene(Scene):
    def construct(self):
        # Title
        title = Text("5. Matrices", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition
        definition = Text("A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns.", font_size=28)
        definition.next_to(title, DOWN, buff=0.5)
        definition.scale(0.8)
        self.play(Write(definition))
        self.wait(2)
        
        # Example of a matrix
        matrix_example = MathTex(r"A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}")
        matrix_example.next_to(definition, DOWN, buff=0.7)
        self.play(Write(matrix_example))
        
        # Dimensions
        dimensions = Text("This is a 3×3, or square, matrix", font_size=24)
        dimensions.next_to(matrix_example, DOWN, buff=0.5)
        self.play(Write(dimensions))
        self.wait(2)
        
        # Matrix operations
        operations_title = Text("Matrix Operations", font_size=32)
        operations_title.next_to(dimensions, DOWN, buff=1)
        self.play(Write(operations_title))
        
        # Matrix addition
        self.play(FadeOut(matrix_example), FadeOut(dimensions))
        
        addition_title = Text("Addition", font_size=28)
        addition_title.next_to(operations_title, DOWN, buff=0.5)
        self.play(Write(addition_title))
        
        matrix_a = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
        matrix_b = MathTex(r"B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")
        matrix_sum = MathTex(r"A + B = \begin{bmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}")
        
        matrices = VGroup(matrix_a, matrix_b, matrix_sum).arrange(DOWN, buff=0.5)
        matrices.next_to(addition_title, DOWN, buff=0.5)
        
        self.play(Write(matrix_a))
        self.play(Write(matrix_b))
        self.play(Write(matrix_sum))
        self.wait(2)
        
        # Matrix multiplication
        self.play(FadeOut(matrices), FadeOut(addition_title))
        
        mult_title = Text("Multiplication", font_size=28)
        mult_title.next_to(operations_title, DOWN, buff=0.5)
        self.play(Write(mult_title))
        
        matrix_c = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
        matrix_d = MathTex(r"B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")
        
        mult_process = MathTex(r"A \times B = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{bmatrix}")
        matrix_product = MathTex(r"A \times B = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}")
        
        mult_steps = VGroup(matrix_c, matrix_d, mult_process, matrix_product).arrange(DOWN, buff=0.5)
        mult_steps.next_to(mult_title, DOWN, buff=0.5)
        
        self.play(Write(matrix_c))
        self.play(Write(matrix_d))
        self.play(Write(mult_process))
        self.play(Write(matrix_product))
        self.wait(2)
        
        # Matrix properties
        self.play(FadeOut(mult_steps), FadeOut(mult_title), FadeOut(operations_title))
        
        properties_title = Text("Important Properties", font_size=32)
        properties_title.next_to(definition, DOWN, buff=0.7)
        self.play(Write(properties_title))
        
        properties = VGroup(
            MathTex(r"1. \text{ Not commutative: } A \times B \neq B \times A \text{ (generally)}"),
            MathTex(r"2. \text{ Associative: } (A \times B) \times C = A \times (B \times C)"),
            MathTex(r"3. \text{ Distributive: } A \times (B + C) = A \times B + A \times C"),
            MathTex(r"4. \text{ Identity matrix: } A \times I = I \times A = A")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        properties.next_to(properties_title, DOWN, buff=0.5)
        
        self.play(Write(properties), run_time=3)
        self.wait(2)
        
        # Special matrices
        self.play(FadeOut(properties))
        
        special_title = Text("Special Matrices", font_size=32)
        special_title.next_to(properties_title, DOWN, buff=0.5)
        self.play(Write(special_title))
        
        # Identity matrix
        identity = MathTex(r"I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}")
        identity_desc = Text("Identity Matrix (like 1 in scalar multiplication)", font_size=24)
        
        # Zero matrix
        zero = MathTex(r"O = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}")
        zero_desc = Text("Zero Matrix (like 0 in scalar addition)", font_size=24)
        
        # Diagonal matrix
        diagonal = MathTex(r"D = \begin{bmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{bmatrix}")
        diagonal_desc = Text("Diagonal Matrix (non-zero entries only on diagonal)", font_size=24)
        
        special_matrices = VGroup(
            VGroup(identity, identity_desc).arrange(DOWN, buff=0.3),
            VGroup(zero, zero_desc).arrange(DOWN, buff=0.3),
            VGroup(diagonal, diagonal_desc).arrange(DOWN, buff=0.3)
        ).arrange(DOWN, buff=0.7)
        special_matrices.next_to(special_title, DOWN, buff=0.5)
        
        self.play(Write(special_matrices), run_time=4)
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Matrices are powerful tools for representing and solving linear systems", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class BasisRankScene(Scene):
    def construct(self):
        # Title
        title = Text("6. Basis and Rank", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Section for Basis
        basis_title = Text("Basis", font_size=36)
        basis_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(basis_title))
        
        # Definition of basis
        basis_def = Text("A basis is a set of linearly independent vectors that span a vector space.", font_size=28)
        basis_def.next_to(basis_title, DOWN, buff=0.5)
        basis_def.scale(0.8)
        self.play(Write(basis_def))
        self.wait(2)
        
        # Linear independence definition
        li_title = Text("Linear Independence", font_size=28)
        li_title.next_to(basis_def, DOWN, buff=0.7)
        self.play(Write(li_title))
        
        li_def = MathTex(r"\text{Vectors } \vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n \text{ are linearly independent if:}")
        li_equation = MathTex(r"c_1\vec{v}_1 + c_2\vec{v}_2 + \ldots + c_n\vec{v}_n = \vec{0} \text{ implies } c_1 = c_2 = \ldots = c_n = 0")
        
        li_group = VGroup(li_def, li_equation).arrange(DOWN, buff=0.5)
        li_group.next_to(li_title, DOWN, buff=0.5)
        
        self.play(Write(li_group))
        self.wait(2)
        
        # Visualize basis in R^2
        self.play(FadeOut(li_group), FadeOut(li_title))
        
        vis_title = Text("Visualizing a Basis in R²", font_size=28)
        vis_title.next_to(basis_def, DOWN, buff=0.7)
        self.play(Write(vis_title))
        
        # Setup coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        
        self.play(Create(grid), Create(axes), Create(axes_labels))
        self.wait(1)
        
        # Standard basis
        standard_i = Vector([1, 0], color=RED)
        standard_j = Vector([0, 1], color=GREEN)
        
        i_label = MathTex(r"\vec{e}_1", color=RED)
        i_label.next_to(standard_i.get_end(), DOWN)
        
        j_label = MathTex(r"\vec{e}_2", color=GREEN)
        j_label.next_to(standard_j.get_end(), LEFT)
        
        standard_basis_text = Text("Standard Basis: {e₁, e₂}", font_size=24)
        standard_basis_text.next_to(axes, DOWN, buff=0.5)
        
        self.play(
            GrowArrow(standard_i),
            GrowArrow(standard_j),
            Write(i_label),
            Write(j_label),
            Write(standard_basis_text)
        )
        self.wait(2)
        
        # Alternative basis
        self.play(
            FadeOut(standard_i),
            FadeOut(standard_j),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(standard_basis_text)
        )
        
        alt_v1 = Vector([2, 1], color=BLUE)
        alt_v2 = Vector([1, 2], color=YELLOW)
        
        v1_label = MathTex(r"\vec{v}_1", color=BLUE)
        v1_label.next_to(alt_v1.get_end(), RIGHT)
        
        v2_label = MathTex(r"\vec{v}_2", color=YELLOW)
        v2_label.next_to(alt_v2.get_end(), UP)
        
        alt_basis_text = Text("Alternative Basis: {v₁, v₂}", font_size=24)
        alt_basis_text.next_to(axes, DOWN, buff=0.5)
        
        self.play(
            GrowArrow(alt_v1),
            GrowArrow(alt_v2),
            Write(v1_label),
            Write(v2_label),
            Write(alt_basis_text)
        )
        self.wait(1)
        
        # Show spanning with new basis
        vector_to_express = Vector([5, 5], color=PURPLE)
        vector_label = MathTex(r"\vec{w}", color=PURPLE)
        vector_label.next_to(vector_to_express.get_end(), RIGHT)
        
        self.play(GrowArrow(vector_to_express), Write(vector_label))
        
        # Components
        component1 = Vector([4, 2], color=BLUE, opacity=0.5)  # 2 * v1
        component2 = Vector([1, 3], color=YELLOW, opacity=0.5)  # 3 * v2
        
        expression = MathTex(r"\vec{w} = 2\vec{v}_1 + 3\vec{v}_2")
        expression.next_to(alt_basis_text, DOWN, buff=0.5)
        
        self.play(GrowArrow(component1), GrowArrow(component2))
        self.play(Write(expression))
        self.wait(2)
        
        # Transition to rank
        self.play(
            FadeOut(grid), FadeOut(axes), FadeOut(axes_labels),
            FadeOut(alt_v1), FadeOut(alt_v2),
            FadeOut(v1_label), FadeOut(v2_label),
            FadeOut(vector_to_express), FadeOut(vector_label),
            FadeOut(component1), FadeOut(component2),
            FadeOut(expression), FadeOut(alt_basis_text),
            FadeOut(vis_title)
        )
        
        # Rank Section
        rank_title = Text("Rank", font_size=36)
        rank_title.next_to(basis_def, DOWN, buff=1)
        self.play(Write(rank_title))
        
        rank_def = Text("The rank of a matrix is the dimension of the vector space spanned by its columns or rows.", font_size=28)
        rank_def.next_to(rank_title, DOWN, buff=0.5)
        rank_def.scale(0.8)
        self.play(Write(rank_def))
        self.wait(2)
        
        # Example of rank
        example_title = Text("Example", font_size=28)
        example_title.next_to(rank_def, DOWN, buff=0.7)
        self.play(Write(example_title))
        
        matrix_a = MathTex(r"A = \begin{bmatrix} 1 & 3 & 2 \\ 2 & 6 & 4 \\ 0 & 0 & 0 \end{bmatrix}")
        matrix_a.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(matrix_a))
        self.wait(1)
        
        # Column view
        columns = MathTex(r"\text{Columns: } \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}, \begin{bmatrix} 3 \\ 6 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix}")
        columns.next_to(matrix_a, DOWN, buff=0.5)
        self.play(Write(columns))
        
        # Relationship between columns
        relation = MathTex(r"\begin{bmatrix} 3 \\ 6 \\ 0 \end{bmatrix} = 3 \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}, \quad \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix} = 2 \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}")
        relation.next_to(columns, DOWN, buff=0.5)
        self.play(Write(relation))
        self.wait(1)
        
        # Only one linearly independent column
        conclusion = Text("Only one linearly independent column ⟹ rank(A) = 1", font_size=28)
        conclusion.next_to(relation, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Rank properties
        self.play(
            FadeOut(matrix_a), FadeOut(columns),
            FadeOut(relation), FadeOut(conclusion),
            FadeOut(example_title)
        )
        
        props_title = Text("Properties of Rank", font_size=28)
        props_title.next_to(rank_def, DOWN, buff=0.7)
        self.play(Write(props_title))
        
        props = VGroup(
            Text("1. 0 ≤ rank(A) ≤ min(m,n) for an m×n matrix", font_size=24),
            Text("2. rank(A) = rank(A^T)", font_size=24),
            Text("3. rank(AB) ≤ min(rank(A), rank(B))", font_size=24),
            Text("4. A matrix is invertible if and only if rank(A) = n (for n×n matrix)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        props.next_to(props_title, DOWN, buff=0.5)
        
        self.play(Write(props), run_time=3)
        self.wait(2)
        
        # Conclusion
        final_text = Text("Basis and rank are fundamental for understanding vector spaces and matrices", font_size=28)
        final_text.to_edge(DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class MatrixTransformationsScene(Scene):
    def construct(self):
        # Title
        title = Text("7. Elementary Row Operations and Echelon Form", font_size=42)
        title.to_edge(UP)
        title.scale(0.9)
        self.play(Write(title))
        self.wait(1)
        
        # Elementary row operations
        ero_title = Text("Elementary Row Operations", font_size=36)
        ero_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(ero_title))
        
        # List the operations
        operations = VGroup(
            Text("1. Swap two rows: Rᵢ ↔ Rⱼ", font_size=28),
            Text("2. Multiply a row by a non-zero scalar: Rᵢ → c·Rᵢ", font_size=28),
            Text("3. Add a multiple of one row to another: Rᵢ → Rᵢ + c·Rⱼ", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        operations.next_to(ero_title, DOWN, buff=0.5)
        
        self.play(Write(operations), run_time=3)
        self.wait(2)
        
        # Example of using row operations
        self.play(FadeOut(operations))
        
        example_title = Text("Example: Applying Row Operations", font_size=28)
        example_title.next_to(ero_title, DOWN, buff=0.5)
        self.play(Write(example_title))
        
        # Initial matrix
        matrix_a = MathTex(r"A = \begin{bmatrix} 1 & 3 & 2 \\ 2 & 7 & 4 \\ 1 & 5 & 3 \end{bmatrix}")
        matrix_a.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(matrix_a))
        self.wait(1)
        
        # Operations one by one
        op1 = MathTex(r"R_2 \to R_2 - 2R_1: \begin{bmatrix} 1 & 3 & 2 \\ 0 & 1 & 0 \\ 1 & 5 & 3 \end{bmatrix}")
        op2 = MathTex(r"R_3 \to R_3 - R_1: \begin{bmatrix} 1 & 3 & 2 \\ 0 & 1 & 0 \\ 0 & 2 & 1 \end{bmatrix}")
        op3 = MathTex(r"R_3 \to R_3 - 2R_2: \begin{bmatrix} 1 & 3 & 2 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}")
        
        operations = VGroup(op1, op2, op3).arrange(DOWN, buff=0.7)
        operations.next_to(matrix_a, DOWN, buff=0.7)
        
        self.play(Write(op1))
        self.wait(1)
        self.play(Write(op2))
        self.wait(1)
        self.play(Write(op3))
        self.wait(2)
        
        # Row Echelon Form
        self.play(
            FadeOut(matrix_a), FadeOut(operations),
            FadeOut(example_title)
        )
        
        ref_title = Text("Row Echelon Form (REF)", font_size=32)
        ref_title.next_to(ero_title, DOWN, buff=0.7)
        self.play(Write(ref_title))
        
        ref_properties = VGroup(
            Text("Properties:", font_size=28),
            Text("1. All zero rows are at the bottom", font_size=24),
            Text("2. Leading entry of each non-zero row is to the right of the leading entry above", font_size=24),
            Text("3. All entries in a column below a leading entry are zeros", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        ref_properties.next_to(ref_title, DOWN, buff=0.5)
        
        self.play(Write(ref_properties), run_time=3)
        self.wait(2)
        
        # Example of REF
        ref_example = MathTex(r"\begin{bmatrix} 1 & 3 & 2 & 5 \\ 0 & 1 & 7 & 9 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}")
        ref_example.next_to(ref_properties, DOWN, buff=0.7)
        self.play(Write(ref_example))
        self.wait(1)
        
        # Reduced Row Echelon Form
        self.play(FadeOut(ref_properties), FadeOut(ref_example))
        
        rref_title = Text("Reduced Row Echelon Form (RREF)", font_size=32)
        rref_title.next_to(ref_title, DOWN, buff=0.7)
        self.play(Write(rref_title))
        
        rref_properties = VGroup(
            Text("Additional properties:", font_size=28),
            Text("4. Leading entry of each non-zero row is 1", font_size=24),
            Text("5. Each leading 1 is the only non-zero entry in its column", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rref_properties.next_to(rref_title, DOWN, buff=0.5)
        
        self.play(Write(rref_properties), run_time=2)
        self.wait(1)
        
        # Example of RREF
        rref_example = MathTex(r"\begin{bmatrix} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}")
        rref_example.next_to(rref_properties, DOWN, buff=0.7)
        self.play(Write(rref_example))
        self.wait(2)
        
        # Applications
        self.play(
            FadeOut(rref_properties), FadeOut(rref_example),
            FadeOut(rref_title), FadeOut(ref_title)
        )
        
        apps_title = Text("Applications", font_size=32)
        apps_title.next_to(ero_title, DOWN, buff=0.7)
        self.play(Write(apps_title))
        
        applications = VGroup(
            Text("1. Solving systems of linear equations", font_size=24),
            Text("2. Finding the rank of a matrix", font_size=24),
            Text("3. Computing the inverse of a matrix", font_size=24),
            Text("4. Finding bases for fundamental subspaces", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        applications.next_to(apps_title, DOWN, buff=0.5)
        
        self.play(Write(applications), run_time=3)
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Row operations and echelon forms provide systematic methods for matrix calculations", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        conclusion.scale(0.8)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Clear scene for transition
        self.play(FadeOut(VGroup(*self.mobjects)))


class ImageKernelScene(Scene):
    def construct(self):
        # Title
        title = Text("8. Image and Kernel", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition for Linear Transformation
        lt_def = Text("For a linear transformation T: V → W between vector spaces:", font_size=28)
        lt_def.next_to(title, DOWN, buff=0.7)
        self.play(Write(lt_def))
        self.wait(1)
        
        # Image definition
        image_title = Text("Image (Range)", font_size=36)
        image_title.next_to(lt_def, DOWN, buff=0.7)
        self.play(Write(image_title))
        
        image_def = MathTex(r"\text{Im}(T) = \{\vec{w} \in W \mid \vec{w} = T(\vec{v}) \text{ for some } \vec{v} \in V\}")
        image_def.next_to(image_title, DOWN, buff=0.5)
        self.play(Write(image_def))
        
        image_explain = Text("The image is the set of all possible outputs of the transformation", font_size=24)
        image_explain.next_to(image_def, DOWN, buff=0.5)
        self.play(Write(image_explain))
        self.wait(2)
        
        # Kernel definition
        self.play(
            FadeOut(image_def), FadeOut(image_explain)
        )
        
        kernel_title = Text("Kernel (Null Space)", font_size=36)
        kernel_title.next_to(image_title, DOWN, buff=1)
        self.play(Write(kernel_title))
        
        kernel_def = MathTex(r"\text{Ker}(T) = \{\vec{v} \in V \mid T(\vec{v}) = \vec{0}\}")
        kernel_def.next_to(kernel_title, DOWN, buff=0.5)
        self.play(Write(kernel_def))
        
        kernel_explain = Text("The kernel is the set of all vectors that map to the zero vector", font_size=24)
        kernel_explain.next_to(kernel_def, DOWN, buff=0.5)
        self.play(Write(kernel_explain))
        self.wait(2)
        
        # Matrix representation
        self.play(
            FadeOut(kernel_def), FadeOut(kernel_explain),
            FadeOut(kernel_title), FadeOut(image_title)
        )
        
        matrix_title = Text("Matrix Representation", font_size=32)
        matrix_title.next_to(lt_def, DOWN, buff=0.7)
        self.play(Write(matrix_title))
        
        matrix_text = Text("For a linear transformation represented by matrix A:", font_size=24)
        matrix_text.next_to(matrix_title, DOWN, buff=0.5)
        self.play(Write(matrix_text))
        
        image_matrix = MathTex(r"\text{Im}(A) = \{\vec{b} \in \mathbb{R}^m \mid \vec{b} = A\vec{x} \text{ for some } \vec{x} \in \mathbb{R}^n\}")
        image_matrix.next_to(matrix_text, DOWN, buff=0.5)
        self.play(Write(image_matrix))
        
        kernel_matrix = MathTex(r"\text{Ker}(A) = \{\vec{x} \in \mathbb{R}^n \mid A\vec{x} = \vec{0}\}")
        kernel_matrix.next_to(image_matrix, DOWN, buff=0.5)
        self.play(Write(kernel_matrix))
        self.wait(2)
        
        # Visualizing Image and Kernel
        self.play(
            FadeOut(image_matrix), FadeOut(kernel_matrix),
            FadeOut(matrix_title), FadeOut(matrix_text)
        )
        
        vis_title = Text("Visualization Example", font_size=32)
        vis_title.next_to(lt_def, DOWN, buff=0.7)
        self.play(Write(vis_title))
        
        # Example matrix
        example_matrix = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}")
        example_matrix.next_to(vis_title, DOWN, buff=0.5)
        self.play(Write(example_matrix))
        self.wait(1)
        
        # Setup coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        
        self.play(
            Create(grid), Create(axes), Create(axes_labels)
        )
        self.wait(1)
        
        # Visualize kernel
        kernel_vector = Vector([2, -1], color=RED)
        kernel_label = MathTex(r"\vec{v} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}", color=RED)
        kernel_label.next_to(kernel_vector.get_end(), RIGHT)
        
        kernel_text = MathTex(r"A\vec{v} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}")
        kernel_text.next_to(grid, DOWN, buff=0.5)
        
        self.play(GrowArrow(kernel_vector), Write(kernel_label))
        self.play(Write(kernel_text))
        self.wait(1)
        
        kernel_line = Line(start=[-4, 2, 0], end=[4, -2, 0], color=RED_D)
        kernel_line_text = Text("Kernel: line with direction vector [2, -1]", font_size=24)
        kernel_line_text.next_to(kernel_text, DOWN, buff=0.5)
        
        self.play(Create(kernel_line), Write(kernel_line_text))
        self.wait(2)
        
        # Visualize image
        self.play(
            FadeOut(kernel_vector), FadeOut(kernel_label),
            FadeOut(kernel_text), FadeOut(kernel_line),
            FadeOut(kernel_line_text)
        )
        
        # Column vectors
        col1 = Vector([1, 2], color=BLUE)
        col1_label = MathTex(r"\vec{a}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=BLUE)
        col1_label.next_to(col1.get_end(), RIGHT)
        
        col2 = Vector([2, 4], color=GREEN)
        col2_label = MathTex(r"\vec{a}_2 = \begin{bmatrix} 2 \\ 4 \end{bmatrix}", color=GREEN)
        col2_label.next_to(col2.get_end(), RIGHT)
        
        self.play(GrowArrow(col1), Write(col1_label))
        self.play(GrowArrow(col2), Write(col2_label))
        self.wait(1)
        
        # Show they're linearly dependent
        ld_text = MathTex(r"\vec{a}_2 = 2\vec{a}_1")
        ld_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(ld_text))
        
        # Image is a line
        image_line = Line(start=[-5, -10, 0], end=[5, 10, 0], color=PURPLE)
        image_text = Text("Image: line with direction vector [1, 2]", font_size=24)
        image_text.next_to(ld_text, DOWN, buff=0.5)
        
        self.play(Create(image_line), Write(image_text))
        self.wait(2)
        
        # Rank-Nullity Theorem
        self.play(
            FadeOut(grid), FadeOut(axes), FadeOut(axes_labels),
            FadeOut(col1), FadeOut(col1_label),
            FadeOut(col2), FadeOut(col2_label),
            FadeOut(ld_text), FadeOut(image_line),
            FadeOut(image_text), FadeOut(example_matrix),
            FadeOut(vis_title)
        )
        
        theorem_title = Text("Rank-Nullity Theorem", font_size=32)
        theorem_title.next_to(lt_def, DOWN, buff=0.7)
        self.play(Write(theorem_title))
        
        theorem = MathTex(r"\dim(V) = \dim(\text{Im}(T)) + \dim(\text{Ker}(T))")
        theorem.next_to(theorem_title, DOWN, buff=0.5)
        self.play(Write(theorem))
        
        theorem_matrix = MathTex(r"\text{For a matrix } A_{m \times n}: \quad n = \text{rank}(A) + \text{nullity}(A)")
        theorem_matrix.next_to(theorem, DOWN, buff=0.5)
        self.play(Write(theorem_matrix))
        self.wait(1)
        
        example_text = Text("Example: For our 2×2 matrix, dim(R²) = 2, rank(A) = 1, nullity(A) = 1", font_size=24)
        example_text.next_to(theorem_matrix, DOWN, buff=0.7)
        self.play(Write(example_text))
        self.wait(2)
        
        # Applications
        self.play(
            FadeOut(theorem), FadeOut(theorem_matrix),
            FadeOut(example_text), FadeOut(theorem_title)
        )
        
        app_title = Text("Applications", font_size=32)
        app_title.next_to(lt_def, DOWN, buff=0.7)
        self.play(Write(app_title))
        
        applications = VGroup(
            Text("1. Solving homogeneous linear systems (Ax = 0)", font_size=24),
            Text("2. Understanding linear transformations geometrically", font_size=24),
            Text("3. Analyzing data in machine learning (PCA, dimension reduction)", font_size=24),
            Text("4. Differential equations and dynamical systems", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        applications.next_to(app_title, DOWN, buff=0.5)
        
        self.play(Write(applications), run_time=3)
        self.wait(2)
        
        # Conclusion
        conclusion = Text("Image and Kernel characterize the fundamental properties of linear transformations", font_size=28)
        conclusion.to_edge(DOWN, buff=1)
        conclusion.scale(0.8)
        self.play(Write(conclusion))
        self.wait(2)
        
        # Final scene
        self.play(FadeOut(VGroup(*self.mobjects)))
        
        final_title = Text("Linear Algebra", font_size=48)
        final_title.to_edge(UP, buff=1)
        self.play(Write(final_title))
        
        final_text = VGroup(
            Text("Understanding linear algebra is crucial for:", font_size=36),
            Text("• Machine Learning", font_size=30),
            Text("• Computer Graphics", font_size=30),
            Text("• Data Science", font_size=30),
            Text("• Engineering", font_size=30),
            Text("• Physics", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_text.next_to(final_title, DOWN, buff=1)
        
        self.play(Write(final_text), run_time=3)
        self.wait(2)
        
        self.play(FadeOut(VGroup(*self.mobjects)))


# Scenes in order of presentation
class LinearAlgebraJourney(Scene):
    def construct(self):
        # Title sequence
        title = Text("A Visual Journey Through Linear Algebra", font_size=48)
        subtitle = Text("Fundamentals for Machine Learning", font_size=36)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        # List of topics
        topics = VGroup(
            Text("1. Vectors", font_size=30),
            Text("2. Vector Spaces", font_size=30),
            Text("3. Linear Transformations", font_size=30),
            Text("4. Systems of Linear Equations", font_size=30),
            Text("5. Matrices", font_size=30),
            Text("6. Basis and Rank", font_size=30),
            Text("7. Elementary Row Operations", font_size=30),
            Text("8. Image and Kernel", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        topics.move_to(ORIGIN)
        
        self.play(FadeOut(subtitle))
        self.play(Write(topics), run_time=4)
        self.wait(2)
        
        self.play(FadeOut(topics), FadeOut(title))