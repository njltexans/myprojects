# Creating a simple python calculator
# User will select arithmetic operator and input numbers

operator = input("Enter an operator (+, -, *, /): ")
if operator not in ['+', '-', '*', '/']:
    print("What are you doing?")
    exit()

try:
    num1 = float(input("Enter first number: "))
except ValueError:
    print("That's not a number silly goose!")
    exit()

try:
    num2 = float(input("Enter second number: "))
except ValueError:
    print("This isn't english class funny boy!")
    exit()

if operator == "+":
    print(f"{num1 + num2}")
elif operator == "-":
    print(f"{num1 - num2}")   
elif operator == "*":
    print(f"{num1 * num2}")
elif operator == "/":
    print(f"{num1 / num2}")
else:
    print("Idk what you're doing but it ain't math")