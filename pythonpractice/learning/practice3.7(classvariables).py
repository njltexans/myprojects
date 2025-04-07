# class variables = shared among all instances of a class
#    - defined outside of any methods in the class (outside the constructor)
#    - Can share data among all objects created from that class

class student:
    #class variable
    class_year = "2021"
    student_population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.student_population += 1 #increment student population by 1. (name of class.variable) when printed returns 2 (since there are 2 students)

student1 = student("Bobby Shmeet", 18) #instance of student class
student2 = student("Tiummy Shmurda", 29)

print(f"My graduation year was {student.class_year}, and my graduating class had {student.student_population} students.") #prints "My graduation year was 2021, and my graduating class had 2 students." since there are 2 students

