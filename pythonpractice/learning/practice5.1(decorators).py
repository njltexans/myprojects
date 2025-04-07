# Decorator is a function that extands the behavior of another function without modifying the base function.

# @add_sprinkeles
# get_ice_cream("vanilla")

def add_sprinkles(func):  # Decorator function
    def wrapper(*args, **kwargs):  # Wrapper function, which ensures that the sprinkles are added before the base function is called
        print("Here are your sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):  # Decorator function
    def wrapper(*args, **kwargs):  # Wrapper function, which ensures that the fudge is added before the base function is called
        print("Here is your fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge #Decorator (outlined above)
@add_sprinkles #Decorator (outlined above)
def get_ice_cream(flavor): #Base function
    print(f"Here is your {flavor} ice cream")


get_ice_cream("vaniilla") #Calling the base function






