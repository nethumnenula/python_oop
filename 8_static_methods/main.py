# Static Methods = A method that belongs to class rather than any object from that class/instance
#                  Usually used for general utility functions

# Instance Methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

from employee import *

employee1 = Employee("Nethum", "Manager")
employee2 = Employee("Nenula", "Cashier")
employee3 = Employee("Nenula2", "Cook")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())