# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself



from student import *
student1 = Student("A", 3)
student2 = Student("A", 3)
student3 = Student("A", 3)
student4 = Student("A", 4)
student5 = Student("A", 3)

print(Student.get_count())
print(Student.get_avg_gpa())