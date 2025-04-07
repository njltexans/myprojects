# Abstract class is a class that can't be instantiated on its own. It is designed to be subclasses (inherited by other classes.)
#    - They can contain abstract methods, which are declared but have no implementation
#    - Abstract classes benefits:
#       - Provides a blueprint for other classes
#       - Forces the implementation of methods (Requires children to use inherited abstract methods)
#       - Helps to maintain a standard (prevents instantiation of the class itself)


from abc import ABC, abstractmethod # ABC = Abstract Base Class

class vehicle(ABC): # Abstract class
    @abstractmethod # Decorator to declare abstract method
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class car(vehicle): # Child that Inherits from vehicle
    def go(self): # Must implement the abstract methods
        print("Car is moving")

    def stop(self):
        print("Car stopped")


car = car()
car.go()
car.stop()

class bike(vehicle): # Child that Inherits from vehicle
    def go(self): # Must implement the abstract methods
        print("Bike is moving")

    def stop(self):
        print("Bike stopped")

bike = bike()
bike.go()   
bike.stop()

class boat(vehicle): # Child that Inherits from vehicle
    def go(self): # Must implement the abstract methods
        print("Boat is sailing")

    def stop(self):
        print("Boat stopped")

boat = boat()
boat.go()
boat.stop()



