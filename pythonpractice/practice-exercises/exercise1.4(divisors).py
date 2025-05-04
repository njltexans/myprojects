# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Ask the user for a number
number = int(input("Enter your number here: "))

# Create an empty list to store divisors
divisors = []

# Loop through numbers from 1 to the given number
for i in range(1, number + 1):
    if number % i == 0:  # Check if i is a divisor
        divisors.append(i)

# Print the list of divisors
print(f"The divisors of {number} are: {divisors}")


