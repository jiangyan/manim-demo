from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Introduction
        title = Text("The Pythagorean Theorem", font_size=72)
        subtitle = Text("a² + b² = c²", font_size=48)
        
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_edge(UP))
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))
        
        # Creating the right triangle
        triangle = self.create_right_triangle()
        triangle.scale(0.8)
        triangle_group = self.label_triangle(triangle)
        triangle_group.shift(LEFT * 2.5 + DOWN * 1)
        
        self.play(Create(triangle_group))
        self.wait(1)
        
        # Show the squares on each side
        squares = self.create_squares(triangle)
        self.play(Create(squares))
        self.wait(1)
        
        # Highlight the relationship
        self.show_area_relationship(triangle, squares)
        
        # Show algebraic formulation
        self.show_algebraic_proof()
        
        # Final summary
        final_theorem = MathTex("a^2 + b^2 = c^2").scale(2)
        self.play(FadeOut(*self.mobjects))
        self.play(Write(final_theorem))
        self.wait(2)
        
        # Add caption
        caption = Text("The Pythagorean Theorem", font_size=36).next_to(final_theorem, DOWN)
        self.play(Write(caption))
        self.wait(2)
    
    def create_right_triangle(self):
        """Create a right triangle with sides 3, 4, and 5."""
        # Create points for a 3-4-5 triangle with right angle at A
        A = np.array([-1.5, -1, 0])
        B = np.array([1.5, -1, 0])    # Side a = 3 
        C = np.array([-1.5, 1, 0])    # Side b = 2
        
        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)
        
        # Add the right angle marker
        right_angle = RightAngle(Line(A, C), Line(A, B), length=0.3, color=YELLOW)
        
        return VGroup(triangle, right_angle)
    
    def label_triangle(self, triangle):
        """Label the vertices and sides of the triangle."""
        triangle_poly = triangle[0]
        vertices = triangle_poly.get_vertices()
        A, B, C = vertices
        
        # Labels for vertices
        label_A = Text("A").next_to(A, DOWN + LEFT, buff=0.1)
        label_B = Text("B").next_to(B, DOWN + RIGHT, buff=0.1)
        label_C = Text("C").next_to(C, UP, buff=0.1)
        
        # Labels for sides
        label_a = MathTex("a").next_to((A + B) / 2, DOWN, buff=0.4)
        label_b = MathTex("b").next_to((A + C) / 2, LEFT, buff=0.4)
        label_c = MathTex("c").next_to((B + C) / 2, np.array([0.5, 0.5, 0]), buff=0.1)
        
        return VGroup(triangle, label_A, label_B, label_C, label_a, label_b, label_c)
    
    def create_squares(self, triangle):
        """Create squares on each side of the triangle."""
        triangle_poly = triangle[0]
        vertices = triangle_poly.get_vertices()
        A, B, C = vertices
        
        # Create squares on each side
        square_a = self.create_square_on_segment(A, B, color=GREEN_D, opacity=0.7)
        square_b = self.create_square_on_segment(A, C, color="#C19A6B", opacity=0.7)  # Darker gold/brown
        square_c = self.create_square_on_segment(B, C, color="#662211", opacity=0.7)  # Dark brown-red
        
        # Calculate side lengths
        a = np.linalg.norm(B - A)
        b = np.linalg.norm(C - A)
        c = np.linalg.norm(C - B)
        
        # Create text for squares
        a_squared = MathTex("a^2").move_to(square_a).scale(0.7)
        b_squared = MathTex("b^2").move_to(square_b).scale(0.7)
        c_squared = MathTex("c^2").move_to(square_c).scale(0.7)
        
        return VGroup(square_a, square_b, square_c, a_squared, b_squared, c_squared)
    
    def create_square_on_segment(self, point1, point2, color=WHITE, opacity=0.5):
        """Create a square on a line segment from point1 to point2."""
        # Vector from point1 to point2
        v = point2 - point1
        
        # For a right angle rotation in the plane, we need (-y, x)
        # This creates a perpendicular vector in the correct direction for the square
        if point1[1] == point2[1]:  # Horizontal segment (like A to B)
            # For horizontal segments at the bottom, square goes down
            if point1[1] < 0:
                perp = np.array([0, -1, 0]) * np.linalg.norm(v)
            else:
                perp = np.array([0, 1, 0]) * np.linalg.norm(v)
        elif point1[0] == point2[0]:  # Vertical segment (like A to C)
            # For vertical segments on the left, square goes left
            if point1[0] < 0:
                perp = np.array([-1, 0, 0]) * np.linalg.norm(v)
            else:
                perp = np.array([1, 0, 0]) * np.linalg.norm(v)
        else:  # Diagonal segment (like B to C)
            # Normalize v
            v_norm = v / np.linalg.norm(v)
            # Create perpendicular vector (rotate 90 degrees counterclockwise)
            perp = np.array([-v_norm[1], v_norm[0], 0]) * np.linalg.norm(v)
            
            # Flip the hypotenuse square 180 degrees (always use this direction)
            perp = -perp  # This will flip it to the outside
        
        # Calculate the other points of the square
        point3 = point2 + perp
        point4 = point1 + perp
        
        # Create the square with adjusted appearance
        square = Polygon(point1, point2, point3, point4,
                         color=color, fill_color=color, fill_opacity=opacity,
                         stroke_width=1.5)
        
        return square
    
    def show_area_relationship(self, triangle, squares):
        """Demonstrate the relationship between the areas."""
        square_a, square_b, square_c = squares[:3]
        a_squared, b_squared, c_squared = squares[3:]
        
        # Side lengths for a 3-4-5 triangle
        a = 3    # Length of side AB
        b = 4    # Length of side AC
        c = 5    # Length of side BC (calculated from Pythagorean theorem)
        
        area_a = MathTex(f"\\text{{Area of square a}} = a^2 = {a}^2 = {a**2}").scale(0.9)
        area_b = MathTex(f"\\text{{Area of square b}} = b^2 = {b}^2 = {b**2}").scale(0.9)
        area_c = MathTex(f"\\text{{Area of square c}} = c^2 = {c}^2 = {c**2}").scale(0.9)
        area_sum = MathTex(f"a^2 + b^2 = {a**2} + {b**2} = {a**2 + b**2}")
        
        # Position area equations to match the screenshot layout
        area_a.to_edge(RIGHT, buff=0.5).shift(UP * 3)
        area_b.next_to(area_a, DOWN, buff=0.5)
        area_c.next_to(area_b, DOWN, buff=0.5)
        area_sum.next_to(area_c, DOWN, buff=0.8)
        
        # Animation sequence
        self.play(Write(area_a))
        self.play(Indicate(square_a))
        self.wait(0.5)
        
        self.play(Write(area_b))
        self.play(Indicate(square_b))
        self.wait(0.5)
        
        self.play(Write(area_c))
        self.play(Indicate(square_c))
        self.wait(0.5)
        
        self.play(Write(area_sum))
        box = SurroundingRectangle(area_sum, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(1)
        
        # Equality visualization
        equals = MathTex("=").scale(2)
        final_eq_left = area_sum.copy()
        final_eq_right = area_c.copy()
        final_eq_group = VGroup(final_eq_left, equals, final_eq_right).arrange(RIGHT, buff=0.5)
        final_eq_group.to_edge(UP, buff=1.5)
        
        self.play(
            ReplacementTransform(area_sum, final_eq_left),
            ReplacementTransform(area_c, final_eq_right),
            FadeOut(area_a),
            FadeOut(area_b),
            FadeOut(box),
        )
        self.play(FadeIn(equals))
        self.wait(2)
        
    def show_algebraic_proof(self):
        """Show a simple algebraic proof."""
        # Clear the screen
        self.play(FadeOut(*self.mobjects))
        
        # Algebraic proof
        title = Text("Algebraic Proof", font_size=48).to_edge(UP)
        self.play(Write(title))
        
        proof_steps = VGroup(
            MathTex("\\text{In a right triangle:}"),
            MathTex("\\text{Hypotenuse } c \\text{ and legs } a \\text{ and } b"),
            MathTex("\\text{By the Pythagorean Theorem:}"),
            MathTex("a^2 + b^2 = c^2")
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.5)
        
        for step in proof_steps:
            self.play(Write(step))
            self.wait(0.5)
        
        self.wait(1)
        
        # Example - updated to match our triangle with a=4.2, b=3.0, c=5.2
        example = VGroup(
            MathTex("\\text{Example with a 3-4-5 triangle:}"),
            MathTex("a = 3, b = 4, c = 5"),
            MathTex("3^2 + 4^2 = 5^2"),
            MathTex("9 + 16 = 25"),
            MathTex("25 = 25 \\checkmark")
        ).arrange(DOWN, buff=0.3).next_to(proof_steps, DOWN, buff=1)
        
        for step in example:
            self.play(Write(step))
            self.wait(0.5)
        
        self.wait(2)


class PythagoreanVisualProof(Scene):
    def construct(self):
        # Introduction
        title = Text("Visual Proof of the Pythagorean Theorem", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_edge(UP))
        
        # Create two identical squares with sides (a+b)
        square_size = 4
        
        # First square arrangement
        square1 = Square(side_length=square_size).shift(LEFT * 3)
        self.play(Create(square1))
        
        # Second square arrangement
        square2 = Square(side_length=square_size).shift(RIGHT * 3)
        self.play(Create(square2))
        
        # Create 4 right triangles
        a, b = 1.5, 2.5  # Sides of the right triangle
        
        # Function to create a right triangle
        def create_triangle(a, b, position, rotation=0):
            triangle = Polygon(
                ORIGIN,
                RIGHT * a,
                RIGHT * a + UP * b,
                UP * b,
                color=YELLOW,
                fill_opacity=0.5
            )
            triangle.rotate(rotation * DEGREES)
            triangle.shift(position)
            return triangle
        
        # Create triangles for the first square
        positions1 = [
            square1.get_corner(UL) + RIGHT * a + DOWN * b,
            square1.get_corner(UR) + LEFT * b + DOWN * a,
            square1.get_corner(DR) + LEFT * a + UP * b,
            square1.get_corner(DL) + RIGHT * b + UP * a
        ]
        rotations1 = [0, 90, 180, 270]
        
        triangles1 = VGroup(*[
            create_triangle(a, b, pos, rot)
            for pos, rot in zip(positions1, rotations1)
        ])
        
        self.play(Create(triangles1))
        
        # Label the center square
        center_square1 = Square(
            side_length=square_size - 2 * (a + b) + 2 * (a * b),
            color=BLUE,
            fill_opacity=0.5
        ).move_to(square1.get_center())
        
        c_squared1 = MathTex("c^2").move_to(center_square1.get_center())
        
        self.play(Create(center_square1), Write(c_squared1))
        
        # Create a different arrangement for the second square
        # Create triangles for the second square (different arrangement)
        triangle2_1 = create_triangle(a, b, square2.get_corner(UL) + RIGHT * a, 0)
        triangle2_2 = create_triangle(a, b, square2.get_corner(UL) + DOWN * b, 0)
        triangle2_3 = create_triangle(a, b, square2.get_corner(DR) + LEFT * a, 180)
        triangle2_4 = create_triangle(a, b, square2.get_corner(DR) + UP * b, 180)
        
        triangles2 = VGroup(triangle2_1, triangle2_2, triangle2_3, triangle2_4)
        
        self.play(Create(triangles2))
        
        # Label the center regions
        a_square = Square(side_length=a, color=GREEN, fill_opacity=0.5).move_to(
            square2.get_corner(UL) + RIGHT * a / 2 + DOWN * b + DOWN * a / 2
        )
        b_square = Square(side_length=b, color=RED, fill_opacity=0.5).move_to(
            square2.get_corner(DR) + LEFT * a + UP * b / 2 + LEFT * b / 2
        )
        
        a_squared = MathTex("a^2").move_to(a_square.get_center())
        b_squared = MathTex("b^2").move_to(b_square.get_center())
        
        self.play(
            Create(a_square),
            Create(b_square),
            Write(a_squared),
            Write(b_squared)
        )
        
        # Equation showing the relationship
        equation = MathTex("a^2 + b^2 = c^2").scale(1.5).next_to(title, DOWN, buff=1)
        self.play(Write(equation))
        
        # Explanation text
        explanation = Text(
            "Both squares have the same area (a+b)², and both contain\n"
            "4 identical right triangles. The remaining areas must be equal.",
            font_size=24
        ).next_to(equation, DOWN, buff=0.5)
        self.play(Write(explanation))
        
        # Highlight the equality
        self.play(
            Indicate(a_square),
            Indicate(b_square),
            Indicate(center_square1)
        )
        
        self.wait(2)
        
        # Final theorem statement
        final = MathTex("a^2 + b^2 = c^2").scale(2)
        self.play(FadeOut(*self.mobjects))
        self.play(Write(final))
        self.wait(2)


class InteractiveExploration(Scene):
    def construct(self):
        # Introduction
        title = Text("Exploring Different Right Triangles", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_edge(UP))
        
        # Function to create a right triangle with squares
        def create_triangle_with_squares(a, b):
            # Calculate hypotenuse
            c = np.sqrt(a**2 + b**2)
            
            # Create the triangle
            A = ORIGIN
            B = RIGHT * a
            C = RIGHT * a + UP * b
            
            triangle = Polygon(A, B, C, color=WHITE)
            right_angle = RightAngle(Line(A, B), Line(A, C), length=0.2, color=YELLOW)
            
            # Create squares on each side
            square_a = Square(side_length=a, color=GREEN, fill_opacity=0.3).move_to(B + RIGHT * a/2)
            square_b = Square(side_length=b, color=BLUE, fill_opacity=0.3).move_to(C + UP * b/2)
            
            # Create square on hypotenuse (more complex)
            # Vector from A to C
            hyp_vec = C - A
            # Rotate 90 degrees
            perp_vec = np.array([-hyp_vec[1], hyp_vec[0], 0])
            perp_vec = perp_vec / np.linalg.norm(perp_vec) * c
            
            square_c = Polygon(
                A, C, C + perp_vec, A + perp_vec,
                color=RED, fill_opacity=0.3
            )
            
            # Labels
            a_label = MathTex(f"a = {a}").next_to(square_a, DOWN)
            b_label = MathTex(f"b = {b}").next_to(square_b, LEFT)
            c_label = MathTex(f"c = {c:.2f}").next_to(square_c, UP + LEFT)
            
            # Area calculations
            a_area = MathTex(f"a^2 = {a}^2 = {a**2}").to_edge(RIGHT).shift(UP * 2)
            b_area = MathTex(f"b^2 = {b}^2 = {b**2}").next_to(a_area, DOWN)
            c_area = MathTex(f"c^2 = {c:.2f}^2 = {c**2:.2f}").next_to(b_area, DOWN)
            sum_area = MathTex(f"a^2 + b^2 = {a**2} + {b**2} = {a**2 + b**2}").next_to(c_area, DOWN)
            
            # Group everything
            triangle_group = VGroup(
                triangle, right_angle, square_a, square_b, square_c,
                a_label, b_label, c_label
            )
            equations = VGroup(a_area, b_area, c_area, sum_area)
            
            return triangle_group, equations
        
        # Create a few examples
        examples = [
            (3, 4),   # 3-4-5 triangle
            (5, 12),  # 5-12-13 triangle
            (1, 1)    # Isosceles right triangle
        ]
        
        all_groups = []
        
        for i, (a, b) in enumerate(examples):
            # Generate the triangle and equations
            triangle_group, equations = create_triangle_with_squares(a, b)
            
            # Position the triangle
            triangle_group.scale(0.7).move_to(ORIGIN).shift(DOWN * 0.5)
            
            # Add to all groups
            group = VGroup(triangle_group, equations)
            all_groups.append(group)
            
            if i == 0:
                self.play(Create(triangle_group))
                self.play(Write(equations))
                self.wait(2)
            else:
                self.play(
                    FadeOut(all_groups[i-1]),
                    FadeIn(group)
                )
                self.wait(2)
        
        # Final theorem statement
        self.play(FadeOut(*self.mobjects))
        
        conclusion = Text("The Pythagorean Theorem holds for all right triangles.", font_size=42)
        formula = MathTex("a^2 + b^2 = c^2").scale(2).next_to(conclusion, DOWN)
        
        self.play(Write(conclusion))
        self.play(Write(formula))
        self.wait(2)


if __name__ == "__main__":
    # Uncomment the scene you want to render
    # The default rendered scene would be PythagoreanTheorem
    scene = PythagoreanTheorem()
    # scene = PythagoreanVisualProof()
    # scene = InteractiveExploration()