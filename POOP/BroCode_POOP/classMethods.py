# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

class Student:

    count = 0
    gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.gpa += gpa
    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_student_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Total average of students' GPA: {cls.gpa / cls.count:.2f}"


student1 = Student("Spongebob", 3.00)
student2 = Student("Patrick", 1.50)

print(student1)
print(student1.get_info())
print(student2.get_info())
print(Student.get_student_count())
print(Student.get_gpa())
