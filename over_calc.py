
import math
class ShapeCalculator:
    def __init__(self):
        self.shapes = {
            "rectangle": self.calculate_rectangle_area,
            "circle": self.calculate_circle_area,
            "triangle": self.calculate_triangle_area
        }

    def calculate_area(self, shape_name, *args):
        if shape_name.lower() in self.shapes:
            return self.shapes[shape_name.lower()](*args)
        else:
            raise ValueError(f"Invalid shape: {shape_name}")

    def calculate_rectangle_area(self, length=0, width=0):
        if isinstance(length, (int, float)) and isinstance(width, (int, float)) and length >= 0 and width >= 0:
            return length * width
        else:
            raise ValueError("Invalid arguments for rectangle")

    def calculate_circle_area(self, radius=0):
        if isinstance(radius, (int, float)) and radius >= 0:
            return math.pi * radius ** 2
        else:
            raise ValueError("Invalid argument for circle")

    def calculate_triangle_area(self, base=0, height=0):
        if isinstance(base, (int, float)) and isinstance(height, (int, float)) and base >= 0 and height >= 0:
            return 0.5 * base * height
        else:
            raise ValueError("Invalid arguments for triangle")

# Example usage:
calculator = ShapeCalculator()

try:
    shape_name = input("Enter shape name (rectangle, circle, triangle): ").strip()
    shape_name = shape_name.lower()

    if shape_name not in ("rectangle", "circle", "triangle"):
        raise ValueError(f"Invalid shape: {shape_name}")

    if shape_name == "rectangle":
        length_str = input("Enter length: ").strip()
        width_str = input("Enter width: ").strip()

        if not length_str or not width_str:
            raise ValueError("Both length and width must be provided")

        length = float(length_str)
        width = float(width_str)

        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")

        print("Rectangle Area:", calculator.calculate_area("rectangle", length, width))

    elif shape_name == "circle":
        radius_str = input("Enter radius: ").strip()

        if not radius_str:
            raise ValueError("Radius must be provided")

        radius = float(radius_str)

        if radius < 0:
            raise ValueError("Radius must be non-negative")

        print("Circle Area:", calculator.calculate_area("circle", radius))

    elif shape_name == "triangle":
        base_str = input("Enter base: ").strip()
        height_str = input("Enter height: ").strip()

        if not base_str or not height_str:
            raise ValueError("Both base and height must be provided")

        base = float(base_str)
        height = float(height_str)

        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative")

        print("Triangle Area:", calculator.calculate_area("triangle", base, height))

except ValueError as e:
    print(f"Error: {e}")
