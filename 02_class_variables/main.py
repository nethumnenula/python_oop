# Shared among all instances of a class
# Defined outside the constructor
# Allow you to share data among all objects created from that class

from student import Student

student1 = Student("Nethum", 22)
student2 = Student("Nethum2", 22)
student3 = Student("Nethum3", 22)

print(student1.name)
print(Student.class_year)
print(Student.num_students)