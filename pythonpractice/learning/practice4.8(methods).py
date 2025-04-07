# Class methods allow operators to relate to the class itself rather than instances of the class
#      - Used for operations that involve the class itself

class student:

    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa, grade):
        self.name = name
        self.gpa = gpa
        self.grade = grade
        student.count += 1
        student.total_gpa += gpa
    
    def get_info(self): # Instance method
        return f"{self.name} has a {self.gpa} GPA and is in grade {self.grade}"
    
    @classmethod
    def get_count(cls): # Class method
        return f"Total # of students: {cls.count}" #modifies the class variable count
    
    @classmethod
    def get_total_gpa(cls): # Class method
        if cls.count == 0:
            return "No students"
        else:
            return f"Average GPA: {cls.total_gpa/cls.count:.2f}" #modifies the class variable total_gpa
    

student1 = student("Spongebob", 3.5, 12)
student2 = student("Daffy", 2.5, 11)
student3 = student("Dr.Doofenshmirtz", 5.0, 12)
    

print(student2.get_info())
print(student1.get_info())
print(student3.get_info())

print(student.get_count())
print(student.get_total_gpa()) # Returns the average GPA of all students