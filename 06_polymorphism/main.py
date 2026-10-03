from shape import *

# square = Shape()

shapes = [Circle(7), Square(7), Triangle(7,7), Pizza(True,22)]
for shape in shapes:
    print(f"Area: {shape.area()} cm²")