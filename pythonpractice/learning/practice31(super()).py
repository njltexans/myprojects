# super() function is used in a child class to call methods from a parent class 
#     - It allows you to extend the functionality of the inherited methods
#     - It is used to call the constructor of the parent class



class shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self): # method to describe the shape, so that we can print more information about the shape at once (instead of indivdual print statements)
        if self.filled:
            return f"{self.color} and filled"
        else:
            return f"{self.color} and not filled"


class circle(shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # calling the constructor of the parent class
        self.radius = radius
    
    def describe(self): # overriding the describe method in the parent class
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2") # adding more information to the describe method
        return super().describe() # calling the describe method of the parent class

class square(shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class triangle(shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height


circle = circle("red", True, 5)
square = square("blue", False, 10)
triangle = triangle("green", True, 10, 5)

print(circle.color)
print(circle.filled)
print(f"{circle.radius}cm")

print(f"The circle is {circle.describe()}")

