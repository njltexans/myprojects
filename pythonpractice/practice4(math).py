import math
# arithmetic operators, math functions, exercises

#arithmetic operators
Pizza = 10
Cheese = 2

Pizza = Pizza + 1 # addition opporator
Pizza += 1 # augmented assignment operator
# This is the same for subtraction (-), multiplication (*), division(/)

Cheese = Cheese ** 5 # exponentiation operator
Cheese **= 5 # augmented assignment operator

remainder = 10 % 3 # modulus operator, returns the remainder of the division
# modulus operator determines remainder of division. Popular to be used when determine if a number is odd or even




# Built-in math functions (rounding,  

x = 3.245
y = -4
z = 6

result = round(x) #rounds up the function to nearest whole number (can specify decimal palce with ,2 ,3 etc.)

result = abs(y) #absolute value of y, distance away from zero as a whole number 

result = pow(y, z) # Power function (y to the power of 5)

result = max(x, y, z) #What is the maximum value between x, y, and Z

result = min(x, y, z) #What is the min value between listed varibles, integers, etc.


# Math module
# import math (done at the top of the file)
# math module contains mathematical functions and constants

print(math.pi) #math module, pi constant
print(math.e) #math module, e constant
print(math.inf) #math module, infinity constant
print(math.nan) #math module, not a number constant 

result = math.sqrt(16) #math module, square root function
result = math.ceil(3.7) #math module, ceiling function, rounds floating number up to the nearest whole number
result = math.floor(3.7) #math module, floor function, rounds floating number down to the nearest whole number

print(result)
