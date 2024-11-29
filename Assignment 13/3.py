import math

class Shape:
    def getPerimeter(self):
        pass

    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    circle = Circle(5)
    print(f"Perimeter of the circle: {circle.getPerimeter():.2f}")
    print(f"Area of the circle: {circle.getArea():.2f}")