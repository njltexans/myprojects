# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
# If the number is a multiple of 4, print out a different message

number = int(input("Enter your number here: "))

if number % 4 == 0:
    print(f"{number} is divisible by 4 and even")

elif number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")


