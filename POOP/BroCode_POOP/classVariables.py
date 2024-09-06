# class variables =Shared among all instances of a class
#                 Defined outside the constructor
#                 Allow you to share data among all objects created from that class

#GOOD PRACTICE TO ACCESS A CLASS VARIABLE BY THE NAME OF A CLASS
class Student:

    class_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student_1 = Student("Jeays", 22)
student_2 = Student("Queen", 24)

print(student_1.name)
print(student_2.age)

print(student_1.class_year)

#GOOD PRACTICE TO ACCESS A CLASS VARIABLE BY THE NAME OF A CLASS (NOT ANY INSTANCE FROM THE CLASS)
# HELPS WITH CLARITY & READABILITY
print(Student.class_year)
print(Student.num_students)

print(f"The number of students for class {Student.class_year} is {Student.num_students}")