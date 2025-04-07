# function = a block of code that is resuable
# function is defined using the def keyword
#     place () after the function name to invoke it


def happy_birthday(name, age): # defining a function
    print(f"Happy Birthday to {name}!")
    print(f"Happy Birthday to {name}!")
    print(f"Happy Birthday dear {name}!")
    print(f"Happy Birthday to {name}!")

happy_birthday("Joey") # invoking the function, each time invoked is one time it is printed

happy_birthday("Speedy") # invoking the function with an argument, "Speedy will replace the {name} in the function"
#One name will be printed each single time the function is invoked

def add(a, b): # defining a function with two arguments
    return a + b # return statement returns the value of a + b
# Example: happy_birthday("Joey", 30) # invoking the function with two arguments, "Joey" and 30
#the order of the parameters matters, the first parameter will be assigned to the first argument and the second parameter will be assigned to the second argument


#return statement is used to return a value from a function back to the place where the function was called
#return statement can be used to exit a function

def add(a, b):
    x = a + b
    return x # return statement returns the value of x

def subtract(a, b):
    x = a - b
    return x

def multiply(a, b):
    x = a * b
    return x

def divide(a, b):
    x = a / b
    return x

print(add(10, 20))
print(subtract(10, 20))
print(multiply(10, 20))
print(divide(10, 20)) #the function becomes the answer of the equations 





