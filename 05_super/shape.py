import math as m
class Shape:
    def __init__(self, name, color, is_filled):
        self.name = name
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, name, color, is_filled, radius):
        super().__init__(name, color, is_filled)
        self.radius = radius

    # method overriding
    def describe(self):
        area = m.pi * m.pow(self.radius, 2)
        print(f"It is a Circle. \nArea: {area:.2f}cm")
        super().describe()


class Square(Shape):
    def __init__(self, name, color, is_filled, width):
        super().__init__(name, color, is_filled)
        self.width = width

    def describe(self):
        area = m.pow(self.width, 2)
        print(f"It is a Square. \nArea: {area:.2f}cm")
        super().describe()

class Triangle(Shape):
    def __init__(self, name, color, is_filled, width, height):
        super().__init__(name, color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        area = float(0.5 * self.width * self.height)
        print(f"It is a Triangle. \nArea: {area:.2f}cm")
        super().describe()