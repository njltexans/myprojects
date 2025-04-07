# Polymorphism means to have "many forms and faces"
#   -Poly = many
#   -Morph = forms

#   2 ways to achieve polymorphism:
#     1) Inheritance, which is an object that can be treated as a parent or child class (treated same way)
#     2) Duck Typing, which must have necessary attribute/methods

from abc import ABC, abstractmethod

class shape:
    
    @abstractmethod
    def area(self):
        pass



class rectangle(shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    

class circle(shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


class triangle(shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height 

    def area(self):
        return 0.5 * self.base * self.height  
    

class pizza(circle): # pizza inherits from circle

    def __init__(self, toppings, radius):
        self.toppings = toppings
        super().__init__(radius)  # super() calls the parent class constructor

shapes = [circle(4), rectangle(4, 7), triangle(8, 5), pizza(["cheese", "meat"], 12)] 


for shape in shapes:
    print(shape.area())

