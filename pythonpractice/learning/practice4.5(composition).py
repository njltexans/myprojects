# Aggregation is a relationship where the child can exist independently of the parent.
#       - "has-a" relationship

# Composition is a relationship where the child cannot exist independently of the parent.
#       - "owns-a" relationship


class engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class wheel:
    def __init__(self, size):
        self.size = size

class car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = engine(horsepower) #passing in the horsepower from engine class
        self.wheel = [wheel(wheel_size) for i in range(4)] #passing in the wheel size from wheel class, 4 times since car has 4 wheels

    def diplay_car(self):
        return f"{self.make} {self.model} with {self.engine.horsepower} horsepower and {self.wheel[0].size} inch wheels" #displaying the car make, model, engine horsepower and wheel size


car1 = car(make="Tesla", model="Model 3", horsepower=10, wheel_size=3)
car2 = car(make="BYD", model="Awesome", horsepower=5000, wheel_size=15)

print(car.diplay_car()) # Tesla Model 3 with 10 horsepower and 3 inch wheels 