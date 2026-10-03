import math as m
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return m.pi * m.pow(self.radius, 2)

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return m.pow(self.width, 2)


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return float(0.5 * self.width * self.height)


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping