# Another way to achieve polymorphism besides Inheritance
# Objects must have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck"

from animal import *

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)