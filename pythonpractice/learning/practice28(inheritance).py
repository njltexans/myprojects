# inheritance allows a class to inherit attributes and methods from another class (like a kid in real life inherating traits from their parents)
#       - Helps with code reusability and extensibility
#       - class Child(Parent):


# Example:

class Father: # Parent class
    height = 182
    color = "brown"

class Son(Father): # Child class
    pass



# Example2:

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    

class Dog(Animal): # Dog class inherits from Animal class
    def speak(self): #Can set up a method that is unique to the Dog class, the other inherited classes will still be valid
        print("Woof")

class Cat(Animal): # Cat class inherits from Animal class
    def speak(self):
        print("Meow")    

class Platapus(Animal): # Platapus class inherits from Animal class
    def speak(self):
        print("Hey I'm Perry!")


dog = Dog("Daffy")
cat = Cat("Speedy")
Platapus = Platapus("Perry")


print(dog.name) #Can do this for dog, cat, and platapus just have to change the object
print(dog.is_alive)
dog.eat()
dog.sleep()







