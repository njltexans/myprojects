# Lamda functions are small anonymous functions for one time use (then thrown away)
#   - They take any number of arguments, but can only have one expression
#   - Syntax: lambda arguments: expression
#   - sort(), filter(), map(), reduce() functions are used with lambda functions

# Example lambda function:

# map(lambda x: x * 2, numbers)  # Doubles each item in the list

duoble = lambda x: x * 2 # Doubles the input, accepts one argument (x)

print(duoble(5))  # Can be called like a regular function, substituting x with whatever value you want


add = lambda x, y: x + y  # Adds two arguments (x, y)

print(add(5, 3))  # Can be called like a regular function, substituting x and y with whatever values you want


max_value = lambda x, y: x if x > y else y  # Returns the greater of the two arguments (x, y)

print(max_value(5, 3))  # Can be called like a regular function, substituting x and y with whatever values you want


age_check = lambda age: True if age >= 18 else False  # Returns True if the argument is 18 or older, otherwise False

print(age_check(21))  # Can be called like a regular function, substituting age with whatever value you want