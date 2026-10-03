# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefits: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method
#             _variable = private decorator
from shape import *

rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)
