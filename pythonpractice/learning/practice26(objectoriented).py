# Object oriented programming
# Object = A "bundle" of related attributes (variables) and methods (functions)
# Examples: phone, cup, book, computer, etc.
# You need a "class  to create many objects 
# 
# Class = A blueprint for creating objects, used to design the structure and layout of objects


class Car:
    def __init__(self, color, model, year, for_sale): # Constructor method, this are the parameters for the object created
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} is now driving.") # f-string, used to format the string, {salf.model} is a placeholder for the model attribute
    
    def stop(self):
        print(f"{self.model} has stopped.")
    
    def describe(self):
        print(f'The car is a {self.color} {self.model} from {self.year}.')
    
    def sale(self):
        if self.for_sale:
            print(f'The {self.year} {self.color} {self.model} is for sale.')
        else:
            print('The {self.year} {self.color} {self.model} is not for sale.')

car1 = Car("red", "Toyota", 2020, True) # Creating an object of the class Car, pass in the parameters (refer to the __init__ method above)
car2 = Car("black", "Honda", 2011, False)
car3 = Car("blue", "Nissan", 2018, True)

car1.drive() # Accessing the methods of the object (can do this for car2 and car3 as well)
car1.stop() # Accessing the methods of the object

print(car1.color) # Accessing the attributes of the object (if you just print "car1", you will get the memory location of the object)
print(car1.model)
print(car1.year)    
print(car1.for_sale)