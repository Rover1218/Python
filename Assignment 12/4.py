import math
class Shape:
    def area(self, *args):
        if len(args) == 1:
            return math.pi * args[0] ** 2
        elif len(args) == 2:
            return args[0] * args[1]
        elif len(args) == 2 and args[0] == "square":
            return args[1] ** 2
        else:
            return "Invalid arguments."

shape = Shape()
print(f"Area of circle (radius = 5): {shape.area(5):.2f}")
print(f"Area of rectangle (length = 4, breadth = 6): {shape.area(4, 6)}")
print(f"Area of square (side = 3): {shape.area('square', 3)}")
