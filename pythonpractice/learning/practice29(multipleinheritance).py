# Multiple inheritance is when a child class inherits from more than one parent class
#           - class Child(Parent1, Parent2):

# mutilevel inheritance is when a child class inherits from a parent class that also inherits from another parent class (inheritance inception)
#           - C(B) <- B(A) <- A
#           - class C(B):
#           - class B(A):

class Animal:

    def __init__(self, name): #Constructor that initializes the name attribute
        self.name = name 
    
    def eat(self):
        print(f"{self.name} is snackin!")
    
    def sleep(self):
        print(f"{self.name} is snoooozzzin")


class prey(Animal): #Inherits from Animal
    def flee(self):
        print(f"{self.name} is skedadlin out of there!")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is on the prowl")

class ardvark(prey, predator): #Multiple inheritance
    pass

class evil_dodo(predator): #inherits from predator and Animal
    pass

class ant(prey):
    pass



ardvark = ardvark("Arthur")
evil_dodo = evil_dodo("Dr. Doom")
ant = ant("Armando")


ardvark.eat()
evil_dodo.hunt()
ant.flee()

