# multiple inheritance = inherit from more than one parent class C(A, B)

# multilevel inheritance = inherit from aa parent which inherits from another parent
#                           C(B) <- B(A) <- A

from Prey import *

rabbit = Rabbit("RRR")
hawk = Hawk("HHH")
fish = Fish("FFF")

rabbit.eat()