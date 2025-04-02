# Duck typing is a concept related to polymorphism. It is a way to design code in which an object's methods and properties are used rather than the object's type itself.
# Another way to achieve polymorphism besides using inheritance
#       - Object must have the minimum necessary attributes/methods
#       - "If it walks like a duck, quacks like a duck, then it must be a duck"


class animal:
    alive = True


class duck(animal):
    def speak(self):
        print("Quackity quack quack")   

class cat(animal):
    def speak(self):
        print("Meowy meow meow")

class car: #it quacks like a duck so we can treat it like a duck (a honk can be considered speaking)

    alive = False
    def speak(self):
        print("Honky honky AWOOOOGAAAA")

animals = [duck(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
